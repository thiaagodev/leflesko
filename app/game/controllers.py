from flask import Blueprint, current_app, request, jsonify
from .models import Word
from .serializers import WordSchema
from random import choice
from sqlalchemy import desc
from datetime import datetime

bp_word = Blueprint('word', __name__, url_prefix='/word')

@bp_word.route('/', methods=['GET'])
def word():
    schema = WordSchema()
    
    word = Word.query.order_by(desc(Word.created_at)).first()
    
    if not word:
       add_new_word()
    
    word = Word.query.order_by(desc(Word.created_at)).first()
    
    now = datetime.now().astimezone(current_app.timezone)
    current = word.created_at.astimezone(current_app.timezone)
    
    diff_time = now - current
    hours_diff = int(diff_time.total_seconds() / 3600)
    
    if hours_diff >= 24:
         add_new_word()
    
    word = Word.query.order_by(desc(Word.created_at)).first()

    return schema.jsonify(word), 200


def add_new_word():
    schema = WordSchema()
    with open('app/game/palavras.txt', 'r') as file:
            lines = file.readlines()
            word = choice(lines).strip()
            
            word = schema.load({'word': word})
            current_app.db.session.add(word)
            current_app.db.session.commit()
