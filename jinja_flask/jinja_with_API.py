from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/<name>")
def challenge(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = gender_response["gender"]

    age_response = requests.get(f"https://api.agify.io?name={name}").json()
    age = age_response["age"]

    nationality_response = requests.get(f"https://api.nationalize.io?name={name}").json()
    country = nationality_response["country"][0]["country_id"]

    return render_template("challenge.html", person = name,sex=gender, lifespan=age, con=country)


if __name__ == "__main__":
    app.run(debug=True)

