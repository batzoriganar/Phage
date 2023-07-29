import pandas as pd
from matplotlib import pyplot as plt
import json
import numpy as np
jsondata=dict()
with open('data.json' , 'r') as datafile:
    jsondata=json.load(datafile)

counterlist=[]
interactiondict={}
for i in range(len(jsondata)):
    counterlist.append(len(jsondata[i]['hosts']))
    if len(jsondata[i]['hosts'])==7:
        print (f'7 interecationtoi sda: {jsondata[i]["name"]}')
a=[]
b=[]


for i in range (max(counterlist)+1):
    a.append(i)
    # print(f'{counterlist.count(i)} phages have {i} host(s)')
    b.append(counterlist.count(i))
a.pop(0)
b.pop(0)

print(a,b)
# print(sum(b[1:-1]))
XX = pd.Series(b,index=a)
fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,
                         figsize=(6 ,7))
ax1.spines['bottom'].set_visible(False)
ax1.tick_params(axis='x',which='both',bottom=False)
ax2.spines['top'].set_visible(False)
ax2.set_ylim(0,500)
ax1.set_ylim(10000,15001)
ax1.set_yticks(np.arange(10000,15001,1000))
XX.plot(ax=ax1,kind='bar'
        )
XX.plot(ax=ax2,kind='bar')
for tick in ax2.get_xticklabels():
    tick.set_rotation(0)
d = .015
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot((-d, +d), (-d, +d), **kwargs)
ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
kwargs.update(transform=ax2.transAxes)
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)

ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

# giving X and Y labels
plt.xlabel("Host Range")
plt.ylabel("Number of Phages")


plt.show()

plt.savefig('HostRange.png')




