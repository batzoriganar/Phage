##FIRST DEFINE Bacterial interest group
##CLuster heatmap interaction
# do Phages that infect multiple bacteria live in the same environment?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path
import sys
sys.setrecursionlimit(100000)



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


def hostcladeplot(subset, typeoflist, Title=''):
    '''Subset of ids of phages can be defined'''
    if typeoflist == 'host':
        condition = df_exploded['hosts'].isin(subset)
    elif typeoflist == 'phage':
        condition = df_exploded['name'].isin(subset)

    filtered_df = df_exploded[condition]
    # whatever_df = df_exploded['species_taxid'].symmetric_difference(soilID)

    # print(filtered_df)


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
    # plt.savefig(f"D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\HostClust\MultiPhage.pdf")

    # calling original names of the phage and host by indexing with available info
    columnlist = [binary_matrix.columns[i] for i in columninfo]
    rowlist = [binary_matrix.index[i] for i in rowinfo]

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
    # print(extradf)
    # Assigning taxids, source, and original index to the BINARY into CSV
    ### THIS HAS TO BE CROSS-CHECKED
    species_taxid = (list(extradf.species_taxid))

    originalindex = list(extradf.index)
    isolationsource = list()
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
                isolationsource.append("n/a")
    newdf.insert(0, 'index', originalindex, True)
    newdf.insert(0, 'species_taxid', species_taxid, True)
    newdf.insert(2, 'isolation_source', isolationsource, True)
    # newdf.set_index('index')
    # print(originalindex)
    return newdf
def save_dftocsv(pddf, saveloc):

    filepath = Path(saveloc)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    pddf.to_csv(filepath)

with open('hierarchy_host.json' , 'r') as datafile:
    data=json.load(datafile)

Data=pd.read_json('data.json')

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 100)
# print(Data)

interactiondict={}
multihoster={}

for i in range(len(Data)):
    hostrange=(len(Data['hosts'][i].keys()))
    if hostrange >1:
        multihoster[Data['name'][i]]=list(Data['hosts'][i].keys())

#calling expanded DF into work
df_exploded= pd.read_json("Data_exploded.json")
countdf=(df_exploded['hosts'].value_counts())
hosts_with_multiple_phages=(countdf.loc[countdf > 0].index.tolist())

print(hosts_with_multiple_phages)

#Defining filter condition
calllist = (list(multihoster.keys()))
# s = hostcladeplot(actinomycota_species, Title='Title')


# Creating a DF object from the clustering


#Saving rearranged dataframe into csv
# s = hostcladeplot( calllist, typeoflist='phage', Title="Phages with multiple hosts")
# path="D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\HostClust\MultiHost.csv"
# save_dftocsv(s,path)

#
# hostplot = hostcladeplot( hosts_with_multiple_phages, typeoflist='host', Title="Hosts with multiple phages")
# path="D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\HostClust\MultiPhage.csv"
# save_dftocsv(hostplot,path)