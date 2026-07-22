import matplotlib.pyplot as plt

subjects = ["Python", "Math", "Science", "English", "AI"]
marks = [88, 75, 92, 80, 95]

plt.figure(figsize=(6,4))
plt.plot(subjects, marks, marker='o')
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

#line chart 2

months = ["Jan","Feb","Mar","Apr","May"]
attendance = [90,92,88,95,93]

plt.figure(figsize=(6,4))
plt.plot(months, attendance, marker='s')
plt.title("Monthly Attendance")
plt.xlabel("Month")
plt.ylabel("Attendance (%)")
plt.grid(True)
plt.show()

#bar chart 1

plt.figure(figsize=(6,4))
plt.bar(subjects, marks)
plt.title("Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

#bar chart 2

departments = ["CSE","ECE","EEE","MECH"]
students = [50,35,25,20]

plt.figure(figsize=(6,4))
plt.bar(departments, students)
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.show()

#pie chart 1

plt.figure(figsize=(6,6))
plt.pie(students,
        labels=departments,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Department Distribution")
plt.show()

#pie chart 2

activities = ["Study","Sports","Sleep","Entertainment"]
hours = [8,2,8,6]

plt.figure(figsize=(6,6))
plt.pie(hours,
        labels=activities,
        autopct="%1.1f%%")
plt.title("Daily Activities")
plt.show()