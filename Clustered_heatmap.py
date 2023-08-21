import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path
import sys
sys.setrecursionlimit(100000)

Data=pd.read_json('data.json')
df_exploded = Data.explode('hosts')

#Calling clustered dict
with open('ClusteredCorrectPooled.json', 'r') as datafile:
    clusters = json.load(datafile)




def plotter(clusterid, clustermethod='ward', subset=False):
    calledcluster=clusters[clusterid]
    clustercallID=[int(id) for id, text in calledcluster]
    condition = df_exploded['species_taxid'].isin(clustercallID)
    filtered_df = df_exploded[condition]
    ############
    # Plotting #
    ############
    #Length can be edited for subsetting the too long clusters
    df_subset= filtered_df.iloc[:len(clustercallID)]
    if subset:
        df_subset = filtered_df.iloc[:2000]
    #generate interaction matrix
    binary_matrix = pd.crosstab(df_subset['name'], df_subset['hosts'])

    # this can be put into the clustermap call to make a full plot
    ExpandPlot=((.2*(len(binary_matrix.columns))),(.2*(len(binary_matrix.index))))
    cmap = sns.cm.rocket_r
    h = sns.clustermap( data= binary_matrix,
                    cmap=cmap, method='ward')
    h.fig.suptitle(f'{(clusterid.capitalize())}')
    # plt.show()
    #Clustermap returns this Object which has the built-in calls for row/col order
    rowinfo=h.dendrogram_row.reordered_ind

    columninfo= h.dendrogram_col.reordered_ind

    # can be uncommented to save the figure
    plt.savefig(f"D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\ClustMAP\{clusterid}.pdf")

    #calling original names of the phage and host by indexing with available info
    columnlist= [binary_matrix.columns[i] for i in columninfo]
    rowlist=[binary_matrix.index[i] for i in rowinfo]

    #Rearranging the binary matrix into the order clustermap did
    newdf=binary_matrix[columnlist]
    newdf=newdf.reindex(rowlist)

    ###CLustered binary matrix is ready to be annotated
    #Extracting necessary information from the source-subsetted DF
    filtered_df['name'] = pd.Categorical(filtered_df['name'], categories=rowlist, ordered=True)

    ### rearreanging the original DF from which the binary matrix was created.
    ### to extract the original index number from the order.
    # Sort the original source-subsetted DataFrame based on the custom order
    extradf = filtered_df.sort_values('name')
    # Duplicated has to be dropped because of multiple phage entry gives different shape of DF
    extradf = extradf.drop_duplicates(subset='name')
    extradf.dropna(axis = 'index')
    extradf = (extradf.dropna(axis = 'index'))
    print(extradf)
    #Assigning taxids, source, and original index to the BINARY into CSV
    ### THIS HAS TO BE CROSS-CHECKED
    species_taxid=(list(extradf.species_taxid))

    originalindex=list( extradf.index)
    isolationsource=list()
    with open('IsolationSource.json', 'r') as datafile:
        data = json.load(datafile)

        # Extract terms from the data
        terms = list(data.values())
        ids = list(data.keys())

        # Step 1: Data Preprocessing (convert to lowercase)
        terms = [term.lower() for term in terms]
        # print(data[str(id)])
        for id in species_taxid:
            isolationsource.append(data[str(id)])
    newdf.insert(0, 'index', originalindex, True)
    newdf.insert(0, 'species_taxid',species_taxid, True)
    newdf.insert(2, 'isolation_source', isolationsource, True)
    # newdf.set_index('index')
    # print(originalindex)
    return newdf

def save_dftocsv(pddf, saveloc):

    filepath = Path(saveloc)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    pddf.to_csv(filepath)
toolong=[]
valuerror= {}

# for i in clusters:
#     try:
#         newcluster= plotter(i)
#         save_dftocsv(newcluster, f'D:\MEDICAL BIOTECHNOLOGY MSC\Internship\Phage\ClustMAP\{i}.csv')
#     except RecursionError:
#         toolong.append(i)
#         continue
#     except ValueError as inf:
#         valuerror[i]=inf
#         continue
print("toolong", toolong )
print("value error", valuerror)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 100)