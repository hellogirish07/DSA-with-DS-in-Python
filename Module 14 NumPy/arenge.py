import numpy as np

# arange() = much similer to the python function range()
print("By arange():")
a = np.arange(1, 10)
print(a)

# linespace() = return evenly spaced number over a spacified interval
print("By linespace():")
b = np.linspace(1, 10, 10)
print(b)

# random() = create array with random numbers
print("By random():")
c = np.random.rand(10, 1)
print(c)

# random() matrix
print("By random():")
d = np.random.rand(3,2)
print(d)

# flatten() = transform 2D array into 1D array
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("OG array:")
for i in e:
    print(i)

print("flatten array:")
print(e.flatten())