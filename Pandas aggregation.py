##FIRST DEFINE Bacterial interest group
##CLuster heatmap interaction

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import json

with open('hierarchy_host.json' , 'r') as datafile:
    data=json.load(datafile)

Data=pd.read_json('data.json')

df_exploded = Data.explode('hosts')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
df_host= Data['hosts'].apply(pd.Series)
# print(Data)

# filt = df['hosts'].str.contains('Python', na=False)
def binary_matrix(host_id):
    Data = pd.read_json('data.json')

    df_exploded = Data.explode('hosts')
    host_group = (df_exploded.groupby(['hosts']))
    df_subset = (host_group.get_group(str(host_id)))
    print(df_subset.columns)
    # print(f'{len(df_subset)} MATCHES FOUND')
    binary_matrix = pd.crosstab(df_subset['name'], df_subset['hosts'])
    #
    # binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)
    return binary_matrix

def plotter(subset):


    condition = df_exploded['hosts'].isin(subset)

    filtered_df = df_exploded[condition]
    # whatever_df = df_exploded['species_taxid'].symmetric_difference(soilID)

    print(filtered_df)


    ############
    # Plotting #
    ############

    df_subset= filtered_df.iloc[:150]
    # print(df_subset)

    binary_matrix = pd.crosstab(df_subset['name'],df_subset['hosts'])

    # Sort the rows and columns for better visualization
    # binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)


    cmap = sns.cm.rocket_r
    sns.clustermap( data= binary_matrix,
                    cmap=cmap, method='ward')


    # plt.savefig("Subset2000 Soil cluster.pdf", dpi=150)
    plt.show()

mycosomet=(binary_matrix(1772))
plotter(mycosomet)