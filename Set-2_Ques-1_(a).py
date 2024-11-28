# Set-2

# Question 1: Python Fundamentals and Control Structures (15 Marks)

#  (a) Basic Data Types and Input/Output (5 Marks)
#  Write a Python program that:
#  Prompts the user to input their full name and age.
#  Prints a greeting that includes their name and calculates the year they will turn 100 years old.

# Answer-1

name = input("Enter your full name: ")
age = int(input("Enter your age: "))

curr_year = 2024
yr_100 = curr_year + (100 - age)

print(f"Hello {name}!")
print(f"You will turn 100 years old in the year {yr_100}.")
