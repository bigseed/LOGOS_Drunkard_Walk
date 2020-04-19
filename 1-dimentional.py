import matplotlib.pyplot as plt
import numpy as np
import random


def drunken_walk(n, iteration):
    sample = np.zeros(n)

    for _ in range(iteration):
        sample = list(map(lambda x: x-1 if random.random()
                          >= 0.5 else x+1, sample))

    sample = np.array(sample)
    average = np.sum(sample) / n

    standard_deviation = np.array(
        list(map(lambda x: np.sqrt((x - average)**2), sample)))
    average_standard_deviation = np.sum(standard_deviation) / n

    return average_standard_deviation


def cal_root(coord1, coord2):
    b = np.log2(coord2[1]/coord1[1])
    a = coord1[1] / (coord1[0]**b)

    root = list(map(lambda x: a*(x**b), range(max_iter)))
    return root


n = 1500
max_iter = 700
av_SD = []
coord1, coord2 = 0, 0


for i in range(1, max_iter):
    if (max_iter - i) % 20 == 0:
        coord1 = (max_iter - i)/2
        coord2 = max_iter - i
        break

for iteration in range(0, max_iter, 10):
    temp = drunken_walk(n, iteration)
    av_SD.append(temp)

    if iteration == coord1:
        coord1 = (coord1, temp)

    if iteration == coord2:
        coord2 = (coord2, temp)
    print(f'{iteration} / {max_iter}')

root = cal_root(coord1, coord2)

fig, ax = plt.subplots()
plt.plot(range(0, max_iter, 10), av_SD, linewidth=3, label='Drunken Walk')
plt.plot(range(len(root)), root, linewidth=5, label='root func.')

plt.legend(loc='upper left')
plt.xlabel('Number of iteration')
plt.ylabel('Value of Standard Deviation')
plt.title("Drunkard's Walk Problem")
plt.savefig('result1.png')
