from app.ext.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    games = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)
    wins_sequence = db.Column(db.Integer, default=0)
    best_sequence = db.Column(db.Integer, default=0)
    
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return self.username
