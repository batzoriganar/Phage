import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path

'''I already have the clustered json file. there are some groups which can be allocated together.'''

with open('ClusteredCorrect.json', 'r') as datafile:
    clusters = json.load(datafile)

# print(clusters)

# namelist=[]
#
# namelist = list(zip(list(lookupname.keys()), list(lookupname.values())))
#
# # print(namelist)
#
# print(clusters)
# # clusters.or(key)
# # for key, value in clusters.items():
#
###Manual concatonation

clusters['seawater'].extend(clusters['_sea_'])
del (clusters['_sea_'])
clusters['seawater'].extend(clusters['iron chloride ppt'])
del (clusters['iron chloride ppt'])
clusters['sewage'].extend(clusters['wastewater'])
del (clusters['wastewater'])
clusters['sewage'].extend(clusters['municipal sewage'])
del (clusters['municipal sewage'])


#Sorting the water cluster

member6good= clusters

sealist=[]
wasterlist=[]
drain=[]
others=[]
for id in (member6good["_water_"]):
    if "sea" in (id[-1]):
        sealist.append(id)
    elif "waste" in (id[-1]):
        wasterlist.append(id)
    elif "drain" in (id[-1]):
        wasterlist.append(id)
    elif "sewage" in id[-1]:
        wasterlist.append(id)
    else:
        others.append(id)
print(len(member6good["_water_"]))
print(len(sealist))
print(len(wasterlist))
print(len(others))

print(member6good.keys())
print(len(member6good['seawater']))
member6good['seawater'].extend(sealist)
print(len(member6good['seawater']))

print(len(member6good['sewage']))
member6good['sewage'].extend(wasterlist)
print(len(member6good['sewage']))

# clusters_json = json.dumps(clusters, indent=2)
# with open('ClusteredCorrectPooled.json' , 'w') as datafile:
#     datafile.write(clusters_json)
#

print(member6good.keys()
      )