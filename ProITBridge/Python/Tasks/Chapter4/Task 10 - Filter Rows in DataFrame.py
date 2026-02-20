# Task 10 - Filter Rows in DataFrame

# Filter Rows in Dataframe where "Age" is greater than 30

import pandas as pd 

file = pd.read_csv("employee_data.csv")

filt = file[file["Age"] > 30]  # Filter Rows where Age is greater than 30 

print(filt)