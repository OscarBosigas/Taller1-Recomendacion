from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    gender = db.Column(db.String(64))
    age = db.Column(db.String(64))
    country = db.Column(db.String(64))
    registered =db.Column(db.String(64))
    password = db.Column(db.String(32))


class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        include_pk = True
        load_instance = True