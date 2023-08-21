import pandas as pd
from matplotlib import pyplot as plt
import json
import numpy as np
jsondata=dict()
with open('data.json' , 'r') as datafile:
    jsondata=json.load(datafile)
#
# counterlist=[]
# interactiondict={}
# for i in range(len(jsondata)):
#     counterlist.append(len(jsondata[i]['hosts']))
#     if len(jsondata[i]['hosts'])==7:
#         print (f'7 interecationtoi sda: {jsondata[i]["name"]}')
# a=[]
# b=[]
#
#
# for i in range (max(counterlist)+1):
#     a.append(i)
#     # print(f'{counterlist.count(i)} phages have {i} host(s)')
#     b.append(counterlist.count(i))
# a.pop(0)
# b.pop(0)
#
# print(a,b)
# # print(sum(b[1:-1]))
# XX = pd.Series(b,index=a)
# fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,
#                          figsize=(6 ,7))
# ax1.spines['bottom'].set_visible(False)
# ax1.tick_params(axis='x',which='both',bottom=False)
# ax2.spines['top'].set_visible(False)
# ax2.set_ylim(0,500)
# ax1.set_ylim(10000,15001)
# ax1.set_yticks(np.arange(10000,15001,1000))
# XX.plot(ax=ax1,kind='bar'
#         )
# XX.plot(ax=ax2,kind='bar')
# for tick in ax2.get_xticklabels():
#     tick.set_rotation(0)
# d = .015
# kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
# ax1.plot((-d, +d), (-d, +d), **kwargs)
# ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
# kwargs.update(transform=ax2.transAxes)
# ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
#
# ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
#
# # giving X and Y labels
# plt.xlabel("Host Range")
# plt.ylabel("Number of Phages")
#
#
# plt.show()
#
# plt.savefig('HostRange.png')
#



#####
#network plot
##############

interaction= {'phages':[],'hosts':[] }


interactiondict={}

for i in range(len(jsondata)):
    interactiondict[jsondata[i]['name']]=list(jsondata[i]['hosts'].keys())
    interaction['phages'].append(jsondata[i]['name'])
    interaction['hosts'].append(list(jsondata[i]['hosts'].keys()))
df=pd.DataFrame(interaction)
df_exploded = df.explode('hosts')



import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'df_exploded' with columns 'phages' and 'hosts'
# 'df_exploded' is the DataFrame obtained after using the 'explode' method

# # Create a NetworkX graph
# G = nx.Graph()
#
# # Add nodes for phages and hosts
# G.add_nodes_from(df_exploded['phages'], node_color='blue', node_size=100, label='phage')
# G.add_nodes_from(df_exploded['hosts'], node_color='red', node_size=100, label='host')
#
# # Add edges for interactions (connections between phages and hosts)
# edges = [(phage, host) for phage, host in zip(df_exploded['phages'], df_exploded['hosts'])]
# G.add_edges_from(edges)
#
# # Set up the plot
# plt.figure(figsize=(10, 8))
# pos = nx.spring_layout(G, seed=42)  # You can use other layout algorithms as well
#
# # Draw the network graph
# nx.draw(G, pos, with_labels=False, node_color='blue', node_size=100, font_size=8, font_color='white', edge_color='gray')
#
# # Customize the plot appearance (optional)
# plt.title("Phage-Host Interaction Network")
# # plt.legend(title='Node Type', labels=['Phage', 'Host'])
# plt.axis('off')
#
# # Show the plot
# plt.show()

# Assuming you have a DataFrame named 'df_exploded' with columns 'phages' and 'hosts'
# 'df_exploded' is the DataFrame obtained after using the 'explode' method
print(df_exploded
      )
# Create a binary matrix
binary_matrix = pd.crosstab(df_exploded['phages'], df_exploded['hosts'])

# Sort the rows and columns for better visualization
binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)

print(binary_matrix)
# Plot the binary matrix as a heatmap
plt.figure(figsize=(10, 8))
plt.imshow(binary_matrix, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Set the x and y-axis ticks and labels
plt.xticks(np.arange(len(binary_matrix.columns)), binary_matrix.columns, rotation=90)
plt.yticks(np.arange(len(binary_matrix.index)), binary_matrix.index)

# Set the plot title and axis labels
plt.title('Phage-Host Interaction Matrix')
plt.xlabel('Hosts')
plt.ylabel('Phages')

# Show the colorbar
plt.colorbar()

# Show the plot
plt.show()