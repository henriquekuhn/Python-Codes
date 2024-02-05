

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(x_position, y_position)

    def go_up():
        if paddle.ycor() < 250:
            new_y = paddle.ycor() + 20
            paddle.goto(paddle.xcor(), new_y)    

    def go_down():
        if paddle.ycor() > -250:
            new_y = paddle.ycor() - 20
            paddle.goto(paddle.xcor(), new_y) 

    