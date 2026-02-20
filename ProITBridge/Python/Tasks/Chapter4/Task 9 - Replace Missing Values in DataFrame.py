# Task 9 - Replace Missing Values in DataFrame

# Replace all the missing values in Dataframe with column's mean

import pandas as pd 

file = pd.read_csv("employee_data.csv")

# Before Change
print(file)

file = file.fillna(file.mean(numeric_only=True))        # Fill only numeric values since mean is only posible for numeric

# After Change
print(file)