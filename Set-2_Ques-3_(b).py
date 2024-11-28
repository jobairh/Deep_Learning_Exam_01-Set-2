# (b) Array Reshaping and Mathematical Operations (7 Marks)
# Given the array:

# array = np.arange(1, 13)

# Reshape the array into a (4, 3) matrix. (2 Marks)
# Compute the natural logarithm of each element in the reshaped matrix. (3 Marks)
# Flatten the matrix back into a one-dimensional array. (2 Marks)

# Answer-2
import numpy as np

array = np.arange(1, 13)
print("Original Array:")
print(array)

reshaped_array = array.reshape(4, 3)
print("Reshaped Array (4x3 matrix):\n", reshaped_array)

log_array = np.log(reshaped_array)
print("Natural logarithm of each element in the reshaped array:\n", log_array)

flattened_array = log_array.flatten()
print("Flattened array after applying logarithm:\n", flattened_array)
