from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)
    def add_part(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snake_body.append(new_snake)
    def grow(self):
        self.add_part(self.snake_body[-1].position())
    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_part - 1].xcor()
            new_y = self.snake_body[snake_part - 1].ycor()
            self.snake_body[snake_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for snake_part in self.snake_body:
            snake_part.goto(10000, 10000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]