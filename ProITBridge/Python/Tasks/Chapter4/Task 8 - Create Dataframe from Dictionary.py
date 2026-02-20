# Task 8 - Create Dataframe from Dictionary

# Create a dataframe from Python Dictionary

import pandas as pd

dict = {"Leagues":["Premier League","Laliga","Serie A","Bundesliga","Ligue1"],"Teams":["Arsenal","Barcelona","Napoli","Bayern","Monaco"],"League Standings":[1,2,5,1,7], "Top Scorer" : ["Gyokeres","Yamal","McTominay","Kane","Silva"],"Trophies":[48,64,29,58,15]}

print(pd.DataFrame(dict))
