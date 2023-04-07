from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdadasdad fafvsfsfs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .user import User
    from .admin import Admin
    from .shelters import Shelter

    from .views import views
    from .auth import auth

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')

    with app.app_context():
        db.create_all()
        db.session.commit()
    return app



