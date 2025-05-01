import numpy as np

# 1D arrays
arr = np.array([1, 2, 3, 4, 5]) 
for i in arr:
    print(i) 

# Creating arry with 0s.
print("Arrays of 0s :")
a = np.zeros(5)
print(a)

print("Arrays of 1s :")
b = np.ones(5)
print(b)

# Sort array
arr2 = np.array([15, 10, 25, 52, 13, 11])
print("Orignal Array:", arr2)
print("Sorted Array:", np.sort(arr2))

