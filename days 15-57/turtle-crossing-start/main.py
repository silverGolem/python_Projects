import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager,remove_from_traffic
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
score=Scoreboard()
game_is_on = True
screen.onkeypress(key="Up",fun= player.move_up)
while game_is_on:
    time.sleep(player.speed_of_car)
    screen.update()
    if player.ycor()>280:
        score.increase_level()
        player.reset()
        player.increase_speed_of_car()
    if car_manager.collision(player):
        score.game_over()
        game_is_on=False
        continue
    new_car = CarManager()
    new_car.move_traffic()
    remove_from_traffic()






screen.exitonclick()