import json
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""functions subsetplot(), save_dftocsv() are created
"""

sys.setrecursionlimit(100000)

Data = pd.read_json('data.json')

sliced_df = Data[["name", "species_taxid", "hosts"]]

df_exploded = sliced_df.explode('hosts')
clusterlist = ['waterrelated', 'plantandvegetables', 'humanrelated', 'animal', 'insect', 'landsoil',
               'searelated', 'others', 'wastewater', 'food']


def get_lowest_order_items(nested_dict):
    """docstring
    """

    lowest_items = []

    def recursive_search(current_dict):
        for key, value in current_dict.items():
            if isinstance(value, dict) and value:
                recursive_search(value)
            else:
                lowest_items.append(key)

    recursive_search(nested_dict)
    return lowest_items


def subsetplot(subset, typeoflist, title='', saveplot=False):
    """docstring
    """

    condition = []
    if typeoflist == 'host':
        condition = df_exploded['hosts'].isin(subset)
    elif typeoflist == 'phage':
        subset = [int(i) for i in subset]
        condition = df_exploded['species_taxid'].isin(subset)

    filtered_df = df_exploded[condition]

    ############
    # Plotting #
    ############

    df_subset = filtered_df

    binary_matrix = pd.crosstab(df_subset['name'], df_subset['hosts'])

    # Sort the rows and columns for better visualization
    binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)
    try:

        cmap = sns.cm.rocket_r
        h = sns.clustermap(data=binary_matrix,
                           cmap=cmap, method='ward')
        h.fig.suptitle(title)
        # Clustermap returns this Object which has the built-in calls for row/col order
        rowinfo = h.dendrogram_row.reordered_ind

        columninfo = h.dendrogram_col.reordered_ind

        # can be uncommented to save the figure
        if saveplot is not False:
            plt.savefig(saveplot)
        else:
            plt.show()
        # calling original names of the phage and host by indexing with available info
        columnlist = [binary_matrix.columns[i] for i in columninfo]
        rowlist = [binary_matrix.index[i] for i in rowinfo]

        # Rearranging the binary matrix into the order clustermap did
        newdf = binary_matrix[columnlist]
        newdf = newdf.reindex(rowlist)

        # CLustered binary matrix is ready to be annotated
        # Extracting necessary information from the source-subsetted DF
        filtered_df['name'] = pd.Categorical(filtered_df['name'], categories=rowlist, ordered=True)

        # rearreanging the original DF from which the binary matrix was created.
        # to extract the original index number from the order.
        # Sort the original source-subsetted DataFrame based on the custom order
        extradf = filtered_df.sort_values('name')
        # Duplicated has to be dropped because of multiple phage entry gives different shape of DF
        extradf = extradf.drop_duplicates(subset='name')
        extradf.dropna(axis='index')
        extradf = (extradf.dropna(axis='index'))
        # print(extradf)
        # Assigning taxids, source, and original index to the BINARY into CSV
        # THIS HAS TO BE CROSS-CHECKED
        species_taxid = (list(extradf.species_taxid))

        originalindex = list(extradf.index)
        isolationsource = list()
        hosttaxids = {'species_taxid': None, "prev_index": None, 'isolation_source': None}
        with open('host_taxid_name.json', 'r') as datafile:
            hosttaxid = json.load(datafile)
            for taxid in columnlist:
                hosttaxids[taxid] = [hosttaxid[taxid]]
        hosttaxids = (pd.DataFrame(hosttaxids))
        # print(hosttaxids)
        with open('IsolationSource.json', 'r') as datafile:
            data = json.load(datafile)


            for taxid in species_taxid:
                try:
                    isolationsource.append(data[str(taxid)])
                except KeyError:
                    isolationsource.append("NO INFO")
        newdf.insert(0, 'isolation_source', isolationsource, True)
        newdf.insert(0, 'prev_index', originalindex, True)
        newdf.insert(0, 'species_taxid', species_taxid, True)
        # .drop('hosts', axis=1)
        newdf = pd.concat([hosttaxids, newdf], ignore_index=False)
        # newdf.set_index('index')
        # print(originalindex)
        return newdf
    except ValueError as e:
        print(
            f"Error occured: {e} \nMake sure you correctly specify type of list is either host"
            f" OR phage and it matches that of subset")
    except Exception as e:
        print(f"Error occured: {e}")


# s = hostcladeplot(actinomycota_species, Title='Title')

def save_dftocsv(pddf, saveloc):
    """docstring
    """
    filepath = Path(saveloc)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    pddf.to_csv(filepath)
