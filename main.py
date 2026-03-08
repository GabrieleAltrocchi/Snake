from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game!")
"""It is like freezing the screen until we re-activate it with screen.update"""
screen.tracer(0)

snake = Snake()
snake_food = Food()
snake_score = Scoreboard()
game_speed = 0.1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    """Snake grows when eats food"""
    while snake.head.distance(snake_food) < 15:
        snake_food.refresh()
        snake_score.increase_score()
        snake.extend()
        game_speed *= 1 #This is to change speed (turn to 0.9 to increase speed a bit for every food eaten)

    """Game over when snake collides with walls"""
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake_score.reset()
        snake.reset()

    """Game over when snake collides with its own tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake_score.reset()
            snake.reset()

screen.exitonclick()
