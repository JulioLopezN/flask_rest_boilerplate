from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    roles = db.Column(db.String(50), nullable=False)
    reset_password_token = db.Column(db.String(50), nullable=True)
    reset_password_expire = db.Column(db.DateTime(50), nullable=True)