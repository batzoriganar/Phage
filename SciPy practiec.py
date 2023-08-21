##FIRST DEFINE Bacterial interest group
##CLuster heatmap interaction

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import json

Data=pd.read_json('Data_exploded.json')

# Data.rename(columns={'index': 'index_original'}, inplace=True)
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# print(Data)

print(Data)
# Data.to_json('Data_exploded.json')