import numpy as np

# Search 
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = np.where(arr == 5)
print(x)

# find the index value where arr is even
y = np.where(arr % 2 == 0)
print(y)

# Filtaring 
arr2 = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr2[x]
print("Filterd Array:",newarr)
