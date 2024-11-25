from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Функция для чтения данных из YML-файла
def load_data_from_yml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    date = root.attrib["date"]  # Дата из атрибута yml_catalog
    offers = []

    # Парсим товары из секции <offer>
    for offer in root.find("shop").find("offers").findall("offer"):
        product = {
            "id": offer.attrib["id"],
            "name": offer.find("name").text,
            "stock_quantity": offer.find("stock_quantity").text,
        }
        offers.append(product)

    return date, offers

# Главная страница
@app.route("/")
def index():
    date, offers = load_data_from_yml("market.yml")
    return render_template("index.html", date=date, offers=offers)

if __name__ == "__main__":
    app.run(debug=True)
