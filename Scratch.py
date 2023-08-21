import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path

Data=pd.read_json('data.json')

# sliced_df= Data[["name", "species_taxid", "hosts"]]

df_exploded = Data.explode('hosts')
lookupname={2: 'soil', 7: "_water_", 10: "seawater", 5: 'sewage',
            1: 'Miscellaneous', 9: '_sea_', 4: "Wastewater", 8: 'Patient + some strain',
            3: 'Iron chloride ppt', 6: "Municipal sewage"}
# CLuster 2: soil
# Cluster 7: _water_
# CLuster 10: Seawater
# CLuster 5: sewage
# Cluster 1 : Miscellaneous (river, lakes included)
# Cluster 9: Sea
# CLuster 4: Wastewater
# Cluster 8: Patient + some strain
# CLuster 3: iron chloride precipitation of 0.2um-filtered seawater, resuspended in oxalate solution]
# Cluster 6: Municipal Sewage
def plotter(clusterid, clustermethod='ward'):
    # print(df_exploded)
    with open('Clustered.json' , 'r') as datafile:
        clusters=json.load(datafile)

    calledcluster=clusters[str(clusterid-1)]
    #
    # print((calledcluster))

    clustercallID=[int(id) for id, text in calledcluster]

    print(len(clustercallID))

    condition = df_exploded['species_taxid'].isin(clustercallID)

    filtered_df = df_exploded[condition]
    # whatever_df = df_exploded['species_taxid'].symmetric_difference(soilID)

    # print(filtered_df)
    print(len(filtered_df))

    ############
    # Plotting #
    ############

    df_subset= filtered_df.iloc[:len(clustercallID)]
    # print(df_subset)

    binary_matrix = pd.crosstab(df_subset['name'], df_subset['hosts'])





    ExpandPlot=((.2*(len(binary_matrix.columns))),(.2*(len(binary_matrix.index))))

    cmap = sns.cm.rocket_r
    h = sns.clustermap( data= binary_matrix,
                    cmap=cmap, method='ward')
    h.fig.suptitle(f'{lookupname[clusterid]}')

    roworder=h.dendrogram_row.reordered_ind
    columnorder= h.dendrogram_col.reordered_ind
    columnlist= [binary_matrix.columns[i] for i in columnorder]
    rowlist=[binary_matrix.index[i] for i in roworder]
    print(len(roworder))
    print(len(rowlist))

    filtered_df['name'] = pd.Categorical(filtered_df['name'], categories=rowlist, ordered=True)
    ### rearreanging the original DF from which the binary matrix was created.
    ### to extract the original index number from the order.
    # Sort the DataFrame based on the custom order

    extradf = filtered_df.sort_values('name')
    print(f'this is the BEFORE ', extradf.info())
    extradf = extradf.drop_duplicates(subset='name')
    print(f'this is the extra ', extradf.info())
    newdf=binary_matrix[columnlist]
    newdf=newdf.reindex(rowlist)
    print(newdf.info)

    external_df = pd.DataFrame({'order_col': roworder})
    print(external_df)
    # print(binary_matrix)
    # print(len(rowinfo), len(columninfo))
    # # # plt.savefig(f"D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\Figures\{lookupname[clusterid]}cluster half.pdf")
    plt.show()


def save_dftocsv(pddf, saveloc):

    filepath = Path(saveloc)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    pddf.to_csv(filepath)
didntprint=[]
fuckedup= {}

# for i in range (2,11):
#     try:
#         newcluster= plotter(i)
#         save_dftocsv(newcluster, f'deleteme {lookupname[i]}.csv')
#     except RecursionError:
#         didntprint.append(lookupname[i])
#         continue
#     except ValueError as inf:
#         fuckedup[(lookupname[i])]=inf
#         continue

newcluster= plotter(5)
# save_dftocsv(newcluster, f'deleteme {lookupname[5]}.csv')

print(fuckedup)