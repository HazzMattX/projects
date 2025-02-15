import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "space")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    car_manager.make_car()
    car_manager.drive()
    player.finish()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.finish():
        player.start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()