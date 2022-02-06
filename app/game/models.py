from app.ext.database import db
from datetime import datetime
from flask import current_app


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self):
        return self.word
