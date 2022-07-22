from turtle import Turtle, Screen
from paddles import Paddles
from scoring import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.tracer(0)

paddles = Paddles()
screen.listen()

screen.onkey(paddles.up, "w")
screen.onkey(paddles.down, "s")
screen.onkey(paddles.up1, "Up")
screen.onkey(paddles.down1, "Down")

boundary = Turtle("circle")
boundary.hideturtle()
boundary.penup()
boundary.goto(-0, 350)
boundary.pensize(5)
boundary.color("white")
boundary.setheading(270)

ping = Ball()
score =Scoreboard()


for n in range(0, 700, 40):
    boundary.pendown()
    boundary.fd(20)
    boundary.penup()
    boundary.fd(20)

is_game_end = False

while is_game_end == False:
    screen.update()
    time.sleep(0.04)
    ping.move()

    if ping.quadrant2() == True:
        if ping.ball.ycor() >= 300:
            ping.ball.left(100)

    elif ping.quadrant4() == True:
        if ping.ball.ycor() <= -300:
            ping.ball.left(100)

    elif ping.quadrant1() == True:
        if ping.ball.ycor() >= 300:
            ping.ball.right(100)

    elif ping.quadrant3() == True:
        if ping.ball.ycor() <= -300:
            ping.ball.right(100)

    if ping.quadrant2() == True:
        if ping.ball.distance(paddles.paddles[0]) < 30:
            ping.ball.right(90)

    elif ping.quadrant4() == True:
        if ping.ball.distance(paddles.paddles[1]) < 30:
            ping.ball.right(90)

    elif ping.quadrant1() == True:
        if ping.ball.distance(paddles.paddles[1]) < 30:
            ping.ball.left(90)

    elif ping.quadrant3() == True:
        if ping.ball.distance(paddles.paddles[0]) < 30:
            ping.ball.left(90)

    if ping.ball.xcor() > 500:
        score.change_score(1)
        if score.check_score == "1":
            print(" Player 1 Wins ...")
            is_game_end = True
        else:
            ping.ball_reset()

    elif ping.ball.xcor() < -500:
        score.change_score(2)
        if score.check_score() == "2":
            print(" Player 2 Wins ...")
            is_game_end = True
        else:
            ping.ball_reset()




