import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array :")
print(arr1)
print("2D Array :")
print(arr3)

add = arr1 + arr2
mul = arr1 * arr2

print("Addition of Array :")
print(add)
print("Multiplication of Array :")
print(mul)