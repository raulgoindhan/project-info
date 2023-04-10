from flask import Blueprint, render_template
from . import db
from flask_login import login_required, login_user, logout_user, current_user

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

@views.route('/donations')
@login_required
def donations():
    return render_template('donations.html')

@views.route('/drop')
def drop():
    db.drop_all()
    return 'Dropped All'