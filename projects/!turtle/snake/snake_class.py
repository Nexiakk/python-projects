from turtle import Turtle
from random import randint
class Snake:
    def __init__(self, startpos):
        self.body = []
        self.score = 0
        self.headings = {0: 180, 90: 270, 180: 0, 270: 90}
        for _ in range(2):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.speed(0)
            snake.setposition(startpos[0], startpos[1])
            self.body.append(snake)
            
    def move_snake(self):
        for x in range(len(self.body)-1, 0, -1):
            self.body[x].goto(self.body[x-1].xcor(), self.body[x-1].ycor())
        self.body[0].forward(20)
        
    def change_direction(self, direction):
        if direction == self.headings[self.body[0].heading()]:
            return
        
        self.body[0].setheading(direction)
        
    def check_food_distance(self, object):
        if self.body[0].distance(object.xcor(), object.ycor()) < 20:
            return True
        return False
    
    def check_wall_distance(self):
        if self.body[0].xcor() > 280 or self.body[0].xcor() < -280 or self.body[0].ycor() > 280 or self.body[0].ycor() < -280:
            return True
        return False
    
    def check_segment_distance(self):
        for x in range(1, len(self.body)):
            if self.body[0].distance(self.body[x].xcor(), self.body[x].ycor()) < 10:
                return True
        return False
    
    def add_segment(self):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.setposition(self.body[-1].xcor(), self.body[-1].ycor())
        self.body.append(segment)
        
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.setposition(randint(-280, 280), randint(-280, 280))
        
    def set_random_position(self):
        pos = (randint(-280, 280), randint(-280, 280))
        if pos[0] == self.xcor() and pos[1] == self.ycor():
            self.set_random_position()
        else:
            self.setposition(pos)
            
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.setposition(0, 0)
        self.color("white")
        self.write("PRESS SPACE TO START", align="center", font=("Courier", 15, "normal"))
        
    def display_score(self):
        self.clear()
        self.setposition(-290, 279)
        self.write("Score: 0", align="left", font=("Courier", 15, "normal"))
        
    def update_score(self, score):
        self.clear()
        self.write("Score: {}".format(score), align="left", font=("Courier", 15, "normal"))
        
    def game_over(self):
        self.setposition(0, 0)
        self.color("white")
        self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))
        