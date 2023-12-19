from turtle import Turtle
ALIGNMENT= "center"
FONT=("Courier",15,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("C:/Users/raana/OneDrive/שולחן העבודה/data.txt") as file:
            self.high_score= int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.update_score()


    def update_score(self):
            self.clear()
            self.write(arg=f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

    def increase(self):
        self.score+=1
        self.update_score()
    def reset(self):
        if self.score> self.high_score:
            self.high_score=self.score
            with open("C:/Users/raana/OneDrive/שולחן העבודה/data.txt","w") as file:
                file.write(str(self.score))
        self.score=0
        self.update_score()



