from turtle import Screen
from Ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

SPEED = 0.1
l_paddle = Paddle(-470, 0)
r_paddle = Paddle(470, 0)
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_om = True
while game_is_om:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 450 or ball.distance(l_paddle) < 50 and ball.xcor() < -450:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 480:
        ball.refresh()
        scoreboard.l_point()
    # detect when left paddle misses
    if ball.xcor() < -480:
        ball.refresh()
        scoreboard.r_point()
screen.exitonclick()
