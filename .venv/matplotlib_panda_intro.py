#chap 2 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-2-2025
#Last mod: 1-2-2025

import matplotlib.pyplot as plt
import pandas as pd

#load gene expression data from CSV file into Pandas DataFrame
expression_data = pd.read_csv('gene_expression.csv')

#plot a bar chart showing expression levels of various genes
plt.figure(figsize=(10,6))
plt.bar(expression_data['Gene'])
plt.xlabel('Gene')
plt.ylabel('Expression Level')
plt.title('Gene Expression Levels')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
