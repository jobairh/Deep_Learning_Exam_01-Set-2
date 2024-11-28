# Question 2: Data Structures in Python (20 Marks)

# (a) List Manipulations (10 Marks)
# Given the list:

# numbers = [12, 75, 150, 180, 145, 525, 50]

# Write a Python script that:
# Iterates through the list and prints each number.
# Skips any number greater than 500.
# Stops the loop if a number greater than 150 is encountered.
# Skips numbers that are divisible by 5.

# Answer-1
# Given list
numbers = [12, 75, 150, 180, 145, 525, 50]

# Iterate through the list
for num in numbers:
    # Skip numbers greater than 500
    if num > 500:
        continue
    # Stop the loop if a number greater than 150 is encountered
    if num > 150:
        break
    # Skip numbers divisible by 5
    if num % 5 == 0:
        continue
    # Print the number
    print(num)
