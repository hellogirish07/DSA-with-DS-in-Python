import numpy as np

# Trace() = The trace of a square matrix is the sum of the elements on its main diagonal (from the top-left to the bottom-right).
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Orignal Array:")
for i in a:
    print(i)

print("Trace of given matrix:", a.trace())
print("Trace:", sum(a.diagonal()))

# Transpos of Matrix
print("Orignal Array:")
for i in a:
    print(i)

print("Transpos of Mtarix:", np.transpose(a))
print("Transpos of Mtarix:", a.transpose())