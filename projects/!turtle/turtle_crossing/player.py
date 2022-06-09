STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            return True
        return False
    
    def set_start_pos(self):
        self.setpos(STARTING_POSITION)
    
    def check_car_collision(self, cars):
        for x in cars:
            if self.distance(x) < 20:
                return True
        return False
    
