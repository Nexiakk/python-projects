from turtle import Turtle
from random import choice
class Paddle(Turtle):
    def __init__(self, startpos=[350, 0]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(startpos)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.startpos = startpos
        
    def move_paddle(self, distance):
        self.setpos(self.xcor(), self.ycor() + distance)
        
    def reset_pos(self):
        self.setpos(self.startpos)
        
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setpos(0,0)
        self.left(45)
        self.move_distance = [10, 10]
        self.move_speed = 0.07
    
    def ball_move(self):
        self.setpos(self.xcor()+self.move_distance[0], self.ycor()+self.move_distance[1])
        
    def check_y_wall_collision(self):
        if self.ycor() < -280 or self.ycor() > 280:
            return True
        return False
    
    def check_x_wall_collision(self):
        if self.xcor() < -390:
            return "2"
        elif self.xcor() > 390:
            return "1"
        return False
    
    def check_paddle_collision(self, paddle_a, paddle_b):
        if self.xcor() < -320 and self.distance(paddle_b) < 50 or self.xcor() > 320 and self.distance(paddle_a) < 50:        
            return True
        return False
        
    def bounce_x(self):
        self.move_distance[0] = -self.move_distance[0]
        if self.move_speed > 0.03:
            self.move_speed -= 0.01

    def bounce_y(self):
        self.move_distance[1] = -self.move_distance[1]
        
    def random_move_distance(self):
        self.move_distance = [choice([-10,10]), choice([-10,10])]
        
        
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.color("white")
        self.score = [0,0]
        self.write("{} : {}".format(self.score[0], self.score[1]), align="center", font=("Courier", 20, "normal"))
        
    def update_score(self):
        self.clear()
        self.write("{} : {}".format(self.score[0], self.score[1]), align="center", font=("Courier", 20, "normal"))
        
class Notif(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(0, 0)
        self.color("white")
        
    def show(self, msg, color="white"):
        self.clear()
        self.color(color)
        self.write(msg, align="center", font=("Courier", 20, "normal"))
        