import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
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
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.current_score()

    # Detect if the snake hit the wall
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
