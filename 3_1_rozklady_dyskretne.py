import scipy.stats as scs
import matplotlib.pyplot as plt
import numpy as np

p = 0.6
size = 1300
n = 20
k = 12

# rozkład Bernoulliego - jeden eksperyment sukces/porazka, ze zdefiniowanym prawdopodobieństwem sukcesu p
dane_bernoulli = scs.bernoulli.rvs(p, size=size)
#print("Wygenerowane dane:", dane_bernoulli)
statystyki = scs.describe(dane_bernoulli)
print("parametry wygenerowanych danych dla rozkładu Bernoulliego:", statystyki[2], statystyki[3], statystyki[4], statystyki[5])
srednia, wariancja, skosnosc, kurtoza = scs.bernoulli.stats(p, moments='mvsk')
print("parametry dla teoretycznego rozkładu", srednia, wariancja, skosnosc, kurtoza)

# rozkład dwumianowy - prawdopodobieństwo k sukcesów w n próbach, ze zdefiniowanym prawdopodobieństwem sukcesu p

p_binom = scs.binom.rvs(n, p, size=10)
print(p_binom)

suma_p = 0
for k in range(0, n+1):
    p_k_n_binom = scs.binom.pmf(k, n, p)
    print('Prawdopodobieństwo ',k,' sukcesow w ',n,' probach', p_k_n_binom)
    suma_p = suma_p + p_k_n_binom
    print(suma_p)

# rozkład Poissona - wygenerowanie wykresu
mu = 2
x = np.arange(scs.poisson.ppf(0.0001, mu), scs.poisson.ppf(0.9999, mu))
rv = scs.poisson(mu)
fig, ax = plt.subplots(1, 1)
ax.vlines(x, 0, rv.pmf(x), colors='r', linestyles='-', lw = 6)
plt.show()

