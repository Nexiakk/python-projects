import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""screen setup"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

"""core function"""
def main():
    """assign objects"""
    ply = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    
    def player_move():
        """
        Function that moves the player
        ply.move() returns True if the player has reached the finish line
        Then it resets cars and player position, increases the level and cars speed
        """
        if ply.move():
            car_manager.reset_cars()
            car_manager.speed_up_cars()
            scoreboard.lvl+=1
            scoreboard.update()
        screen.update()
        
    def reset_game():
        """
        Function that resets the game after car collide with player
        """
        car_manager.reset_game()
        scoreboard.lvl = 1
        scoreboard.update()
        ply.set_start_pos()
        
    screen.onkey(player_move, "Up")
    
    while True:
        """
        Main loop that spawns cars, moves them, checks if player collided with car
        """
        if car_manager.is_moving_allowed:
            car_manager.cooldown_counter+=1
            if car_manager.cooldown_counter >= car_manager.spawn_cooldown:
                car_manager.create_car()
                car_manager.cooldown_counter = 0
            car_manager.move_cars()
            
            if ply.check_car_collision(car_manager.cars):
                reset_game()
                
        time.sleep(0.1)
        screen.update()
        
main()
