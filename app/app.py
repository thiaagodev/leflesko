from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from app.ext import database, serializer
from dotenv import load_dotenv
import os
import pytz

from app.user.controllers import bp_users
from app.game.controllers import bp_word


load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    app.timezone = pytz.timezone('Etc/GMT+3')
    
    database.init_app(app)
    serializer.init_app(app)
    
    Migrate(app, app.db)
    JWTManager(app)
    
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_word)
    
    return app
