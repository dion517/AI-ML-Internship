import numpy as np

marks = np.random.randint(1, 101, 50)

print("Student Marks:")
print(marks)

print("\nHighest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
print("Average:", np.mean(marks))

print("\nStudents scoring above 75:")
print(marks[marks > 75])

print("\nStudents scoring below 40:")
print(marks[marks < 40])