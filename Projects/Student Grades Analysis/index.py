import pandas as pd

# Load the CSV file
df = pd.read_csv("C:/Users/Girish/Desktop/Python Tutorials/Projects/Student Grades Analysis/data.csv")

# Show the first few rows
print("Initial DataFrame:")
print(df)

# Calculate average for each student
print("\nCalculating average grades...")
df["Average"] = df[["Math", "Science", "English", "History"]].mean(axis=1)
print(df[["Name", "Average"]])

# Sort in descending order of average
print("\nSorting students by average grades...")
sorted_df = df.sort_values(by="Average", ascending=False)
print(sorted_df[["Name", "Average"]])

# Find the top and lowest scorer
print("\nTop and lowest scorer:")
top_student = df.loc[df["Average"].idxmax()]
bottom_student = df.loc[df["Average"].idxmin()]
print("Top Scorer:", top_student["Name"], "with average", top_student["Average"])
print("Lowest Scorer:", bottom_student["Name"], "with average", bottom_student["Average"])
