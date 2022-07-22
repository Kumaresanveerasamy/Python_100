from turtle import *
from random import *

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.fd(10)

def move_backwards():
    timmy.bk(10)

def turn_clockwise():
    timmy.right(10)
    timmy.fd(10)

def turn_counterclockwise():
    timmy.left(10)
    timmy.fd(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()