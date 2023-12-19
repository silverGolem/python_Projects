import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_dec = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange","yellow","green","blue", "purple"]
all_turtle=[]
i= -80
is_race_on= False
for color in colors:
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    all_turtle.append(new_turtle)
    new_turtle.goto(-230,i)
    i+=30

if user_dec:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        forward= random.randint(0,10)
        turtle.forward(forward)
        if turtle.xcor() >= 230:
            winner=turtle.pencolor()
            is_race_on= False
            break
if winner == user_dec:
    print(f"You won, {winner} turtle got the win")
else:
    print(f"You lose, {winner} turtle got the win")



screen.exitonclick()