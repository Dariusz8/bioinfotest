#Trying and looking into pandas while learning about bioinformatics
#Dariusz Czeczuk
#Start date: 11-02-2024
#Last mod: 11-02-2024

import pandas as pd
from sklearn.decomposition import PCA

#load gene expression data from CSV file

gene_expression_df = pd.read_csv('gene_expression.csv')
print(gene_expression_df.head())

#normalizing gene expression levels using simple scaling factor

scaling_factor = gene_expression_df.sum(axis = 0)
normalized_df = gene_expression_df/scaling_factor
print(normalized_df.head())

pca = PCA(n_components = 2)
principal_components = pca.fit_transform(normalized_df)
principal_df= pd.DataFrame(data=principal_components, columns=['PC1','PC2'])
print(principal_df.head())

