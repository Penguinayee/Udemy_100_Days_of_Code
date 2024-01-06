# with open("./D25/weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# import csv

# with open("./D25/weather_data.csv") as file:
#     data = csv.reader(file, )
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
    
#     print(temperatures)

# import pandas as pd

# df = pd.read_csv("./D25/weather_data.csv")
# print(df)


import pandas as pd

df = pd.read_csv("./D25_central_park_squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(df.head())
# print(df.columns)

fur_df = pd.DataFrame(df["Primary Fur Color"].value_counts())

fur_df.rename({'Gray': 'grey',
               'Cinnamon': 'red',
               'Black':'black'}, axis = 0, inplace=True)
fur_df.reset_index(inplace=True)
fur_df.columns = ['Fur color', 'Count']

print(fur_df)

