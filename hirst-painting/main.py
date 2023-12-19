# # from colorgram import extract
import turtle
from turtle import *
from random import *
# # colors=extract("image.jpg",10)
# # colors_list=[]
# # for color in colors:
# #     r=color.rgb.r
# #     g=color.rgb.g
# #     b=color.rgb.b
# #     new_color= (r,g,b)
# #     colors_list.append(new_color)
# # print(colors_list)
# tommy=Turtle()
# turtle.colormode(255)
# color_list=[(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
#
# prev_pos=0
# tommy.hideturtle()
# tommy.setheading(225)
# tommy.penup()
# tommy.speed("fastest")
# tommy.forward(350)
# tommy.setheading(0)
# pos=tommy.pos()
# posy=pos[0]
# for row in range (10):
#     tommy.goto(pos[0],posy)
#     posy+=50
#     for inRow in range(10):
#         tommy.dot(20,choice(color_list))
#         tommy.forward(50)
#
# screen=Screen()
# screen.exitonclick()
#import turtle as t
from random import*

tommy=Turtle()
tommy.shape("turtle")
tommy.speed(1000)
def draw(size_of_gap):
    for i in range (int(360/size_of_gap)):
        tommy.color(random(),random(),random())
        tommy.setheading(tommy.heading() +size_of_gap)
        tommy.circle(100 )
draw(1)












screen=Screen()
screen.exitonclick()

#
#
#
#
#
#
#
#
#
