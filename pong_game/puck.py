from turtle import Turtle
class Puck(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.x_move = 10  # Horizontal velocity
        self.y_move = 10  # Vertical velocity
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce(self, l_paddle, r_paddle):
        if self.ycor() > 290 or self.ycor() < -290:
            self.y_move *= -1  # Reverse vertical direction
        if self.xcor() > -340 and l_paddle.distance(self) < 50:
            self.x_move *= -1
        if self.xcor() < 340 and r_paddle.distance(self) < 50:
            self.x_move *= -1
    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
