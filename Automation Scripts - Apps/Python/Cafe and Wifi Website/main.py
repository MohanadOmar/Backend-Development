import os
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import NewCafe, LoginForm, RegisterForm
from flask import Flask, render_template, redirect, url_for

# APP
app = Flask(__name__)
# CRFK
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# BOOTSTRAP
bootstrap = Bootstrap(app)
# DATABASS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    # Basics
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    map_url = db.Column(db.String(1000), unique=True, nullable=False)
    img_url = db.Column(db.String(1000), unique=True, nullable=False)
    location = db.Column(db.String(800), nullable=False)
    # Space
    restroom = db.Column(db.String(80), nullable=False)
    seats = db.Column(db.String(80), nullable=False)
    # Time
    opening_time = db.Column(db.String(80), nullable=False)
    closing_time = db.Column(db.String(80), nullable=False)
    # Productivity
    wifi = db.Column(db.String(80), nullable=False)
    sockets = db.Column(db.String(80), nullable=False)
    # Coffee
    coffee = db.Column(db.String(80), nullable=False)
    coffee_price = db.Column(db.String(80), nullable=False)
db.create_all()


@app.route('/')
def home():
    all_cafes = Cafe.query.all()
    return render_template("index.html", all_cafes=all_cafes)


@app.route('/add-cafe', methods=['GET', 'POST'])
def add_cafe():
    form = NewCafe()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            restroom=form.restroom.data,
            seats=form.seats.data,
            opening_time=form.opening_time.data,
            closing_time=form.closing_time.data,
            wifi=form.wifi.data,
            sockets=form.sockets.data,
            coffee=form.coffee.data,
            coffee_price=form.coffee_price.data
        )

        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add_cafe.html", form=form)


@app.route('/cafe-preview/<int:cafe_id>', methods=['GET', 'POST'])
def cafe_preview(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    return render_template("cafe_preview.html", cafe=cafe)


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template("register_page.html", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login_page.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)