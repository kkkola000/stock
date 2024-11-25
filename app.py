from flask import Flask, render_template, request
import yaml
import os
from datetime import datetime

app = Flask(__name__)

# Функция для загрузки данных из YML файла
def load_data():
    with open("data.yml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data

# Главная страница
@app.route("/")
def index():
    data = load_data()
    update_date = data["updated"]
    products = data["products"]
    return render_template("index.html", products=products, update_date=update_date)

if __name__ == "__main__":
    # Запуск сервера на localhost
    app.run(debug=True)
