from app.ext.database import db
from datetime import datetime
from flask import current_app
import pytz


class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now().astimezone(current_app.timezone))
    
    def __repr__(self):
        return self.letter
