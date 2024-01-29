from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITION:
            rosbiff = Turtle(shape="square")
            rosbiff.penup()
            rosbiff.color("white")
            rosbiff.goto(position)
            self.segments.append(rosbiff)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg-1].xcor() #move to the x position of the front segment
            new_y = self.segments[seg-1].ycor() #move to the y position of the front segment
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)