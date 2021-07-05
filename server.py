from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

name = "chris"

agyfi_data = requests.get(f"https://api.agify.io/?name={name}")
agyfi_content = agyfi_data.json()
age = agyfi_content["age"]

genderize_data = requests.get(f"https://api.genderize.io/?name={name}")
genderize_content = genderize_data.json()
gender = genderize_content["gender"]


@app.route('/')
def home():
    current_year = datetime.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year, name=name)


@app.route('/guess/<name>')
def guess(name):
    return render_template("guess.html", name=name, gender=gender, years_old=age)


if __name__ == "__main__":
    app.run(debug=True)
