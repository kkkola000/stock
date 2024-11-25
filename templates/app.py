from flask import Flask, render_template_string
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Функция для чтения данных из YML-файла
def load_data_from_yml(file_path="market.yml"):
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

# Загрузка HTML-шаблона из файла
def load_template(file_path="index.html"):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Главная страница
@app.route("/")
def index():
    date, offers = load_data_from_yml()  # Загружаем данные из market.yml
    template = load_template()  # Загружаем HTML-шаблон
    return render_template_string(template, date=date, offers=offers)

if __name__ == "__main__":
    app.run(debug=True)
