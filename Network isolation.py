from cluster_heatmap_subset import subsetplot, save_dftocsv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import json
import numpy as np
from pathlib import Path
import sys
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 10000)

sys.setrecursionlimit(100000)

def random_phage_sample(df,rowcount=5):
    df1 = df.sample(rowcount)
    zero_cols = df1.columns[(df1 == "0").all()]
    df1.drop(labels=zero_cols, axis=1, inplace=True)

    print("Sampled binary matrix:")
    print(df1)
    # print(len(df1))
    # print(['!!!this is df1'])
    # print(df1)
    lst = list(df1.species_taxid)
    print(lst)
    return lst
def random_host_sample(df,rowcount=50):
    "returns hosts of randodmly selected 5 phages from the binary df"


    df1 = df.sample(rowcount)
    zero_cols = df1.columns[(df1 == "0").all()]
    df1.drop(labels=zero_cols, axis=1, inplace=True)

    print("Sampled binary matrix:")
    print(df1)
    # print(len(df1))
    # print(['!!!this is df1'])
    # print(df1)
    lst = list(df1.columns[4:])
    print(lst)
    # lst = list(df1.species_taxid)
    return lst


def open_file():
    '''A dialog to select a CSV file that defines the filepath for other functions to parse'''
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.csv'), ('All Files', '*.*')])
    if not filepath:
        return
    return filepath
###Calling thhe plotters
# hostcladeplot(random_phage_sample(df), 'phage','randomsamplephage')
# hostcladeplot(random_host_sample(df,rowcount=2), 'host','randomsamplehost')

def binarydftolist(typeoflist):
    """The function calls open_file which asks user to select a binary matrix.
    It returns the the taxids in that binary matrix, of the type specified: phage or host."""
    filepath =  open_file()
    df = pd.read_csv(filepath)
    if typeoflist == 'host':
        taxidlist= df.columns[4:]
    elif typeoflist == 'phage':
        taxidlist = df['species_taxid'][1:].astype('Int64').astype('str')

    return list(taxidlist)

# (help(open_file))
hostorphage='phage'
# subset = ''
# print(subset)
# s = subsetplot(subset=binarydftolist(hostorphage), typeoflist=hostorphage, title='insects', saveplot=False)
# #
# print(s)
#
# save_dftocsv(s, saveloc='Plot_and_csv/insectsamplehost.csv')
# # lst =['562', '28901', '470', '821', '1772']
# # # # # def custom_sample(df,lst):
# # # #
phagelist = ['2844134','10689','2844131','10710','10702','2169700']
s = subsetplot(subset=phagelist, typeoflist='phage', title='manualsample', saveplot="Plot_and_csv/manual.pdf")
print(s)
save_dftocsv(s, 'Plot_and_csv/manual.csv')