import numpy as np

# 2D Array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 1st way
# print(arr)

# 2nd way
for x in arr:
    print(x)

# Dimantions of array
a = np.array([1, 2, 3])
print("DImantions of a:", a.ndim)
print("Numbers of element:", a.size) # for size
print("Order is:", a.shape) # for order 

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("DImantions of b:", b.ndim)
print("Numbers of element:", b.size)
print("Order is:", b.shape)

# Reshape
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("Array before Reshape:")
print(c)

print("Array after Reshape:")
c = c.reshape(6,2)
print(c)