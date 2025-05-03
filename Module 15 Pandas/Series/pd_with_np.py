import pandas as pd 
import numpy as np

# Working with series in Pandas along with Numpy
arr = np.array([10, 20, 30, 40, 50])
s = pd.Series(arr)
print(s)

t = np.sqrt(s)
print(t)

# Printing arr in pd with custom index
arr2 = np.array([100, 200, 300, 400, 500])
idx = np.array(['a', 'b', 'c', 'd', 'e'])
s = pd.Series(arr2, index = idx)
print(s)

