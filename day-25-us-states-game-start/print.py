from turtle import Turtle
ALIGNMENT="center"
FONT=("Ariel",12,"normal")
class Print(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def print_state(self,x, y, name):
        self.goto(int(x), int(y))
        self.write(name)