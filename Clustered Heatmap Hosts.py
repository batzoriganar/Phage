##FIRST DEFINE Bacterial interest group
##CLuster heatmap interaction
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path
import sys
sys.setrecursionlimit(100000)


with open('hierarchy_host.json' , 'r') as datafile:
    data=json.load(datafile)

Data=pd.read_json('data.json')

sliced_df= Data[["name", "species_taxid", "hosts"]]

df_exploded = sliced_df.explode('hosts')

actinomycota=(data['2']['1224'])
# for i in (actinomycota):
#     print(actinomycota[i])
#     print('sssssssssssss')
def get_lowest_order_items(nested_dict):
    lowest_items = []

    def recursive_search(current_dict):
        for key, value in current_dict.items():
            if isinstance(value, dict) and value:
                recursive_search(value)
            else:
                lowest_items.append(key)

    recursive_search(nested_dict)
    return lowest_items
actinomycota_species=get_lowest_order_items(actinomycota)

print(actinomycota_species)


'''"lineage": [
          "2": {
    "1224": {
      "1236": {
        "91347": {
          "543": {'''

def hostcladeplot(subset, Title=''):


    condition = df_exploded['hosts'].isin(subset)

    filtered_df = df_exploded[condition]
    # whatever_df = df_exploded['species_taxid'].symmetric_difference(soilID)

    print(filtered_df)


    ############
    # Plotting #
    ############

    df_subset= filtered_df.iloc[:1500]
    # print(df_subset)

    binary_matrix = pd.crosstab(df_subset['name'],df_subset['hosts'])

    # Sort the rows and columns for better visualization
    binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)

    # print(binary_matrix)
    cmap = sns.cm.rocket_r
    h = sns.clustermap(data=binary_matrix,
                       cmap=cmap, method='ward')
    h.fig.suptitle(Title)
    plt.show()
    # Clustermap returns this Object which has the built-in calls for row/col order
    rowinfo = h.dendrogram_row.reordered_ind

    columninfo = h.dendrogram_col.reordered_ind

    # can be uncommented to save the figure
    # plt.savefig(f"D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\ClustMAP\{clusterid}.pdf")

    # calling original names of the phage and host by indexing with available info
    columnlist = [binary_matrix.columns[i] for i in columninfo]
    rowlist = [binary_matrix.index[i] for i in rowinfo]
    print(f'columnlist:{columnlist}')
    # Rearranging the binary matrix into the order clustermap did
    newdf = binary_matrix[columnlist]
    newdf = newdf.reindex(rowlist)

    ###CLustered binary matrix is ready to be annotated
    # Extracting necessary information from the source-subsetted DF
    filtered_df['name'] = pd.Categorical(filtered_df['name'], categories=rowlist, ordered=True)

    ### rearreanging the original DF from which the binary matrix was created.
    ### to extract the original index number from the order.
    # Sort the original source-subsetted DataFrame based on the custom order
    extradf = filtered_df.sort_values('name')
    # Duplicated has to be dropped because of multiple phage entry gives different shape of DF
    extradf = extradf.drop_duplicates(subset='name')
    extradf.dropna(axis='index')
    extradf = (extradf.dropna(axis='index'))
    print(extradf)
    # Assigning taxids, source, and original index to the BINARY into CSV
    ### THIS HAS TO BE CROSS-CHECKED
    species_taxid = (list(extradf.species_taxid))

    originalindex = list(extradf.index)
    isolationsource = list()
    hosttaxids = {'species_taxid':None, "prev_index":None, 'isolation_source':None}
    with open('host_taxid_name.json', 'r') as datafile:
        hosttaxid = json.load(datafile)
        for taxid in columnlist:
            hosttaxids[taxid] = [hosttaxid[taxid]]
    hosttaxids = (pd.DataFrame(hosttaxids))
    print(hosttaxids)
    with open('IsolationSource.json', 'r') as datafile:
        data = json.load(datafile)

        # Extract terms from the data
        terms = list(data.values())
        ids = list(data.keys())

        # Step 1: Data Preprocessing (convert to lowercase)
        terms = [term.lower() for term in terms]
        # print(data[str(id)])
        for id in species_taxid:
            try:
                isolationsource.append(data[str(id)])
            except KeyError:
                isolationsource.append("NO INFO")
    newdf.insert(0, 'isolation_source', isolationsource, True)
    newdf.insert(0, 'prev_index', originalindex, True)
    newdf.insert(0, 'species_taxid', species_taxid, True)
    # .drop('hosts', axis=1)
    newdf = pd.concat([hosttaxids,newdf],ignore_index=False)
    # newdf.set_index('index')
    # print(originalindex)
    return newdf

s = hostcladeplot(actinomycota_species, Title='Title')

def save_dftocsv(pddf, saveloc):

    filepath = Path(saveloc)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    pddf.to_csv(filepath)

print(s)
path="D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\HostClust\PhylPseudomonadota.csv"
save_dftocsv(s,path)

# # with open('Host tree.pkl', 'rb') as fp:
#     person = pickle.load(fp)
#
# print(person)
# # CLuster 2: soil
# # Cluster 7: _water_
# # CLuster 10: Seawater
# # CLuster 5: sewage
# # Cluster 1 : Miscellaneous (river, lakes included)
# # Cluster 9: Sea
# # CLuster 4: Wastewater
# # Cluster 8: Patient + some strain
# # CLuster 3: iron chloride precipitation of 0.2um-filtered seawater, resuspended in oxalate solution]
# # Cluster 6: Municipal Sewage