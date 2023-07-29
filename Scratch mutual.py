import json
import pandas as pd
with open('data.json' , 'r') as datafile:
    data=json.load(datafile)


interaction= {'phages':[],'hosts':[] }


interactiondict={}

for i in range(len(data)):
    interactiondict[data[i]['name']]=list(data[i]['hosts'].keys())
    interaction['phages'].append(data[i]['name'])
    interaction['hosts'].append(list(data[i]['hosts'].keys()))


phages_with_multiple_hosts = []
for phage_id, phage_info in interactiondict.items():
    # print(len(phage_info))
    if len(phage_info) > 1:
        phages_with_multiple_hosts.append(phage_id)
# print((phages_with_multiple_hosts))
# print(f'keys{interactiondict.items()}')
# Printing the results
print("Phages with Multiple Hosts:")
print(len(phages_with_multiple_hosts))
print('****************')
df=pd.DataFrame(interaction)
# print(df)

# adf=df.sort_values('hosts')
# print((adf['hosts']))
counter=0
host_to_phage=dict()


dfexpanded = df.explode('hosts')

df2 = dfexpanded.sort_values('hosts')
list_of_hosts = pd.unique(df2['hosts'])
# print(type(list_of_hosts))

# for i in range(10):
#     hosttemp = (list_of_hosts[i])
countdf=(dfexpanded['hosts'].value_counts())
hosts_with_multiple_phages=(countdf.loc[countdf > 0].index.tolist())

print('Hosts with multiple Phages:')
print(len((hosts_with_multiple_phages)))
print('**************')
my_new_dict=dict()
for i in range(len(hosts_with_multiple_phages)):
    queryhost = (hosts_with_multiple_phages[i])

    matched_phages = ( (dfexpanded[dfexpanded['hosts'] == queryhost]['phages']))
    my_new_dict[queryhost] = matched_phages

# print((my_new_dict))
# print (hosts_with_multiple_phages)
# print((dfexpanded['hosts']))
# print(dfexpanded['phages'])
#
counter_dict={}
for i in my_new_dict:
    print(f'The host {i} has {len(my_new_dict[i])} phage interactions')

    # if (len(my_new_dict[i]) in list(counter_dict.keys())) is False:
    #     counter_dict[my_new_dict[i]] = 1
    # elif len(my_new_dict[i]) in list(counter_dict.keys()):
    #     counter_dict[my_new_dict[i]] = +1
def host_info():
    return list(my_new_dict.keys())

def phage_count():
    list=[]
    for i in my_new_dict:
        list.append(len(my_new_dict[i]))
    return list
# print(host_info())

for i in phage_count():
    # print(i)
    # print()
    counter_dict[i]=phage_count().count(i)


import numpy as np
import matplotlib.pyplot as plt

# counter_dict=reversed(counter_dict)
print(counter_dict)
# plt.bar(counter_dict.keys(), counter_dict.values())
# plt.show()
# plt.savefig("graph.pdf")
# from matplotlib import pyplot as plt
# plt.bar(host_info()[0:100],phage_count()[0:100])
# # fig.bar(host_info()[0:100],phage_count()[0:100])
# plt.show()

# for i in range(10):
#     host_id=host_info()[i]
#     print ()
#
#
# print([phages_with_multiple_hosts]
#       )
'''*i know the phages with more than 1 host
* I also identified the hosts with more than 1 phages and the phage IDs
'''
