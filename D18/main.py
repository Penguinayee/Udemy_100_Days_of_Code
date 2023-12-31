# import colorgram

# # Extract n colors as a list from an image.
# def extract_colors(file, n_colors):
#     colors = colorgram.extract(file, n_colors)
#     color_list = []
#     for i in range(len(colors)):
#         color_list.append(tuple(colors[i].rgb))
#     return color_list

# colors = extract_colors('image.jpg', 30)
# print(colors)


color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

import turtle as t
import random

t.colormode(255) # set the rgb color mode

tim = t.Turtle()

tim.speed('fastest')

tim.penup()
tim.hideturtle()
tim.setposition(-250, -250)

for _ in range(10):
    for _ in range(10):
        #tim.pendown()
        tim.dot(20, random.choice(color_list)) #tim.width(20) #tim.forward(0) 
        #tim.penup()
        tim.forward(50)
    tim.setposition(-250, tim.pos()[1] + 50)




screen = t.Screen()
screen.exitonclick()
