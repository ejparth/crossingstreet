from turtle import Screen
from player import Player
import time
from controls import Control

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Let's Cross")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.upy, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
