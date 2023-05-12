from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

#this incripts our passwords
from werkzeug.security import generate_password_hash, check_password_hash

# import secrets mudule (from python) generate a token for each user
import secrets

# import flask login to check for an aruthentication user and store
# from flask_login import UserMixin, LoginManager

# from flask_marshmallow import Marshmallow

db = SQLAlchemy()
# login_manager = LoginManager()
# ma = Marshmallow()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

class User(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    username = db.Column(db.String(150), nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # remeber to add the artist relationship

    def __init__(self, email, username, first_name = '', last_name = '',id='',password = '', token=''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        print(self.pw_hash)
        return self.pw_hash

    def __repr__(self):
        return f"User {self.email} has been added to the database! wooo"
    
