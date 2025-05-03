import pandas as pd

# Concatenation of DataFrames
dict1 = {
    'Name': ['John', 'Anna', 'Peter', 'Amenda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

dict2 = {
    'Name': ['Chris', 'Sophia', 'James', 'Emma'],
    'Age': [30, 22, 29, 27],
    'City': ['Toronto', 'Sydney', 'Tokyo', 'Mumbai']
}

df1 = pd.DataFrame(dict1)
print("Original DataFrame 1:\n", df1)

df2 = pd.DataFrame(dict2)
print("\nOriginal DataFrame 2:\n", df2)

# Concaenation
# df3 = pd.concat([df1, df2])  
df3 = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame:\n", df3)