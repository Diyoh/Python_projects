import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Shiloh's snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 296 or snake.head.xcor() < -296 or snake.head.ycor() > 280 or snake.head.ycor() < -296:
        scoreboard.reduce_lives()
        if scoreboard.lives == 0:
            game_is_on = False
        scoreboard.reset_score()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reduce_lives()
            if scoreboard.lives == 0:
                game_is_on = False
            scoreboard.reset_score()
            snake.reset_snake()

    # if head collides with any segment in the tail trigger game_ov
turtle.write("GAME OVER", True,  align="center", font="Poppins")
screen.exitonclick()
