import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition (A + B):")
print(A + B)

print("\nSubtraction (A - B):")
print(A - B)

print("\nMultiplication (A × B):")
print(np.dot(A, B))


print("\nTranspose of Matrix A:")
print(A.T)

print("\nInverse of Matrix A:")
print(np.linalg.inv(A))
