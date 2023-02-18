import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs

fig, ax = plt.subplots(1,1)
x = np.linspace(scs.norm.ppf(0.001), scs.norm.ppf(0.999), 10000)
ax.plot(x, scs.norm.pdf(x), 'b-', lw=2)
rv = scs.norm(loc=0, scale=0.5)
ax.plot(x, rv.pdf(x), 'g--', lw=6)
rv = scs.norm(loc=0, scale=3)
ax.plot(x, rv.pdf(x), 'r*', lw=9)
plt.show()