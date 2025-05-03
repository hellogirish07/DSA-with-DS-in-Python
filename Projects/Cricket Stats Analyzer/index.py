import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("C:/Users/Girish/Desktop/Python Tutorials/Projects/Cricket Stats Analyzer/data.csv")
print("Cricket Stats Analyzer")
print(df)

# Strike Rate = (Runs / BallsFaced) * 100
df["StrikeRate"] = np.round((df["Runs"] / df["BallsFaced"]) * 100, 2)

# Average = Runs / Matches
df["Average"] = np.round(df["Runs"] / df["Matches"], 2)

# Consistency Score = Std Dev of runs per match (simulate with numpy)
# For simplicity, assume runs per match is consistent, so std = 0
# Let's simulate slight variability in a NumPy array
runs_per_match = df["Runs"] / df["Matches"]
df["StdDev"] = np.round(np.random.normal(5, 2, size=len(df)), 2)  # fake variation

print("\nPlayer Stats with Strike Rate, Average, and Std Dev")
print(df[["Player", "StrikeRate", "Average", "StdDev"]])
print("\n")

# Top Scorer
top_scorer = df.loc[df["Runs"].idxmax()]
print("🏆 Top Scorer:", top_scorer["Player"], "-", top_scorer["Runs"])

# Top Strike Rate
top_striker = df.loc[df["StrikeRate"].idxmax()]
print("🔥 Top Strike Rate:", top_striker["Player"], "-", top_striker["StrikeRate"])

# Best Average
top_avg = df.loc[df["Average"].idxmax()]
print("💯 Highest Average:", top_avg["Player"], "-", top_avg["Average"])

# Most 100s
most_100s = df.loc[df["Hundreds"].idxmax()]
print("🏅 Most 100s:", most_100s["Player"], "-", most_100s["Hundreds"])

# Most 50s
most_50s = df.loc[df["Fifties"].idxmax()]
print("🥈 Most 50s:", most_50s["Player"], "-", most_50s["Fifties"])

