import numpy as np
import matplotlib.pyplot as plt


def drunken_step():
    global drunkards
    drunkards[0] += np.random.choice([-1, 0, 1], n, p=[1/3, 1/3, 1/3])
    drunkards[1] += np.random.choice([-1, 0, 1], n, p=[1/3, 1/3, 1/3])


def calc_distance():
    distance = list()
    for person in drunkards.T:
        distance.append(np.sqrt(person[0]**2 + person[1]**2))

    return sorted(distance)


n = 100000
time = 2000

drunkards = np.zeros((3, n), dtype=np.float32)

for _ in range(time):
    drunken_step()


distance = calc_distance()
density = list()
sample = np.linspace(1, 150, 298)

for length in sample:
    if distance[-1] < length:
        density.append(n/(np.pi * length**2))
        continue
    for i, dis in enumerate(distance):
        if dis > length:
            dense = i / (np.pi * length**2)
            density.append(dense)
            break


fig, ax = plt.subplots()
plt.plot(sample, density, label="Density")
plt.ylim(0, 17)
plt.legend(loc='upper left')
plt.title('Plane Experiment : Walking Density')
plt.savefig('result7.png')
