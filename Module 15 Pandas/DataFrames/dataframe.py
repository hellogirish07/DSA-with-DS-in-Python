import pandas as pd

# Emprty DataFrame
df = pd.DataFrame()
print(df)

# Creating DF using Series
s = pd.Series(['a', 'b', 'c', 'd'])
df1 = pd.DataFrame(s)
print(df1)