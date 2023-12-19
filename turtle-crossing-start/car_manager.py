from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
TO_THE_LEFT=180
traffic=[]

def slow_preparation():
    num=random.randint(2,100)

# Iterate from 2 to n / 2
    for i in range(2, int(num / 2) + 1):
# If num is divisible by any number between
# 2 and n / 2, it is not prime
        if (num % i) == 0:
            return 0
    else:
        return 1


def remove_from_traffic():
    for car in traffic:
        if car.xcor() <-320:
            traffic.remove(car)

def collision(player_pos):
     for car in traffic:
        if car.distance(player_pos)< 20:
            return 1
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(TO_THE_LEFT)
        self.setx(320)
        self.sety(random.randrange(-220,260,20))
        if slow_preparation():
            self.add_to_traffic()


    def move_traffic(self):
        for car in traffic:
            car.forward(STARTING_MOVE_DISTANCE)

    def add_to_traffic(self):
        traffic.append(self)





