import numpy as np

# 1. Broadcasting Example
a = np.array([[1], [2], [3]])   # Shape: (3,1)
b = np.array([10, 20, 30])      # Shape: (3,)
broadcasted = a * b            # Automatically reshaped to (3,3)
print("Broadcasted Result:\n", broadcasted)

# 2. Advanced Indexing
arr = np.array([10, 20, 30, 40, 50])
index = [0, 2, 4]
print("Fancy Indexing:", arr[index])  # [10, 30, 50]

# Boolean Indexing
bool_idx = arr > 25
print("Boolean Indexing:", arr[bool_idx])  # [30 40 50]

# 3. Vectorized Operation
x = np.array([1, 2, 3, 4])
squared = x ** 2  # No for loop!
print("Squared:", squared)

# 4. Aggregation
matrix = np.array([[1, 2], [3, 4]])
print("Sum (axis=0):", np.sum(matrix, axis=0))  # Column-wise sum
print("Mean:", np.mean(matrix))

# 5. Linear Algebra
A = np.array([[2, 1], [1, 3]])
inv_A = np.linalg.inv(A)
det_A = np.linalg.det(A)
eig_vals, eig_vecs = np.linalg.eig(A)
print("Inverse:\n", inv_A)
print("Determinant:", det_A)
print("Eigenvalues:", eig_vals)
print("Eigenvectors:\n", eig_vecs)

# 6. Reshape and Stack
x = np.arange(6).reshape(2, 3)
y = np.ones((2, 3))
stacked = np.hstack((x, y))  # Horizontal stack
print("Stacked:\n", stacked)

# 7. Random Numbers
np.random.seed(42)
rand_nums = np.random.randint(0, 100, (3, 3))
print("Random Integers:\n", rand_nums)
