import pandas as pd
import scipy.stats as scs
import numpy as np
import seaborn
import matplotlib.pyplot as plt


dane_mozgowe = pd.read_csv('files/brain_size.csv', sep=';')
print(dane_mozgowe.head())
wspolczynnik_pearson = scs.pearsonr(dane_mozgowe['VIQ'], dane_mozgowe['PIQ'])
print('Współczynnik korelacji liniowej Pearsona dla PIQ i VIQ', wspolczynnik_pearson)
wspolczynnik_pearson = scs.pearsonr(dane_mozgowe['Weight'], dane_mozgowe['Height'])
print('Współczynnik korelacji liniowej Pearsona dla Weight i Height', wspolczynnik_pearson)
wspolczynnik_spearman = scs.spearmanr(dane_mozgowe['Weight'], dane_mozgowe['Height'])
print('Współczynnik korelacji liniowej Spearmana dla Weight i Height', wspolczynnik_spearman)

wspolczynnik_pearson, pvalue = scs.pearsonr(dane_mozgowe['PIQ'], dane_mozgowe['Height'])
print('Współczynnik korelacji liniowej Pearsona dla PIQ i Height', wspolczynnik_pearson.round(2))
print('Wartość prawdopodobieństwa dla testu istotności współczynnika korelacji Pearsona'
      ' wynosi:', pvalue.round(2))
macierz = [dane_mozgowe['PIQ'],dane_mozgowe['VIQ'],dane_mozgowe['FSIQ'],
           dane_mozgowe['Weight'], dane_mozgowe['Height']]
macierz_korelacji_np = np.corrcoef(macierz).round(2)
print(macierz_korelacji_np)

macierz_df = dane_mozgowe[['PIQ','VIQ','FSIQ','Weight','Height']]
macierz_korelacji_df = macierz_df.corr().round(2)
print(macierz_korelacji_df)
seaborn.heatmap(macierz_korelacji_df, annot=True,cmap="jet" )
plt.show()