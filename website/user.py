from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String, nullable=False)
    is_resturant = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, email, password, phone_number, address, is_resturant):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.is_resturant = is_resturant
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)