import turtle
import pandas as pd

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")

image = './D25_US_state_game/blank_states_img.gif'

screen.addshape(image)
turtle.shape(image) #use image as shape


# Get the coordinates on the screen:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)

guess_input = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

state_coor_dir = "./D25_US_state_game/50_states.csv"
state_coor = pd.read_csv(state_coor_dir)

guessed_states = []


while len(guessed_states) <50:
    if guess_input == 'Exit':
        break
    
    if guess_input in state_coor.state.to_list():
        xcoor = state_coor.loc[state_coor.state == guess_input, "x"]
        ycoor = state_coor.loc[state_coor.state == guess_input, "y"]
        state_xy = (int(xcoor), int(ycoor))
        
        state_mark = turtle.Turtle()
        state_mark.penup()
        state_mark.hideturtle()
        state_mark.color('black')
        state_mark.goto(state_xy)
        state_mark.write(f"{guess_input}", align="center", font = FONT)

        guessed_states.append(guess_input)
    
    guess_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()


#save missing state names as .csv
    
missing_states = [state for state in state_coor.state.to_list() if state not in guessed_states]
pd.DataFrame({'state' : missing_states}).to_csv('./D25_US_state_game/missing_states.csv')


# Keep the screen on
#turtle.mainloop()
#screen.exitonclick() #Alternative method