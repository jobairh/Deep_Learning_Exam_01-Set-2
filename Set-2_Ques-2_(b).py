# (b) Dictionary and Set Operations (10 Marks)
# You have two sets of student names:

# english_students = {"Emma", "Olivia", "Ava", "Isabella", "Sophia"}
# math_students = {"Olivia", "Ava", "Mia", "Charlotte", "Amelia"}

# Perform the following tasks:
# Find the students who are enrolled in both English and Math courses. (3 Marks)
# Find the students who are enrolled in English but not in Math. (3 Marks)
# Create a dictionary where the keys are student names from both sets, and the values are the
# courses they are enrolled in. (4 Marks)

# Answer-2

english_students = {"Emma", "Olivia", "Ava", "Isabella", "Sophia"}
math_students = {"Olivia", "Ava", "Mia", "Charlotte", "Amelia"}

both_courses_students = english_students & math_students
print("Students enrolled in both English and Math:", both_courses_students)

english_enrolled = english_students - math_students
print("Students enrolled in English but not in Math:", english_enrolled)

student_courses = {}

for student in english_students:
    student_courses[student] = "English"

for student in math_students:
    if student in student_courses:
        student_courses[student] += ", Math"
    else:
        student_courses[student] = "Math"

print("Dictionary of students and their enrolled courses:", student_courses)
