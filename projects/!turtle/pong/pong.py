#imports
from turtle import Screen, mainloop, numinput
from pong_class import Paddle, Ball, Score, Notif
from time import sleep

# Screen setup
screen = Screen()
screen.title("Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

# Define Notify
notif = Notif()

# Ask for max score per player
max_score = numinput("Set max score", "Max score:",default=10,minval=1, maxval=100)

# Show start game notify
notif.show("PRESS SPACE TO START!")

# Main thread
def pong_core():
    notif.clear()
    
    # Define paddles
    paddle_a = Paddle([350,0])
    paddle_b = Paddle([-350,0])
    
    # Define ball
    ball = Ball()
    
    # Define scoreboard
    score = Score()
    
    # Manual screen update cuz of tracer(0) method
    screen.update()
    
    # Move paddle function
    def move_paddle(paddle, distance):
        paddle.move_paddle(distance=distance)
        screen.update()
        
    # Setup keyboard listener function
    def keys_setup():
        screen.onkeypress(lambda: move_paddle(paddle_a, 30), "Up")
        screen.onkeypress(lambda: move_paddle(paddle_a ,-30), "Down")
        screen.onkeypress(lambda: move_paddle(paddle_b, 30), "w")
        screen.onkeypress(lambda: move_paddle(paddle_b, -30), "s")
    keys_setup()
    
    # Reset game objects function
    def reset_after_score(player):
        notif.show("Player {} has scored!".format(player))
        sleep(3)
        paddle_a.reset_pos()
        paddle_b.reset_pos()
        ball.setpos(0,0)
        ball.random_move_distance()
        ball.move_speed = 0.07
        notif.clear()
        
    # Main loop
    while True:
        # Move ball
        ball.ball_move()
        
        # Check if ball hit top/bottom wall and bounce
        if ball.check_y_wall_collision():
            ball.bounce_y()
            
        # Check if ball hit left/right wall and give points
        if ball.check_x_wall_collision() == "1":
            score.score[0] +=1
            score.update_score()
            if score.score[0] == max_score:
                notif.show("Player 1 has won!", "green")
                break
            reset_after_score("1")
        elif ball.check_x_wall_collision() == "2":
            score.score[1] +=1
            score.update_score()
            if score.score[1] == max_score:
                notif.show("Player 2 has won!", "green")
                break
            reset_after_score("2")
            
        # Check if ball hit paddle and bounce
        if ball.check_paddle_collision(paddle_a=paddle_a, paddle_b=paddle_b):
            ball.bounce_x()
        
        # Update screen and wait for -0.08 seconds
        screen.update()
        sleep(ball.move_speed)

# Listen for i.a. space key to start
screen.listen()
screen.onkey(pong_core, "space")

# Main loop method so the program doesn't close
mainloop()