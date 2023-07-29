import json
import pandas as pd
with open('processed_phage_data.json' , 'r') as datafile:
    data=json.load(datafile)

text=f'Total phages with annotated isolation source: {len(data)} \n'
for i in data:
    text = text + str(i) +' '+ str(data[i]['isolation_source'])
    text += '\n'
with open('isolation source.txt', 'w') as f:
    f.write(text)
print(len(data))