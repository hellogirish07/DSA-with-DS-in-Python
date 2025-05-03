import pandas as pd

# Basic Data Structures of pandas 
# 1. Series : 1D Array representation
# 2. DataFrame : A object wich represent 2D array

# Serie with default index
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# Serie with customized index
s2 = pd.Series([1.23, 2.25, 5.42], index = ['a', 'b', 'c'])
print(s2)
print(s2[2])
print(s2['c'])

s3 = s1 + 5
print(s3)

# Filtaring Data
s4 = s1[s1 > 20]
print(s4)

s5 = s1[(s1 > 20) & (s1 < 50)]
print(s5)

# Number of element in series
print("Series s1 is: \n", s1)
print("Size of series is:", s1.size)