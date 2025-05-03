import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
df = pd.DataFrame(s)
df.columns = ['List1']
print("Actual Dataframe: \n",df)

# Add Column
df['List2'] = [20, 30, 40, 50, 60]
df['List3'] = df['List1'] + df['List2']
df['List4'] = df['List1'] * df['List2']
df['List5'] = df['List1'] / df['List2']
df['List5'] = [200, 300, 400, 500, 600]
df['List6'] = [200, 300, 400, 500, 600]
print("\nDataframe after adding columns: \n",df)    

# Delete a col
if 'List3' in df.columns:
    # del df['List3'] # delete using del
    df.pop('List6') # delete using pop

print("\nDataframe after deleting columns: \n",df)   

# drop using drop method (axis=1 for columns)
df1 = df.drop('List5', axis=1) 
print("\nDataframe after dropping columns: \n",df1)

# drop using drop method (axis=0 for Rows)
df1 = df.drop(index=[0], axis=0)
print("\nDataframe after dropping rows: \n",df1) 