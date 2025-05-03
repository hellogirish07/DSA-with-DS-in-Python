import pandas as pd

# Accesing Data Row Wise
i = [{'Name':'Virat', 'Sirname':'Kohli'},
     {'Name':'Rohit', 'Sirname':'Sharma'},
     {'Name':'Hardik', 'Sirname':'Pandaya'},]

df = pd.DataFrame(i)
print("Accesing Data Row Wise")
print(df)

for (row_index, row_values) in df.iterrows() :
    print("\nRow Index is:", row_index)
    print("Row Value is:\n", row_values)
    
# Accesing Data Col Wise
j = [{'Name':'Virat', 'Sirname':'Kohli'},
     {'Name':'Rohit', 'Sirname':'Sharma'},
     {'Name':'Hardik', 'Sirname':'Pandaya'},]

df2 = pd.DataFrame(j)
print("\nAccesing Data Column Wise")
print(df2)

for (col_index, col_values) in df2.items() :
    print("\nColumn Index is:", col_index)
    print("Column Value is:\n", col_values)