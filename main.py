

# fnadata=''
# with open('data.fna' , 'r') as datafile:
#     fnadata=datafile.read()
# print(len(fnadata.split('>')))

# gbffdata=''
# with open('data.gbff' , 'r') as datafile:
#     print(type(datafile.read()))

import json
import pandas as pd
from matplotlib import pyplot as plt





jsondata=dict()
with open('data.json' , 'r') as datafile:
    jsondata=json.load(datafile)
# print((jsondata[0].keys()))

interaction=dict()
# df = pd.read_json(jsondata)
for i in range(len(jsondata)):
    interaction[(jsondata[i]['name'])]=(list(jsondata[i]['hosts'].keys()))

print(
    interaction)


# df = pd.DataFrame(interaction)


# print(df.info)
counterlist=[]
for i in range(len(jsondata)):
    counterlist.append(len(jsondata[i]['hosts']))
a=[]
b=[]


for i in range (max(counterlist)+1):
    a.append(i)
    # print(f'{counterlist.count(i)} phages have {i} host(s)')
    b.append(counterlist.count(i))


