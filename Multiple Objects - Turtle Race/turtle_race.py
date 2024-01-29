from turtle import Turtle, Screen
import random
competitors = []
colors = ["blue", "green", "red", "yellow", "black", "orange", "purple"]


def create_racers():
    gap =0
    index = 0
    for new_turtle_racer in range(len(colors)):
        new_turtle_racer = Turtle(shape="turtle")        
        new_turtle_racer.color(colors[index])
        new_turtle_racer.penup()
        new_turtle_racer.goto(x=-230, y=200-gap)
        competitors.append(new_turtle_racer)
        gap+=50
        index+=1

def start_race():
    finish_race = True
    while finish_race:
        turtle_to_move = random.choice(competitors)
        turtle_to_move.forward(10)
        
        if turtle_to_move.xcor() == 230:
            finish_race = False
            return turtle_to_move.pencolor()
    


screen = Screen()
screen.setup(width=500,  height=500)
screen.listen()
create_racers()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
champion = start_race()
if user_bet == champion:
    print(f"You've won! The winner color is {champion}")
else:
    print(f"You've lost! The winner color is {champion}")
screen.exitonclick()