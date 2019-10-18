from config import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(191), unique=False)
    email = db.Column(db.String(191), unique=True, nullable=False)
    role = db.Column(db.String(191))
    phone = db.Column(db.String(191))
    isAdmin = db.Column(db.String(191), nullable=True)
    password = db.Column(db.String(191), nullable=False)
    verifyToken = db.Column(db.String(191), nullable=True)
    status = db.Column(db.Boolean, nullable=True)
    image = db.Column(db.String(191), nullable=False, default='default.jpg')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email):
        self.username = username
        self.email = email
