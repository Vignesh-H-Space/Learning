# Data Frames with Dictionary 

import pandas as pd 

data1 = {"Avengers":["Thor","Captain America","Hulk","Iron Man"],"Power":[90,85,95,80]}

print(pd.DataFrame(data=data1))