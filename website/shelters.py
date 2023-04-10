from werkzeug.security import check_password_hash, generate_password_hash
from . import db


class Shelter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    shelter_name = db.Column(db.String, nullable = False)
    shelter_address = db.Column(db.String, nullable = False)
    shelter_contact = db.Column(db.Integer, nullable = False)
  
    def __init__(self, username, password, shelter_name, shelter_address, shelter_contact):
        self.username = username
        self.set_password(password)
        self.shelter_name = shelter_name
        self.shelter_address = shelter_address
        self.shelter_contact = shelter_contact

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'shelter_name': self.shelter_name,
            'shelter_address': self.shelter_address,
            'shelter_contact': self.shelter_contact,
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)