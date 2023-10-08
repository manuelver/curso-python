"""
02_stats.py
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

# Numpy and Statistics

# Matrix in numpy

four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

print()

# Numpy numpy.arange()

# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)

print()

for l in lst:
    print(l)

print()

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

print()

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)

print()

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

print()

even_numbers = np.arange(2, 20, 2)
print(even_numbers)

print()

# Creating sequence of numbers using linspace

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
print(np.linspace(1.0, 5.0, num=10))

print()

# not to include the last value in the interval
print(np.linspace(1.0, 5.0, num=5, endpoint=False))

print()

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

print(np.logspace(2, 4.0, num=4))

print()

# to check the size of an array
x = np.array([1, 2, 3], dtype=np.complex128)
print(x)

print()

print(x.itemsize)

print()

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)

print()

print('First row: ', np_list[0])
print('Second row: ', np_list[1])

print()

print('First column: ', np_list[:, 0])
print('Second column: ', np_list[:, 1])
print('Third column: ', np_list[:, 2])

print()

# NumPy Statistical Functions with Example

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)

print()

# min, max, mean, median, sd

two_dimension_array = np.array([
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ', two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print()

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))

print()

# How to create repeating sequences?

a = [1, 2, 3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

print()


# How to generate random numbers?

# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)

print()

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2, 3])
print(r)

print()

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

print()

# Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2, 2)
print(rand)

print()

rand2 = np.random.randn(2, 2)
print(rand2)

print()

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5, 3])
print(rand_int)

print()


# mean, standard deviation, number of samples
np_normal_dis = np.random.normal(5, 0.5, 1000)
np_normal_dis
# min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

print()

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

print()


# Linear algebra

# Dot product: product of two arrays
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
# 1*4+2*5 + 3*6
dot_product = np.dot(f, g)
print(dot_product)

print()

# Matmul: matruc product of two arrays
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
# 1*5+2*7 = 19
matmul = np.matmul(h, i)
print(matmul)

print()

# Determinant 2*2 matrix
# 5*8-7*6np.linalg.det(i)
matri = np.linalg.det(i)
print(matri)

print()

Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

print()

new_list = [x + 2 for x in range(0, 11)]
print(new_list)

print()

np_arr = np.array(range(0, 11))
np_arr + 2
print(np_arr)

print()


temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()


mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x)
ax.set(xlabel="x", ylabel='y')
plt.show()
