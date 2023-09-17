import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path


df = pd.read_csv('isolsourcehost.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# df = (df.drop(['Unnamed: 0.1'], axis=1))



print(df)
df = df.astype(dtype=str)
a = (df.sort_values('strains'))
# help(df)
multienvironhosts = list(pd.Categorical(a["taxid"]))

print((multienvironhosts))
#

from cluster_heatmap_subset import subsetplot, save_dftocsv

s = subsetplot(multienvironhosts, 'Hosts')
plt.show()
save_dftocsv(s, "hostswithmutualsource.csv")
