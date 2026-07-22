import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week2/Day3/stud_visualize.csv")

#Marks

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks")
plt.xlabel("Students")
plt.ylabel("Average")
plt.xticks(rotation=45)
plt.show()

#Age

plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.show()

#Department 

dept = df["Department"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(dept.index, dept.values)
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

#Gender

gender = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender,
        labels=gender.index,
        autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.show()

#Attendance

plt.figure(figsize=(8,5))
plt.plot(df["Name"],
         df["Attendance"],
         marker='o')

plt.title("Attendance of Students")
plt.xlabel("Students")
plt.ylabel("Attendance (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

