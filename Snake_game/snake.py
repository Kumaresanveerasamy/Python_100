from turtle import *
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0

class Snake:
    def __init__(self):

        self.turtles_all = []
        self.create_snake()
        self.head =self.turtles_all[0]

    def show_turtle(self):
        self.show_turtle()

    def create_snake(self):
        x = 0

        for n in range(3):
            tim = Turtle(shape="square")
            tim.penup()
            tim.color("white")
            tim.speed("fastest")
            self.turtles_all.append(tim)
            tim.goto(-x,0)
            x +=20


    def move(self):

        for n in range(len(self.turtles_all) - 1, 0, -1):
            old_position = self.turtles_all[n - 1].pos()
            self.turtles_all[n].goto(old_position)


        self.head.fd(20)


    def extend_snake(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        self.turtles_all.append(tim)


    def Up(self):
        if self.head.heading() != 270:
            self.head.seth(UP)

    def Down(self):
        if self.head.heading() != 90:
            self.head.seth(DOWN)

    def Left(self):
        if self.head.heading() != 0:
            self.head.seth(LEFT)

    def Right(self):
        if self.head.heading() != 180:
            self.head.seth(RIGHT)


