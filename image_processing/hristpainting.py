import random
import turtle
from main import color_list
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape("circle")
timmy.speed("fastest")
timmy.pensize(10)
turtle.colormode(255)
y=-200
x=-200
for _ in range(10):

    for _ in range(10):
        timmy.pencolor(random.choice(color_list))
        timmy.penup()
        timmy.goto(x, y)
        timmy.pendown()
        timmy.dot(20)
        x+=50

    y+=50
    x=-200


screen.exitonclick()