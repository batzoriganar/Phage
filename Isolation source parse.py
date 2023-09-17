'''
Exracting information about where the phages are isolated from
'''
import json
import pandas as pd
with open('processed_phage_data.json' , 'r') as datafile:
    data=json.load(datafile)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df_exploded= pd.read_json("Data_exploded.json")
checkexploded =list((df_exploded['species_taxid']))

# print(checkexploded.dtypes)
newlist=[]
newdict={}
counter= 0
truecounter= 0
for i in data:
    newdict[i]= data[i]['isolation_source'][0]
    if (int(i) in checkexploded)== False:
        newlist.append(i)
        counter+=1
    else:
        truecounter+=1
print(counter, truecounter)

print(newlist)
#
# # print(len(data))
# print(len(newdict))
# with open('IsolationSource.json' , 'w') as datafile:
#     datafile.write(json.dumps(newdict))