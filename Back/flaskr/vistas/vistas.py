from flask_restful import Resource
from flask import request,  request
from flask_jwt_extended import jwt_required, create_access_token
from ..modelos import *
from datetime import datetime

usaurioSchema = UsersSchema()

class SignIn(Resource):
    def post(self):
            nuevo_usuario = Users( 
                                  id=request.json["id"], 
                                  gender=request.json["gender"], 
                                  age = request.json["age"],
                                  country = request.json["country"],
                                  registered = request.json["registered"],
                                  password=request.json["password"])
            db.session.add(nuevo_usuario)
            print(nuevo_usuario)
            db.session.commit()
            return {'menaje':'Usuario creado'}
            
            
class LogIn(Resource):
    def post(self):
        u_user = request.json["id"]
        u_contrasena = request.json["password"]
        usuario = Users.query.filter_by(id=u_user, password=u_contrasena).first()
        token_de_Acceso = create_access_token(identity=request.json["id"])
        if usuario:
            return {'mensaje':'Inicio de sesion','token_de_acceso':token_de_Acceso}, 200
        else:
            return {'mensaje':'Usuario no encontrado'}, 400

class Usuario(Resource):
    def post(self):
        id = request.json["id"]
        return usaurioSchema.dump(Users.query.get_or_404(id))
        