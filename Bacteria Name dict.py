
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

df= Data[["hosts"]]

df_exploded = df.explode('hosts')

# print(sliced_df)
lookupdict={}
for ind in df.index:
    hostlist=df['hosts'][ind]
    for i in hostlist.keys():
        x = (i)
        y = (hostlist[i]['taxonomy_ncbi']['lineage_names'][-1])
        lookupdict[x] = y
print(lookupdict)
jsoncopy = (json.dumps(lookupdict, indent=2))
with open('host_taxid_name.json' , 'w') as datafile:
    datafile.write(jsoncopy)