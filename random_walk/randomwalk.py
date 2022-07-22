from turtle import *
from random import *

timmy = Turtle()
screen = Screen()

# def move_right():
#     timmy.right(90)
#     timmy.forward(50)
#
# def move_left():
#     timmy.left(90)
#     timmy.forward(50)
#
# def move_forward():
#     timmy.forward(50)
# timmy.pensize(5)
# colormode(255)
#
# while isTrue:
#     a = randint(0,10)
#     if a%2 == 0:
#         move_left()
#         timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
#
#     elif a%3 == 0:
#         move_right()
#         timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     else:
#         move_forward()
#         timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))

directions=[90,180,270,0,-90,-180,-270]
colormode(255)
timmy.pensize(5)
timmy.shape("circle")
timmy.speed("fastest")
for _ in range(100):
    timmy.fd(30)
    timmy.setheading(choice(directions))
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))




