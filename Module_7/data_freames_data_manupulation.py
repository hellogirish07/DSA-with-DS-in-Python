import pandas as pd 

data = {'Name' : ['Girish', 'Naresh', 'Ravi', 'Nirmal'],
        'Age' : [23, 22, 20, 20],
        'City' : ['Abi Road', 'Odisha', 'Mumbai', 'Sirohi']}

df = pd.DataFrame(data)

print("DataFrame : ")
print(df)

print("\nAccesing the colunm :")
print(df['Name'])

print("\nAccesing the row :")
print(df.iloc[0])

print("\nApplying a function :")
print(df['Age'].apply(lambda x: x + 1))
