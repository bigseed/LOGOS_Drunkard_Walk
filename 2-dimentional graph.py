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


def calc_root(coord1, coord2):
    b = np.log(coord1[1]/coord2[1]) / np.log(coord1[0]/coord2[0])
    a = coord1[1] / coord1[0]**b

    root = list(map(lambda x: a*(x**b), sample_lst))
    return root


def radius():
    distance = list()
    for person in drunkards.T:
        distance.append(np.sqrt(person[0]**2 + person[1]**2))

    return sorted(distance)[n*99 // 100]


n = 15000
sample_lst = range(10, 2501, 10)
border_radius = list()


for time in sample_lst:
    drunkards = np.zeros((2, n), dtype=np.float32)
    for _ in range(time):
        drunken_step()
    border_radius.append(radius())
    print(f'{time} / {sample_lst[-1]}')

l = len(border_radius)

fig, ax = plt.subplots()
plt.plot(sample_lst, border_radius, linewidth=4, label='Border radius')
plt.plot(sample_lst, calc_root(
    (sample_lst[l//3], border_radius[l//3]), (sample_lst[-1], border_radius[-1])), linewidth=2, label='root func.')


plt.legend(loc='upper left')
plt.xlabel('Number of iteration')
plt.ylabel('Border radius of 99%')
plt.title("Drunkard's Walk Problem")
plt.savefig('result1.png')
