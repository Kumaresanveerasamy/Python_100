from flask import Flask


app = Flask(__name__)

#Decorator Function:

def make_bold(func):
    def wrapper():
        return f"<b>{func()} </b>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return f" <u> {func()} </u>"
    return wrapper

@app.route("/")
def hello():
    return '<h1 style = "text-align: center"> Hello Viewer </h1> ' \
           ' <p> Welcome to flask Intro Page..</p> ' \
           '<img src = "https://media.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif" width=200>'


@app.route("/exit")
@make_bold
@make_underlined
def exit():
    return "Good Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hi {name}.. You are {number} years old.."

app.run(debug=True)