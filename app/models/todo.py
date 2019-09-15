from datetime import datetime
from app import db


class Todo(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    lastUpdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    done = db.Column(db.Boolean, nullable=False, default=False)
