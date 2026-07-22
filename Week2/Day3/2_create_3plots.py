#Histogram

import matplotlib.pyplot as plt

marks = [55,60,62,65,70,72,75,78,80,82,85,88,90,92,95]

plt.figure(figsize=(6,4))
plt.hist(marks, bins=5)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot

age = [18,19,20,21,22,23]
marks = [65,70,75,80,85,90]

plt.figure(figsize=(6,4))
plt.scatter(age, marks)
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

#Box Plot

marks = [55,60,62,65,70,72,75,78,80,82,85,88,90,92,95]

plt.figure(figsize=(4,6))
plt.boxplot(marks)
plt.title("Marks Box Plot")
plt.ylabel("Marks")
plt.show()