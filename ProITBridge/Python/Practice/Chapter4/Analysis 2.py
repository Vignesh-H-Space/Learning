#Data Analysis

# Rows - Observation / Record 
# Columns - Features / Parameters 

import pandas as pd 

order_details = pd.read_table(filepath_or_buffer= "data.tsv.txt")

print(order_details.isnull()) # Entire table with true returned where value is null 

print(order_details.isnull().sum())  # Chain of Functions or Chain of Commands
# Proper Descripton of null is returned 

print(order_details.dtypes)     # dtypes - Returns data types 

print(order_details.describe())  # Default Parameter - include = "None", Only two rows are shown since their datatype is int 

print(order_details.describe(include="all")) # When include = All, the entire table is shown 