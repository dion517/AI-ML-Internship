import numpy as np

# Generate a 5x5 random matrix
matrix = np.random.randint(1, 21, (5, 5))

print("Random Matrix:")
print(matrix)

print("\nRow-wise Sum:")
print(np.sum(matrix, axis=1))

print("\nColumn-wise Sum:")
print(np.sum(matrix, axis=0))