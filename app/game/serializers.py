from app.ext.serializer import ma
from marshmallow import ValidationError, validates
from .models import Letter


class LetterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Letter
        load_instance = True
