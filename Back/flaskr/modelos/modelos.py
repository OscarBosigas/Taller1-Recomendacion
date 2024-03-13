from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from pydantic import BaseModel

class DataModel(BaseModel):
    iid: str
    uid: str

db = SQLAlchemy()

class Usuarios(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    gender = db.Column(db.String(64))
    age = db.Column(db.String(64))
    country = db.Column(db.String(64))
    registered =db.Column(db.String(64))
    password = db.Column(db.String(32))
    rate = db.Column(db.Integer)


class UsuariosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios
        include_relationships = True
        include_pk = True
        load_instance = True
