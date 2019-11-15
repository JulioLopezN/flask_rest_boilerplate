from datetime import datetime
from app import db


class Todo(db.Model):
    __tablename__ = "todos"

    id_todo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    done = db.Column(db.Boolean, nullable=False, default=False)
