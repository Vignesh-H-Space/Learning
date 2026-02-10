
# Initial Analysis
# Using shape attribute 

# Function()
# Attribute 

import pandas as pd 

order_details = pd.read_table(filepath_or_buffer= "data.tsv.txt")

print(order_details.shape)

print(order_details.isnull()) # Entire table with true returned where value is null 

print(order_details.isnull().sum())  # Chain of Functions or Chain of Commands
# Proper Descripton of null is returned 
