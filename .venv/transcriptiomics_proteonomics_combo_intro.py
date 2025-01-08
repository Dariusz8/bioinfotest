#chap 5 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-7-2025
#Last mod: 1-7-2025

import pandas as pd
from scipy.stats import spearmanr

#load transcriptomics data
transcriptomics_data = pd.read_csv('transcriptomics.csv',index_col=0)

#load the proteomics_data
proteomics_data = pd.read_csv('proteomics.csv',index_col=0)

#align dataset on the common gene column
combined_data = pd.merge(transcriptomics_data,proteomics_data,on='Gene')

#calculate the spearman correlation
correlation_results = combined_data.apply(lambda row:spearmanr((row['Transcript_Abundance'],row['Protein_Abundance']),axis=1))

#add corelation results to the combined dataframe
combined_data['Correlation'],combined_data['P-value']=zip(*correlation_results)

#id significant correlations
significant_correlations = combined_data[combined_data['P-value']<0.05]
print(significant_correlations[['Gene','Correlation','P-value']])