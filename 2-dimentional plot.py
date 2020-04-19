import numpy as np
import matplotlib.pyplot as plt


def drunken_step():
    global drunkards
    for person in drunkards:
        person += np.random.choice([-1, 0, 1], n, p=[1/3, 1/3, 1/3])


def calc_standard_deviation():
    distance = list()
    for person in drunkards.T:
        distance.append(np.sqrt(person[0]**2 + person[1]**2))

    mean = sum(distance) / n
    standard_deviation = 0
    for length in distance:
        standard_deviation += (length - mean)**2

    return np.sqrt(standard_deviation / n)


def radius():
    distance = list()
    for person in drunkards.T:
        distance.append(np.sqrt(person[0]**2 + person[1]**2))

    return sorted(distance)[n*99 // 100]


n = 120000
time = 2000

drunkards = np.zeros((2, n), dtype=np.float32)

for _ in range(time):
    drunken_step()

fig, ax = plt.subplots()
plt.scatter(drunkards[0], drunkards[1], s=1)
circle = plt.Circle((0, 0), radius(), fill=False,
                    ec='r', lw=3, label='99% border')
ax.add_patch(circle)
plt.legend(loc='upper left')
ax.set_aspect('equal')
plt.title('Plane Experiment')
plt.savefig('result2.png')
