import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Week2/Day3/titanic.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display column names
print("\nColumn Names:")
print(df.columns)

# -------------------------------------------------
# Find required columns automatically
# -------------------------------------------------

# Passenger Class
class_col = None
for col in df.columns:
    if col.lower() in ["pclass", "class"]:
        class_col = col
        break

# Age
age_col = None
for col in df.columns:
    if col.lower() == "age":
        age_col = col
        break

# Survival
survived_col = None
for col in df.columns:
    if col.lower() == "survived":
        survived_col = col
        break

# Gender
sex_col = None
for col in df.columns:
    if col.lower() in ["sex", "gender"]:
        sex_col = col
        break

# -------------------------------------------------
# 1. Passenger Class
# -------------------------------------------------
if class_col:
    plt.figure(figsize=(6,5))
    sns.countplot(x=class_col, data=df)
    plt.title("Passenger Class Distribution")
    plt.xlabel("Passenger Class")
    plt.ylabel("Number of Passengers")
    plt.show()

# -------------------------------------------------
# 2. Age Distribution
# -------------------------------------------------
if age_col:
    plt.figure(figsize=(8,5))
    sns.histplot(df[age_col].dropna(), bins=20, kde=True)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

# -------------------------------------------------
# 3. Survival Count
# -------------------------------------------------
if survived_col:
    plt.figure(figsize=(6,5))
    sns.countplot(x=survived_col, data=df)
    plt.title("Survival Count")
    plt.xlabel("Survived")
    plt.ylabel("Number of Passengers")
    plt.show()

# -------------------------------------------------
# 4. Gender Distribution
# -------------------------------------------------
if sex_col:
    plt.figure(figsize=(6,5))
    sns.countplot(x=sex_col, data=df)
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Number of Passengers")
    plt.show()

# -------------------------------------------------
# 5. Survival by Gender
# -------------------------------------------------
if sex_col and survived_col:
    plt.figure(figsize=(7,5))
    sns.countplot(x=sex_col, hue=survived_col, data=df)
    plt.title("Survival by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Passengers")
    plt.legend(title="Survived", labels=["No", "Yes"])
    plt.show()