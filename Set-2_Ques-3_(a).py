# Question 3: NumPy Array Operations (15 Marks)
# (a) Array Creation and Indexing (8 Marks)
# Create a NumPy array of shape (5, 5) filled with random integers between 1 and 100. (2 Marks)

# Replace all the even numbers in the array with zero. (3 Marks)
# Calculate the sum of all the numbers in each column and store the results in a one-dimensional
# array. (3 Marks)

# Answer-1
import numpy as np

array = np.random.randint(1, 101, size=(5, 5))
print("Original Array:\n", array)

array[array % 2 == 0] = 0
print("Array after replacing even numbers with zero:\n", array)

column_sums = np.sum(array, axis=0)
print("Sum of each column:\n", column_sums)
