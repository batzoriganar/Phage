
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import json

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

with open('data.json' , 'r') as datafile:
    data=json.load(datafile)


interaction= {'phages':[],'hosts':[] }
interactiondict={}

host_lineage={}
host_lineage_lineage={}
flat_list=[]
for i in range(len(data)):

   for host in (list(data[i]['hosts'].keys())):
       flat_list.append(host)
       host_lineage[host]= data[i]['hosts'][host] #host:lineage dictionary with additional info
       host_lineage_lineage[host] = data[i]['hosts'][host]['taxonomy_ncbi']['lineage'] #host:lineage dictionary

my_lineage_data=(list(host_lineage_lineage.values()))

# print(host_lineage_lineage)
lineage_ranks= ['superkingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species']
species_taxon_ids=list(host_lineage.keys())
with open('species of hosts.txt', 'w') as outfile:
    outfile.write((str(species_taxon_ids)))

mydf = pd.DataFrame(host_lineage_lineage, lineage_ranks)


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 2)
# print(mydf)

newdf=mydf[['562', '564','599', '631', '632']].transpose()

newdf1=mydf.transpose()
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 20)


print(newdf)
newdf1.sort_values(by=['superkingdom', 'phylum', 'class', 'order', 'family', 'genus'])

print(newdf1)

data_top = newdf1

# iterating the columns
sorted_host=[]
for row in data_top.index:
    sorted_host.append(row)
# exploded_df=(pd.DataFrame(data).explode('hosts'))

print(data_top)
#
# from pathlib import Path
# filepath = Path('outphylo.csv')
# filepath.parent.mkdir(parents=True, exist_ok=True)
# data_top.to_csv(filepath)

# print(exploded_df)
# df_subset = exploded_df
# # print(df_subset)
#
# binary_matrix = pd.crosstab(df_subset['name'], df_subset['hosts'])

# print(binary_matrix)
# # Sort the rows and columns for better visualization
# binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)
#
# binary_matrix=binary_matrix.transpose().reindex(sorted_host)
#
# cmap = sns.cm.rocket_r
# sns.clustermap( data= binary_matrix,
#                     cmap=cmap, method='single')