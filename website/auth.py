from flask import Blueprint, render_template, request, flash, redirect, url_for
from .user import User
from . import views
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user.check_password(password):
            flash('Logged in successfully!', category='success')
            redirect(url_for('views.home'))
        else:
            flash('Incorrect password', category='error')
    else:
        flash('email does not exist', category='error')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    pass

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        phone_number = data.get('phone')
        address = data.get('address')
        password = data.get('password')
        password2 = data.get('password2')
        isRest = data.get("yes_no_radio")

        user_account = User.query.filter_by(email=email).first()

        if user_account:
            flash('This email is already in use', category='error')
        elif len(name) < 4:
            flash('name should be greater than 4 characters', category='error')
        elif password != password2:
            flash('passwords entered are not the same', category='error')
        elif len(password) < 5:
            flash('password should be greater than 5 characters', category='error')
        # elif len(phone_number > 11):
        #     flash('enter a proper telephone number', category="error")
        # elif len(phone_number < 7):
        #     flash('enter a proper telephone number', category="error")
        else:
            if isRest == 'resturant':
                rest = True
            else:
                rest = False

            user =  User(name=name, email=email, password=password, phone_number=phone_number, address=address, is_resturant=rest)

            db.session.add(user)
            db.session.commit()

            flash('account created', category='success')
            return redirect(url_for('views.home'))
            
        

    return render_template('register.html')



