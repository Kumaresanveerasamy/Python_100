from turtle import *
from random import *

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("red")

# for x in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for x in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
n=3

for x in range(7):
    colormode(255)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))

    for y in range(n):
        timmy.fd(100)
        timmy.rt(360/n)
    n+=1

screen.exitonclick()