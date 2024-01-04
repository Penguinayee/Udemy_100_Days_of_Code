import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, 'Up')


game_is_on = True
while game_is_on:
    # generate a new car only every 6th time the game loop runs
    for frame_id in range(6):
        time.sleep(0.1)

        if frame_id == 0:
            car_manager.add_new_car()

        # Detect when the turtle player collides with a car and stop the game
        for car in car_manager.car_list:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        if player.ycor() > player.finish_line:
            car_manager.car_speed *= 1.2
            player.reset_game()
            scoreboard.add_level()

        car_manager.car_move()
        screen.update()
    


screen.exitonclick()