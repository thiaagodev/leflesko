from flask import Blueprint, current_app, request, jsonify
from .models import Word
from .serializers import WordSchema
from random import choice
from sqlalchemy import desc
from datetime import datetime
import requests


bp_word = Blueprint('word', __name__, url_prefix='/word')

@bp_word.route('/', methods=['GET'])
def word():
    schema = WordSchema()
    
    word = Word.query.order_by(desc(Word.created_at)).first()
    
    if not word:
       add_new_word()
    
    word = Word.query.order_by(desc(Word.created_at)).first()
    
    now = datetime.now().astimezone(current_app.timezone)
    last_word_date = word.created_at.astimezone(current_app.timezone)
    
    if now.day > last_word_date.day or now.month > last_word_date.month:
         add_new_word()
    
    word = Word.query.order_by(desc(Word.created_at)).first()

    return schema.jsonify(word), 200

@bp_word.route('/all', methods=['GET'])
def words():
    with open('app/game/palavras.txt', 'r') as file:
        lines = file.readlines()
    
    words = [word.strip() for word in lines]
    
    data = {
        'words': words
    }
    
    return jsonify(data), 200


def add_new_word():
    schema = WordSchema()
    with open('app/game/palavras.txt', 'r') as file:
        lines = file.readlines()
        
    while True:
        word = choice(lines).strip()
        request = requests.get(f'https://significado.herokuapp.com/{word.lower()}')
        data = request.json()
        
        if type(data) is list:
            data = data[0]
            
        if request.status_code == 200 and data['class'] != "":
            word = schema.load({'word': word})
            current_app.db.session.add(word)
            current_app.db.session.commit()
            
            return   
    
