import numpy as np
import scipy.stats as scs

dane_wzrost1 = np.loadtxt('dane/Wzrost.csv', delimiter=',')
dane_wzrost2 = np.loadtxt('dane/Wzrost2.csv', delimiter=',')
dane_wzrost3 = np.loadtxt('dane/Wzrost1.csv', delimiter=',')

# testy normalności
normalnosc_1 = scs.normaltest(dane_wzrost1)
normalnosc_1_ks = scs.kstest(dane_wzrost1, 'norm')
normalnosc_2 = scs.normaltest(dane_wzrost2)
normalnosc_2_ks = scs.kstest(dane_wzrost2, 'norm')
normalnosc_3 = scs.normaltest(dane_wzrost3)
normalnosc_3_ks = scs.kstest(dane_wzrost3, 'norm')
print('Normalność wzrost 1', normalnosc_1)
print('Normalność wzrost 1 ks', normalnosc_1_ks)
print('Normalność wzrost 2', normalnosc_2)
print('Normalność wzrost 2 ks', normalnosc_2_ks)
print('Normalność wzrost 3', normalnosc_3)
print('Normalność wzrost 3 ks', normalnosc_3_ks)

# testy równości wariancji - Bartletta oraz Levene
bartlett_test = scs.bartlett(dane_wzrost1,  dane_wzrost3)
levene_test = scs.levene(dane_wzrost1,  dane_wzrost3)
print('Równość wariancji dla 1 i 3 grup wzrostu, test bartletta:', bartlett_test)
print('Równość wariancji dla 1 i 3 grup wzrostu, test levene:', levene_test)
bartlett_test = scs.bartlett(dane_wzrost1, dane_wzrost2,  dane_wzrost3)
levene_test = scs.levene(dane_wzrost1, dane_wzrost2,  dane_wzrost3)
print('Równość wariancji dla 1, 2 i 3 grup wzrostu, test bartletta:', bartlett_test)
print('Równość wariancji dla 1, 2 i 3 grup wzrostu, test levene:', levene_test)