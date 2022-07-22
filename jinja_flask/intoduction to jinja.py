import datetime
from flask import Flask,render_template
import random

app =Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(0,100)
    year_cprt = datetime.datetime.now().year
    return render_template("index.html",number=random_number,year= year_cprt)

if __name__ == "__main__":
    app.run(debug= True)