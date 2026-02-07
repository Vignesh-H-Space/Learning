# Data Frames with Dictionary 

import pandas as pd 

# Example 1
data1 = {"Avengers":["Thor","Captain America","Hulk","Iron Man"],"Power":[90,85,95,80]}

print(pd.DataFrame(data=data1))

# Example 2
data2 = {"Country":("India","USA","Russia","UK","Germany","France"),"Capital":("New Delhi","Washington DC","Moscow","London","Berlin","Paris")}

print(pd.DataFrame(data=data2))