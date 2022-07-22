import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
game_is_on = True
states_of_50 = []
dialog = "Guess the State?"

while game_is_on == True:
    guess = screen.textinput(title= f"{dialog}", prompt="Enter another state..").title()

    if guess == "Exit":
        missed_states = []
        for state in data.state:
            if state not in states_of_50:
                missed_states.append(state)
        missed = pandas.DataFrame(missed_states)
        missed.to_csv("states_to_learn.csv")
        break

    for state in data["state"]:
        if guess == state:
            if guess not in states_of_50:
                states_of_50.append(guess)
            state_cor = data[data.state == guess]
            writer.goto(int(state_cor.x),int(state_cor.y))
            writer.write(f"{guess}",align="left", font=("Arial", 8, "normal"))
            dialog = f" {len(states_of_50)}/ 50 is correct"

        if len(states_of_50) == 50:
            game_is_on = False





