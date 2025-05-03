import pandas as pd

# Creating DataFrame from Series
name = pd.Series(['Rohit', 'Virat', 'Dhoni', 'Rahul', 'Shreyash' ])
team = pd.Series(['MI', 'RCB', 'CSK', 'DC', 'PBKS'])

dict = {'Name':name, 'Team':team}
df = pd.DataFrame(dict)
print("Creating DataFrame from Series")
print(df)

# Crating DF from List of Dictonary
i = [{'Name':'Virat', 'Sirname':'Kohli'},
     {'Name':'Rohit', 'Sirname':'Sharma'},
     {'Name':'Hardik', 'Sirname':'Pandaya'},]

df2 = pd.DataFrame(i)
print("\nCrating DF from List of Dictonary")
print(df2)