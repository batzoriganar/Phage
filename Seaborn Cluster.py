import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
Data=pd.read_json('data.json')

df_exploded = Data.explode('hosts')

print( df_exploded.hosts)

# Subsetting the data for first 200 line for faster work

df_subset= df_exploded.iloc[:500]

# print(df_subset)

binary_matrix = pd.crosstab(df_subset['name'], df_subset['hosts'])

# Sort the rows and columns for better visualization
binary_matrix = binary_matrix.sort_index(axis=0).sort_index(axis=1)

print(binary_matrix)
cmap = sns.cm.rocket_r
sns.clustermap( data= binary_matrix,
                cmap=cmap, method='ward')


# sns.set_theme()
#
# # Load an example dataset
# tips = sns.load_dataset("tips")
#
# # Create a visualization
# sns.relplot(
#     data=tips,
#     x="total_bill", y="tip", col="time",
#     hue="smoker", style="smoker", size="size",
# )
# plt.savefig("Subset ward 5000.pdf", dpi=150)
plt.show()