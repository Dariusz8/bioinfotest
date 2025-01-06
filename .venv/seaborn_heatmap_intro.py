#chap 4 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-5-2025
#Last mod: 1-5-2025

import seaborn as sns
import pandas as pd

#load gene expression data into pandas dataframe
expression_data = pd.read_csv("gene_expression.csv",index_col=0)

#create heatmap to visualize data
sns.heatmap(expression_data,cmap='YlGnBu',linewidths=.5)
sns.plt.title('Gene expression Heatmap')
sns.plt.xlabel('Sample')
sns.plt.ylabel('Gene')
sns.plt.show()