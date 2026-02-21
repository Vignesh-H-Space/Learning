# Task 7 - Read CSV and Top 5 Rows

# Use Pandas to read a CSV file and then print the top 5 Rows 

import pandas as pd 

word = pd.read_csv("Euro_2012_stats_TEAM.csv")

print(word.head())