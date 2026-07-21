import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)

print("Matrix:")
print(matrix)

print("\nFirst Row:")
print(matrix[0])

print("\nLast Row:")
print(matrix[-1])

print("\nFirst Column:")
print(matrix[:, 0])

print("\nLast Column:")
print(matrix[:, -1])

print("\nDiagonal Elements:")
print(np.diag(matrix))