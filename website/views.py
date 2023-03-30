from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/faq')
def faq():
    return render_template('FAQ.html')

@views.route('/shelters')
def shelters():
    return render_template('shelters.html')