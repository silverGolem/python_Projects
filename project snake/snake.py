from turtle import Turtle
SNACK_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
RIGHT=0
LEFT=180
UP=90
DOWN=270
last_call_pos=[]
class Snake:
    def __init__(self):
        self.seg=[]
        self.create_snake()
        self.head=self.seg[0]
    def create_snake(self):
        for pos in SNACK_POS:
            self.add_segment(pos)


    def up(self):
        global last_call_pos
        if self.head.heading() !=DOWN and last_call_pos != list(self.head.position()):
            self.head.setheading(UP)
            last_call_pos=list(self.head.position())

    def down(self):
        global last_call_pos
        if self.head.heading() != UP and last_call_pos != list(self.head.position()):
            self.head.setheading(DOWN)
            last_call_pos = list(self.head.position())

    def right(self):
        global last_call_pos
        if self.head.heading() != LEFT and last_call_pos != list(self.head.position()):
            self.head.setheading(RIGHT)
            last_call_pos = list(self.head.position())


    def left(self):
        global last_call_pos
        if self.head.heading() != RIGHT and last_call_pos != list(self.head.position()):
            self.head.setheading(LEFT)
            last_call_pos = list(self.head.position())

    def move(self):

        for segment in range(len(self.seg) - 1, 0, -1):
            new_xcor = self.seg[segment - 1].xcor()
            new_ycor = self.seg[segment - 1].ycor()
            self.seg[segment].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,pos):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.seg.append(new_turtle)

    def reset(self):
        for segment in self.seg:
            segment.goto(1000,1000)

        self.seg.clear()
        self.create_snake()
        self.head=self.seg[0]


    def extend(self):
        self.add_segment(self.seg[-1].position())



