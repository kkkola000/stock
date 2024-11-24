from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для заказов
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Новый")

# Главная страница: список заказов
@app.route('/')
def index():
    orders = Order.query.all()
    return render_template('index.html', orders=orders)

# Добавление нового заказа
@app.route('/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        product = request.form['product']
        new_order = Order(customer_name=customer_name, product=product)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_order.html')

# Обновление статуса заказа
@app.route('/update/<int:order_id>', methods=['GET', 'POST'])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    if request.method == 'POST':
        order.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_order.html', order=order)

# Удаление заказа
@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()  # Создание базы данных
    app.run(debug=True)
