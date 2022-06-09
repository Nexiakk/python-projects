FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-290, 265)
        self.color("white")
        self.lvl = 1
        self.write("Lvl: {}".format(self.lvl), font=FONT)
    
    def update(self):
        self.clear()
        self.write("Lvl: {}".format(self.lvl), font=FONT)