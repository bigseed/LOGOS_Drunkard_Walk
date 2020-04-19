import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def norm(x):
    return k*np.exp(-x**2/(2*a**2))/(np.sqrt(2*np.pi)*a)


k = 55000
a = 38

x = np.linspace(1, 200, 400)

s = 0
density = list()

for i in x:
    s += norm(i)
    density.append(s/i)


fig, ax = plt.subplots()
plt.plot(x, density, label="Density")
plt.legend(loc='upper left')
plt.ylim(0, 1200)
plt.title('Line Experiment : Norm Density')
plt.savefig('result5.png')
