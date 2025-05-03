import pandas as pd

# Average / mean 
s1 = pd.Series([10, 20, 30, 40, 50, 20, 30, 40])
print("Series s1:\n", s1)
print("Mean of s1", s1.mean())

# Maximum in series
print("Maximum in series s1:", s1.max())

# Minimum in series
print("Minimum in series s1:", s1.min())

# Unique Values
print("Unique Values in series s1:", s1.unique())
print("Numbers of unique values in s1:", s1.nunique())