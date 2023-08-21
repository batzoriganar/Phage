import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import json


Data=pd.read_json('data.json')

sliced_df= Data[["name", "species_taxid", "hosts"]]

df_exploded = sliced_df.explode('hosts')

# phage_taxonomy=Data[['taxonomy_ncbi', 'taxonomy_ictv']]
phage_taxonomy=Data[["species_taxid", 'taxonomy_ncbi']]
taxadict={}

for row in range(len(phage_taxonomy)):
    taxadict[str((phage_taxonomy['species_taxid'][row]))]=phage_taxonomy['taxonomy_ncbi'][row]
my_lineage_data=[]
my_name_data=[]
print(len(taxadict))
for i in range(15011):
    info=(taxadict[str(phage_taxonomy['species_taxid'][i])])
    my_lineage_data.append(info['lineage'])
    info['lineage_names'].pop(0)
    my_name_data.append(info['lineage_names'])

# print(my_lineage_data)

def build_hierarchy(hierarchy, lineage):
    current_level = hierarchy
    for taxon_id in lineage:
        if taxon_id is not None:
            current_level = current_level.setdefault(taxon_id, {})
    return hierarchy

hierarchical_data = {}

lineage_lists= my_name_data
# Build hierarchical JSON for each lineage
for lineage in lineage_lists:
    hierarchical_data = build_hierarchy(hierarchical_data, lineage)

# Print the hierarchical JSON
import json
hierarchyjson=(json.dumps(hierarchical_data, indent=2))

with open('name_hierarchy.json' , 'w') as datafile:
    datafile.write(hierarchyjson)