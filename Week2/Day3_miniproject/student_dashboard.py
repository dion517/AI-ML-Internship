import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("Week2/Day3_miniproject/student_performance.csv")

# Create folder to save charts
scripts_dir = os.path.dirname(os.path.abspath(__file__))
charts_dir = os.path.join(scripts_dir, "charts")
os.makedirs(charts_dir, exist_ok=True)

# 1. Line Chart
avg_scores = df.groupby("Hours_Studied")["Exam_Score"].mean()
plt.figure(figsize=(6,4))
plt.plot(avg_scores.index, avg_scores.values, marker='o')
plt.title("Average Exam Score by Hours Studied")
plt.xlabel("Hours Studied")
plt.ylabel("Average Exam Score")
plt.grid(True)
plt.savefig(os.path.join(charts_dir, "line_chart.png"))
plt.show()

# 2. Bar Chart
avg = df.groupby("Motivation_Level")["Exam_Score"].mean()
avg.plot(kind="bar")
plt.title("Average Exam Score by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "bar_chart.png"))
plt.show()

# 3. Pie Chart
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ylabel=""
)
plt.title("Gender Distribution")
plt.savefig(os.path.join(charts_dir, "pie_chart.png"))
plt.show()

# 4. Histogram
plt.figure(figsize=(6,4))
plt.hist(df["Exam_Score"], bins=15)
plt.title("Exam Score Distribution")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.savefig(os.path.join(charts_dir, "histogram.png"))
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Attendance"], df["Exam_Score"])
plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance")
plt.ylabel("Exam Score")
plt.savefig(os.path.join(charts_dir, "scattered_plot.png"))
plt.show()

# 6. Box Plot
plt.figure(figsize=(5,4))
sns.boxplot(y=df["Exam_Score"])
plt.title("Exam Score Box Plot")
plt.savefig(os.path.join(charts_dir, "box_plot.png"))
plt.show()

# 7. Heatmap
cols = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Scores",
    "Tutoring_Sessions",
    "Physical_Activity",
    "Exam_Score"
]

plt.figure(figsize=(7,5))
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(charts_dir, "heatmap.png"))
plt.show()

# Report
print("\nSTUDENT PERFORMANCE REPORT")
print("----------------------------")
print("Average Exam Score :", round(df["Exam_Score"].mean(), 2))
print("Highest Exam Score :", df["Exam_Score"].max())
print("Average Attendance :", round(df["Attendance"].mean(), 2))
print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nHighest Performing Motivation Level:")
print(df.groupby("Motivation_Level")["Exam_Score"].mean().idxmax())

print("\nOverall Observations")
print("- Higher attendance generally leads to better exam scores.")
print("- More study hours improve performance.")
print("- Motivation level affects student performance.")