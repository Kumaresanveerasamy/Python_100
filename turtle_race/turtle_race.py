from random import *
from turtle import *

screen = Screen()

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtles = []
n=0

for n in range(6):
    turtles.append(Turtle())
    n +=1


m = 0
y = -100

for m in range(6):
    turtles[m].shape("turtle")
    turtles[m].penup()
    turtles[m].goto(-300, y)
    turtles[m].color(colors[m])
    m = + 1
    y += 50

user_guess = screen.textinput(title="Welcome to Turtle Race..", prompt="Make your bet , Which turtle wins the race ?..")

def racing(k):
    f_value = randint(0,15)
    turtles[k].fd(f_value)

def checking(k):
    end = turtles[k].pos()
    if end[0] >= 350:
        return turtles[k]
    else:
        pass
k = 0
is_game_end = False

while is_game_end == False:
    for k in range(6):
        racing(k)
        check = checking(k)
        if check in turtles:
            is_game_end = True
            winner = check.color()[0]
            if winner == user_guess.lower():
                print(" Congrats .. You Won..")
            else:
                print(f"Sorry.. The winner is {winner}...")
        else:
            pass

        k += 1


screen.exitonclick()