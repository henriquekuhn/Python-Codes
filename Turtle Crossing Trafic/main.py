import time
from turtle import Screen
from car_manager import CarManager
from player import Player 
from scoreboard import ScoreBoard

cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

rosbiff_the_turtle = Player()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(rosbiff_the_turtle.go_up, "Up")

game_is_on = True
new_car = 5
while game_is_on:
    time.sleep(0.08)
    screen.update()
    if new_car == 5:
        cars.append(CarManager())
        new_car = 0
    new_car += 1
    for car in cars:
        car.move_forward()    
        if rosbiff_the_turtle.distance(car) < 20:
            game_is_on = scoreboard.colision()
    if rosbiff_the_turtle.ycor() == 280:
        game_is_on = scoreboard.victory()  
    





screen.exitonclick()