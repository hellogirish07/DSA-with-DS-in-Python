import pandas as pd

# Disctibe = summery of series
s1 = pd.Series([10, 20, 30, 40, 50, 20, 30, 40])
print("Summary of Series:")
print(s1.describe())