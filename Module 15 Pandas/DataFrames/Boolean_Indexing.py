import pandas as pd

# Boolean Indexing in DataFrame
dict = {
    'Name': ['John', 'Anna', 'Peter', 'Amenda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(dict)
print("Original DataFrame:\n", df)

df2 = pd.DataFrame(dict, index=['T', 'F', 'T', 'F'])
print("\nDataFrame with custom index:\n", df2)
print("\nBoolean Indexing (T):\n", df2[df2.index == 'T'])
print("\nBoolean Indexing (Age):\n", df2[df2['Age'] > 30])