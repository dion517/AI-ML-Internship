import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week2/Day4/cleaned_dataset.csv")

# Histogram
plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=20)
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure(figsize=(6,4))
plt.boxplot(df["Age"])
plt.title("Box Plot of Age")
plt.ylabel("Age")
plt.show()