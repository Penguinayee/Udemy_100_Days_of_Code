import turtle as t
import random

t.colormode(255) # set the rgb color mode

tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)

displacement = 5

for _ in range(int(360/displacement)):
    tim.color(random_color())
    tim.circle(50)
    tim.setheading(tim.heading()+ displacement)


screen = t.Screen()
screen.exitonclick()