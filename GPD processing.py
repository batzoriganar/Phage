# Simple Way to Read TSV Files in Python using pandas
# importing pandas library

##########################################
# GutPhageDB has phage info as Assemblies# #STUB
##########################################


import pandas as pd
import json
# Passing the TSV file to
# read_csv() function
# with tab separator
# This function will
# read data from file
with open('data.json' , 'r') as datafile:
    data=json.load(datafile)


interaction= {'phages':[],'hosts':[] }


interactiondict={}

for i in range(len(data)):
    interactiondict[data[i]['name']]=list(data[i]['assemblies'].keys())
    interaction['phages'].append(data[i]['name'])
    interaction['hosts'].append(list(data[i]['hosts'].keys()))

df = pd.read_csv('GPD_metadata.tsv', sep='\t')

# printing data
PredictedAssemblies=(df[~df['Predicted_phage_taxon'].isna()]['Host_range_isolates'])

PhdailyData = [item for sublist in interactiondict.values() for item in sublist]



# print(PredictedAssemblies)
# print(df.info())
PredAss= str(PredictedAssemblies)
#
# for i in range(len(PredAss)):
#     print(PredAss[i])


for item in PhdailyData:
    if item in PredAss:
        print(item)
    else:
        print(item
              )