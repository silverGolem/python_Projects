import turtle as t
from random import*

tommy=t.Turtle()
tommy.speed(1000)
def draw(size_of_gap):
    for i in range (int(360/size_of_gap)):
        tommy.color(random(),random(),random())
        tommy.setheading(tommy.heading() +size_of_gap)
        tommy.circle(100 )
draw(2)












screen=t.Screen()
screen.exitonclick()