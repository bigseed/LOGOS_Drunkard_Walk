import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def drunken_step():
    global drunkards
    drunkards += np.random.choice([-1, 0, 1], n, p=[1/3, 1/3, 1/3])


n = 50000
time = 2000

drunkards = np.zeros(n, dtype=np.float32)

for _ in range(time):
    drunken_step()

pts = np.zeros(400)
for x in drunkards:
    x = x.astype('int')
    pts[x+200] += 1

x = np.linspace(-200, 200, 800)
y = stats.norm(0, 38).pdf(x)*55000

fig, ax = plt.subplots()
plt.plot(range(-200, 200), pts, linewidth=2, label='Spreads of points')
plt.plot(x, y, linewidth=2, label='Normal Distribution')
plt.title('Relationship with Normal Distribution')
plt.legend(loc='upper left')
plt.savefig('result4.png')
