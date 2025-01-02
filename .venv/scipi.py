#Trying and looking into scipi while learning about bioinformatics
#Dariusz Czeczuk
#Start date: 11-02-2024
#Last mod: 11-02-2024

from scipy import stats

#sample gene expression data for two conditions

condition1 = [13,9,10,12,7,12]
condition2 = [5,8,7,6,6,5]

#perform a two-sample t-test

t_stat,p_value = stats.ttest_ind(condition1, condition2)
print(f"t-statistic: {t_stat}, p-value:{p_value}")