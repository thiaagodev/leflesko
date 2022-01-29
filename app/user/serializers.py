from app.ext.serializer import ma
from marshmallow import ValidationError, validates
from .models import User


class CreateUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
    
    @validates('username')
    def validate_username(self, value):
        user = User.query.filter_by(username=value).first()
        
        if user:
            raise ValidationError('Username already exists!')

