from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)
def right():
    tim.right(10)
def left():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forwards,key="Up" )
screen.onkey(key="Down", fun=move_back)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Left", fun=left)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
