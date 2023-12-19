from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.speed_of_car=0.1
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(0,-280)

    def increase_speed_of_car(self):
        self.speed_of_car *= 0.7

