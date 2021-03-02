from application import db
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length

class Character(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    character_race = db.Column(db.String(20), nullable=False)
    character_class = db.Column(db.String(20), nullable=False)
    character_trait =  db.Column(db.String(250), nullable=False)