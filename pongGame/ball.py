from turtle import Turtle
speed_number=[1,3,6,10]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
        self.just_bounce_paddle=False


    def move(self):
        new_x= self.xcor() + self.x_move
        new_y=self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.just_bounce_paddle=False
        self.y_move*= -1
    def bounce_x(self):
        if not self.just_bounce_paddle:
            self.x_move*= -1
            self.move_speed*=0.8
            self.just_bounce_paddle=True
    def reset(self):
        self.bounce_x()
        self.home()
        self.move_speed= 0.1


