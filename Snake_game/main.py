5from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Adventure")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

is_game_end = False
while is_game_end == False:

    snake.move()
    screen.update()
    time.sleep(0.2)

    if snake.head.distance(food) < 20:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.change_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_end = True
        scoreboard.game_over()

    for turtle in snake.turtles_all:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle) < 10:
            is_game_end = True
            scoreboard.game_over()



















screen.exitonclick()