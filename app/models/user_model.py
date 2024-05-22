from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    roles=db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password, roles=["user"]):
        self.name = name
        self.email = email
        self.roles = json.dumps(roles)
        self.password = generate_password_hash(password)

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Esta funcion encuentra un usuario por su nombre de usuario
    @staticmethod
    def find_by_user(email):
        return User.query.filter_by(email=email).first()
    
    def update(self, name=None,email=None ,password=None, roles=None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if password_hash is not None:
            self.password = password
        if roles is not None:
            self.roles = json.dumps(roles)  # Convertir lista a cadena
        db.session.commit()
    
    # Elimina un dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()