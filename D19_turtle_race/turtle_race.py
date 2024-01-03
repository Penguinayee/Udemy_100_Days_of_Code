from turtle import Turtle, Screen
import random


#tim.speed('fastest')

screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput(title = 'Make a bet', prompt='Which turtle will win the race? Enter a color:')

colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
race_on = False

turtle_list = []
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = -90 + 30*turtle_index)
    turtle_list.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f'You win. The winner is {winner_color} turtle')
            else:
                print(f'You lost. The winner is {winner_color} turtle')

        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()