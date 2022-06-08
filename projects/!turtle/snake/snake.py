from turtle import Screen, mainloop
from snake_class import Snake, Food, Score
from time import sleep

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

score = Score()
screen.update()

def snake_core():
    snake = Snake(startpos=[0, 0])
    food = Food()
    
    score.display_score()
    
    screen.onkey(None, "space")
    screen.onkey(lambda: snake.change_direction(180), "Left")
    screen.onkey(lambda: snake.change_direction(0), "Right")
    screen.onkey(lambda: snake.change_direction(90), "Up")
    screen.onkey(lambda: snake.change_direction(270), "Down")
    
    while True:
        score.update_score(snake.score)
        snake.move_snake()
        if snake.check_food_distance(food):
            snake.score += 1
            food.set_random_position()
            snake.add_segment()
            
        if snake.check_wall_distance():
            score.game_over()
            break
        
        if snake.check_segment_distance():
            score.game_over()
            break
        
        screen.update()
        sleep(0.1)
        
screen.onkey(snake_core, "space")

mainloop()