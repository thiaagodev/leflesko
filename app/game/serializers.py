from app.ext.serializer import ma
from marshmallow import ValidationError, validates
from .models import Word


class WordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Word
        load_instance = True
