from turtle import Screen
from paddle import Paddle
from puck import Puck
from scoreboard import Scoreboard
import time


screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
puck = Puck()
scoreboard = Scoreboard()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    puck.move()
    puck.bounce(l_paddle, r_paddle)
    if puck.xcor() > 380:
        puck.reset_position()
        scoreboard.l_point()
    if puck.xcor() < -380:
        puck.reset_position()
        scoreboard.r_point()
    if scoreboard.l_score == 7:
        scoreboard.winner("PLAYER 1")
        game_on = False
    elif scoreboard.r_score == 7:
        scoreboard.winner("PLAYER 2")
        game_on = False
screen.exitonclick()
