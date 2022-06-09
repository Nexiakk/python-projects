COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
from random import choice, randint
class CarManager():
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.is_moving_allowed = True
        self.spawn_cooldown = 6
        self.cooldown_counter = 0
        
    def create_car(self):
        car = Turtle("square")
        car.shapesize(1,2)
        car.setpos(300, randint(-250, 250))
        car.color(choice(COLORS))
        car.penup()
        car.setheading(180)
        self.cars.append(car)
        car = None
        
    def move_cars(self):
        for x in self.cars:
            x.forward(self.move_distance)
            if x.xcor() < -300:
                self.cars.remove(x)
                x.hideturtle()
                x = None
                
    def reset_cars(self):
        self.is_moving_allowed = False
        for x in self.cars:
            x.hideturtle()
            x = None
        self.cars = []
        self.is_moving_allowed = True
            
    def speed_up_cars(self):
        self.move_distance+=MOVE_INCREMENT
        
    def reset_game(self):
        self.is_moving_allowed = False
        self.move_distance = STARTING_MOVE_DISTANCE
        for x in self.cars:
            x.hideturtle()
            x = None
        self.cars = []
        self.is_moving_allowed = True
