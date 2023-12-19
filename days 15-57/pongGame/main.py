from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Raanan's pong game")
screen.tracer(0)
screen.listen()
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
screen.update()
screen.onkeypress(key="Up",fun=r_paddle.up)
screen.onkeypress(key="Down",fun=r_paddle.down)
screen.onkeypress(key="w",fun=l_paddle.up)
screen.onkeypress(key="s",fun=l_paddle.down)
ball=Ball()
score=Scoreboard()
while 1:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) <50 and 320 < ball.xcor()< 360 or ball.distance(l_paddle) <50 and -320 > ball.xcor()> -360:
        ball.bounce_x()
    if ball.xcor()>380:
        score.increase_l_score()
        ball.reset()
    if ball.xcor() < -380:
        score.increase_r_score()
        ball.reset()










screen.exitonclick()