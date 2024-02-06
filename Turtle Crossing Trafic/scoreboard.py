from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMNENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)

    def colision(self):
        self.write("GAME OVER!", align=ALIGNMNENT, font=FONT)
        return False
    
    def victory(self):
        self.write("VICTORY!", align=ALIGNMNENT, font=FONT)
        return False