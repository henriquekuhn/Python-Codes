from turtle import Turtle, Screen

rosbiff_the_turtle = Turtle()
screen =  Screen()


def move_forward():
    rosbiff_the_turtle.forward(10)    


def move_backward():
    rosbiff_the_turtle.backward(10)


def turn_left():
    rosbiff_the_turtle.left(10)


def turn_right():
    rosbiff_the_turtle.right(10)


def clear_all():
    rosbiff_the_turtle.home()
    rosbiff_the_turtle.clear

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_all, "c")
screen.exitonclick()
