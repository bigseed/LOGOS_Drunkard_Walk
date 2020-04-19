import numpy as np
import matplotlib.pyplot as plt


def drunken_step():
    global drunkards
    drunkards += np.random.choice([-1, 0, 1], n, p=[1/3, 1/3, 1/3])


n = 40000
time = 1000

drunkards = np.zeros(n, dtype=np.float32)

for _ in range(time):
    drunken_step()


distance = sorted(np.abs(drunkards))
density = list()
sample = np.linspace(0.5, 150, 300)

for length in sample:
    if distance[-1] < length:
        density.append(n/length)
        continue
    for i, dis in enumerate(distance):
        if dis > length:
            dense = i / length
            density.append(dense)
            break


fig, ax = plt.subplots()
plt.ylim(0, 1500)
plt.plot(np.linspace(0.5, 150, len(density)), density, label="Density")
plt.legend(loc='upper left')
plt.title('Line Experiment : Walking Density')
plt.savefig('result6.png')
