import numpy as np

# Create multiplication table
table = np.arange(1, 11) * np.arange(1, 11).reshape(10, 1)

print("10 x 10 Multiplication Table:")
print(table)