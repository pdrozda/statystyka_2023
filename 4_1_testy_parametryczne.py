import numpy as np
import scipy.stats as scs

dane_wzrost = np.loadtxt('dane/Wzrost.csv', delimiter=',')
dane_wzrost2 = np.loadtxt('dane/Wzrost2.csv', delimiter=',')

# Test dla jednej średniej
print('Srednia z proby:', dane_wzrost.mean())
test_jedna_proba = scs.ttest_1samp(dane_wzrost, 176)
print('Test dla jednej średniej:', test_jedna_proba)
# Jeśli pvalue jest mniejsze od zakładanego poziomu istotności to odrzucamy H0 na korzyść H1
# jeśli pvalue jest większe od zakładanego poziomu istotności to przyjmujemy H0
print('Srednia z proby 2:', dane_wzrost2.mean())
test_jedna_proba2 = scs.ttest_1samp(dane_wzrost2, 176)
print('Test dla jednej średniej:', test_jedna_proba2)

# Test dla dwóch średnich - próby niezależne
print('Srednia z proby 1:', dane_wzrost.mean())
print('Srednia z proby 2:', dane_wzrost2.mean())
test_dwie_proby_niezalezne = scs.ttest_ind(dane_wzrost, dane_wzrost2)
print('Test dla dwóch średnich, próby niezależne:', test_dwie_proby_niezalezne)

# Test dla dwóch średnich - próby zależne
test_dwie_proby_zalezne = scs.ttest_rel(dane_wzrost, dane_wzrost2)
print('Test dla dwóch średnich, próby zależne:', test_dwie_proby_zalezne)