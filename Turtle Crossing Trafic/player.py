from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(START_POSITION)
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)