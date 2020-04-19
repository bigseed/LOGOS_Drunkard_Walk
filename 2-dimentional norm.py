import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm

isChecked = np.zeros((301, 301))
norm = np.zeros((301, 301))


x = np.linspace(-150, 150, 301)
y = stats.norm(0, 38).pdf(x)*55000
std = stats.norm(0, 38).pdf(0)*55000

for i in range(301):
    for j in range(301):
        norm[i][j] = y[i] * y[j] / std


X = np.arange(-150, 151, 1)
Y = np.arange(-150, 151, 1)
X, Y = np.meshgrid(X, Y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, norm, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig('result9.png')
