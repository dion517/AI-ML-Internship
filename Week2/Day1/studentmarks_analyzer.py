import numpy as np

# Generate marks for 100 students (0 to 100)
marks = np.random.randint(0, 101, 100)

print("Student Marks:")
print(marks)

# Calculate statistics
highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)

# Students above 90 and below 35
above_90 = marks[marks > 90]
below_35 = marks[marks < 35]

# Pass and Fail Percentage
passed = np.sum(marks >= 35)
failed = np.sum(marks < 35)

pass_percentage = (passed / len(marks)) * 100
fail_percentage = (failed / len(marks)) * 100

# Display results
print("\n========== Student Marks Analyzer ==========")
print("Highest Mark           :", highest)
print("Lowest Mark            :", lowest)
print("Average Mark           :", round(average, 2))
print("Median Mark            :", median)
print("Standard Deviation     :", round(std_dev, 2))

print("\nStudents Scoring Above 90:")
print(above_90)

print("\nStudents Scoring Below 35:")
print(below_35)

print("\nPass Percentage        :", round(pass_percentage, 2), "%")
print("Fail Percentage        :", round(fail_percentage, 2), "%")