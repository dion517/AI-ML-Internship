import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("week2/Day4/feature_engineered_dataset.csv")

# Numerical columns to scale
columns = ["Age", "Fare"]

# StandardScaler
standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df[columns])

standard_df = pd.DataFrame(standard_scaled, columns=columns)

print("StandardScaler Output")
print(standard_df.head())


# MinMaxScaler
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df[columns])

minmax_df = pd.DataFrame(minmax_scaled, columns=columns)

print("\nMinMaxScaler Output")
print(minmax_df.head())