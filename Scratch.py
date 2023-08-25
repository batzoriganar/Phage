import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path
Data=pd.read_csv('HostClust/data_binary.csv')
print(Data)

#
# df = (Data.iloc[15012].dropna())
# df = df[1:-1]
hostrange = Data['hostcount'].value_counts()



phagerange = Data.iloc[15012]. value_counts()

print(phagerange)

print(hostrange)

hostrange.plot.bar()
phagerange.plot.bar()
plt.show()