from turtle import Screen
from score import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake!!!!!!")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right,"d")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.grow()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.new_high_score()
        snake.reset()
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 10:
            scoreboard.new_high_score()
            snake.reset()
screen.exitonclick()