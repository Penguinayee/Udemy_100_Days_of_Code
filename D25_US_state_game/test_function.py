import pandas as pd

state_coor_dir = "./D25_US_state_game/50_states.csv"
state_coor = pd.read_csv(state_coor_dir)

print(state_coor)
xcoor = state_coor.loc[state_coor.state == 'Ohio', "x"]
ycoor = state_coor.loc[state_coor.state == 'Ohio', "y"]

state_data = state_coor.loc[state_coor.state == 'Ohio']


print((xcoor, ycoor))
print(type(xcoor))

print(state_data.x, state_data.y)