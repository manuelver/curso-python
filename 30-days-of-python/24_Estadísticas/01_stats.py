"""
01_stats.py
"""

import numpy as np

# Info numpy
print('numpy version:', np.__version__)
print()

print(dir(np))
print()

# Creating int numpy arrays

python_list = [1, 2, 3, 4, 5]

print('Type: ', type(python_list))

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))

print(numpy_array_from_list)

print()

# Creating float numpy arrays

python_list = [1, 2, 3, 4, 5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

print()

# Creating boolean numpy arrays

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

print()

# Creating multidimensional array using numpy

numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

print()

# Converting numpy array to list

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

print()

# Creating numpy array from tuple

python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print('python_tuple: ', python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

print()

# Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ',
      numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)

print()

# Data type of numpy array

int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

print()

# Size of a numpy array

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])

print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)

print()

# Mathematical Operation using numpy

# Addition
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

print()

# Subtraction
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

print()

# Multiplication
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

print()

# Division
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

print()

# Modulus
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

print()

# Floor division
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

print()

# Exponential
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)

print()

# Int,  Float numbers
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

print()

# Converting types

# int to float
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)

print()

# float to int
numpy_int_arr = np.array(numpy_int_arr, dtype='int')
print(numpy_int_arr)

print()

# float to bool
numpy_int_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(numpy_int_arr)

print()

# int to str

numpy_int_arr = np.array([1, 2, 3, 4], dtype='str')
print(numpy_int_arr)

print()

# Multi-dimensional Arrays

# 2 Dimension Array
two_dimension_array = np.array([
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

print()

# Getting items from a numpy array

# 2 Dimension Array
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

print()

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

print()

# Slicing Numpy array

first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

print()

# How to reverse the rows and the whole array?

print(two_dimension_array[::])

print()

# Reverse the row and column positions

print(two_dimension_array[::-1, ::-1])

print()

# How to represent missing values ?
print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)

print()

# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeroes)

print()


# Numpy Zeroes
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)

print()

twoes = numpy_ones * 2

print(twoes)

print()

# Reshape
# numpy.reshape(), numpy.flatten()
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)

print()

flattened = reshaped.flatten()
print(flattened)

print()

# Horitzontal Stack
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

print()

# Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

print()

# Generating Random Numbers

# Generate a random float  number
random_float = np.random.random()
print(random_float)

print()

# Generate a random float  number
random_floats = np.random.random(5)
print(random_floats)

print()

# Generating a random integers between 0 and 10

random_int = np.random.randint(0, 11)
print(random_int)

print()

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2, 10, size=4)
print(random_int)

print()

# Generating a random integers between 0 and 10
random_int = np.random.randint(2, 10, size=(3, 3))
print(random_int)

print()

# Generationg random numbers

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

print()
