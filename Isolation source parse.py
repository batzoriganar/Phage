################################################################
#Exracting information about where the phages are isolated from#
################################################################
import json
import pandas as pd
with open('processed_phage_data.json' , 'r') as datafile:
    data=json.load(datafile)


newdict={}
for i in data:
    newdict[i]= data[i]['isolation_source'][0]
    print(data[i])

print(len(data))

with open('IsolationSource.json' , 'w') as datafile:
    datafile.write(json.dumps(newdict))