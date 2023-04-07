from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        pass

@auth.route('/logout')
def logout():
    pass

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        user = data.get('name')
        email = data.get('email')
        phone_number = data.get('phone')
        address = data.get('address')
        password = data.get('password')
        password2 = data.get('password2')
        isRest = data.get("yes_no_radio")

        

        if len(user) < 4:
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
            flash('account created', category='success')

        print(isRest)

    return render_template('register.html')



