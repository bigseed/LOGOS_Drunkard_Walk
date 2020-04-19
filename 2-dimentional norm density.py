import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

isChecked = np.zeros((150, 150))
norm = np.zeros((150, 150))


x = np.linspace(0, 150, 151)
y = stats.norm(0, 38).pdf(x)*55000
std = stats.norm(0, 38).pdf(0)*55000

for i in range(150):
    for j in range(150):
        norm[i][j] = y[i] * y[j] / std

dis = np.linspace(0.5, 150, 300)
s = 0
density = list()

for distance in dis:
    for i in range(150):
        for j in range(1, 150):
            if isChecked[i][j]:
                continue

            d = np.sqrt(i**2 + j**2)
            if d < distance:
                isChecked[i][j] = 1
                s += norm[i][j]

    density.append((4*s + norm[0][0])/(np.pi*distance**2))

fig, ax = plt.subplots()
plt.plot(np.linspace(0.5, 150, len(density)), density, label='Density')
plt.legend(loc='upper left')
plt.title('Plane Experiment : Norm Density')
plt.savefig('result8.png')
