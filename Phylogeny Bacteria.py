import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import json
import re

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
       lineage_no =  data[i]['hosts'][host]['taxonomy_ncbi']['lineage']
       lineage_names = data[i]['hosts'][host]['taxonomy_ncbi']['lineage_names']
       host_lineage_lineage[host] =  list(zip(lineage_no, lineage_names))#host:lineage dictionary

my_lineage_data=(list(host_lineage_lineage.values()))
# print(my_lineage_data)
newlist1=[]
for i in range(len(my_lineage_data)):
    # print(i)
    newlist1.append([])
    for x in range(len(my_lineage_data[i])):
        # newlist1[i].append()
        id=my_lineage_data[i][x][0]
        nm=my_lineage_data[i][x][1]
        newstr = re.sub("[{}()]", "", str(nm))
        # newlist1[i][x] = f"{id}/{nm}"
        newlist1[i].append(f"{id}/{newstr}")
print(newlist1)
    # for x in my_lineage_data[i]:
    #     print(x)
def build_hierarchy(hierarchy, lineage):
    current_level = hierarchy
    for taxon_id in lineage:
        if taxon_id is not None:
            current_level = current_level.setdefault(taxon_id, {})
    return hierarchy

hierarchical_data = {}

lineage_lists= newlist1
# Build hierarchical JSON for each lineage
for lineage in lineage_lists:
    hierarchical_data = build_hierarchy(hierarchical_data, lineage)

# Print the hierarchical JSON
import json
# hierarchyjson=(json.dumps(hierarchical_data, indent=2))
#
print(hierarchical_data)
# with open('host_tree.json' , 'w') as datafile:
#     datafile.write(hierarchyjson)

# import pickle
# with open('Host tree.pkl', 'wb') as fp:
#     pickle.dump(hierarchical_data, fp)
#     print('dictionary saved successfully to file')
# depth=0

##############################################
### CURRENTLY ONLY WORKS WITH NO HIERARCHY####
##############################################
def generate_newick(node, parent_name=None):
    newick = ""
    if parent_name:
        newick += f"{parent_name},"

    if node:
        child_taxa = []
        for child_name, child_node in node.items():
            child_taxa.append(generate_newick(child_node, parent_name=child_name))
        newick += f"({''.join(child_taxa)},)"

    return newick
#
root_taxon = '2/Bacteria'  # Root taxon
#
newick_tree = generate_newick(hierarchical_data[root_taxon])
newick_tree += ";"

# print(newick_tree)

#Uncomment when saving text
with open('my_nwk_txt2.txt' ,'w') as outfile:
    outfile.write(newick_tree)
# print(hierarchical_data)
