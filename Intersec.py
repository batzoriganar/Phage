from Clustered_heatmap import hostsourcename,hostsource

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path
import sys
sys.setrecursionlimit(100000)
with open('host_taxid_name.json', 'r') as infile:
    taxlookup= json.load(infile)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

def find_list_intersections(input_dict):
    intersection_dict = {}

    keys = list(input_dict.keys())
    num_keys = len(keys)

    for i in range(num_keys):
        for j in range(i + 1, num_keys):
            key1 = keys[i]
            key2 = keys[j]
            list1 = input_dict[key1]
            list2 = input_dict[key2]
            intersection = list(set(list1) & set(list2))
            intersection_key = f"{key1}/{key2}"
            intersection_dict[intersection_key] = intersection

    return intersection_dict

print(hostsource.keys())
d = 'Sewage'
a = (hostsource[d])
b = (hostsourcename[d])

for i in range(len(a)):
    print(a[i])
    print(b [i])
    print(taxlookup[a[i]])
## Finding the common hosts in 2 of each sources
print(find_list_intersections(hostsource))

for i,vals in find_list_intersections(hostsourcename).items():
    print(i, vals)
data = find_list_intersections(hostsourcename)
dataid = find_list_intersections(hostsource)
df = pd.DataFrame(data.items(), columns=['category', 'strains'])
df2 = pd.DataFrame(dataid.items(), columns=['Category', 'taxid'])
print(len(data) == len(dataid))
dfe = (df.explode('strains'))
dfe2 = df2.explode('taxid')
newdf = pd.concat([dfe,dfe2], axis=1,ignore_index=True)

print("!!!this newdf!!!")
print(dfe)

### one time arrangement correction of the ID in csv.
with open('host_taxid_name.json', 'r') as infile:
    taxlookup= json.load(infile)

def swap_keys_values(dictionary):
    swapped_dict = {value: key for key, value in dictionary.items()}
    return swapped_dict
taxlookup = swap_keys_values(taxlookup)
taxidcolumn=[]
for i in dfe['strains']:
    taxidcolumn.append(taxlookup[i])
dfe['taxid'] = taxidcolumn

s1=[]
s2=[]
for i in dfe['category']:
    templist=(i.split('/'))
    s1.append(templist[0])
    s2.append(templist[1])
dfe['source1'] = s1
dfe['source2'] = s2
print(dfe)

dfe.to_csv('isolsourcehost.csv')