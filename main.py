from turtle import Screen
import time
import random
from snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


turt = Snake()
screen.listen()
screen.onkey(turt.up, "Up")
screen.onkey(turt.down, "Down")
screen.onkey(turt.left, "Left")
screen.onkey(turt.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)

    turt.move()







# TODO create food
# TODO detect collision with food
# TODO create scoreboard
# TODO detect wall collision
# TODO detect body collision

screen.exitonclick()
