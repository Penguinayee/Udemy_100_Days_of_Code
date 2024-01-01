from turtle import Turtle, Screen


tim = Turtle()
tim.speed('fastest')

def move_forward():
    tim.forward(5)

def move_backward():
    tim.backward(5)

def counter_clockwise():
    tim.setheading(tim.heading() + 5)

def clockwise():
    tim.setheading(tim.heading() - 5)

def go_home():
    #tim.clear()
    #tim.home()
    tim.reset()

screen = Screen()

screen.listen()
screen.onkey(key = 'w', fun = move_forward)
screen.onkey(key = 's', fun = move_backward)
screen.onkey(key = 'a', fun = counter_clockwise)
screen.onkey(key = 'd', fun = clockwise)
screen.onkey(key = 'c', fun = go_home)

screen.exitonclick()