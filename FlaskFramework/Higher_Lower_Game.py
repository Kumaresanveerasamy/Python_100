from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1> Guess a number between 0 to 9 </h1>' \
           '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = randint(0,9)

@app.route('/<int:guess>')
def check(guess):
    if guess > random_number:
        return '<h1>Too high </h1> ' \
               '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess < random_number:
        return '<h1> Too low </h1> ' \
               '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess is random_number:
        return '<h1> You are Correct </h1>' \
               '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

app.run(debug =True)