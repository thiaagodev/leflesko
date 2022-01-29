from flask import Blueprint, current_app, request, jsonify
from marshmallow import ValidationError
from .models import User
from .serializers import CreateUserSchema

bp_users = Blueprint('users', __name__, url_prefix='/users')


@bp_users.route('/', methods=['POST'])
def create_user():
    schema = CreateUserSchema()
    
    try:
        user = schema.load(request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400
    
    current_app.db.session.add(user)
    current_app.db.session.commit()
    
    return schema.jsonify(user), 201

