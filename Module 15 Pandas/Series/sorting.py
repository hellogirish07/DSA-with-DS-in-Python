import pandas as pd

# Sorting in Series
s2 = pd.Series([20, 40, 95, 75, 86, 56])
print("\nOrignal Series:")
print(s2)

print("\nSorted Series:")
print(s2.sort_values())

print("\nSorted Series with Reset Index:")
sorted_s2 = s2.sort_values().reset_index(drop=True)
print(sorted_s2)