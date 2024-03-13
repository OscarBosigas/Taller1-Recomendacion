from flask_restful import Resource
from flask import request,  request, render_template, url_for
from flask_jwt_extended import create_access_token
from ..modelos import *
from datetime import datetime
from joblib import load
import pandas as pd
import json

usaurioSchema = UsuariosSchema()

class SignIn(Resource):
    def post(self):
            fecha_actual = datetime.now()
            formato_deseado = "%b %d, %Y"
            fecha_formateada = fecha_actual.strftime(formato_deseado)
            nuevo_usuario = Usuarios( 
                                  id=request.json["id"], 
                                  gender=request.json["gender"], 
                                  age = request.json["age"],
                                  country = request.json["country"],
                                  registered = fecha_formateada,
                                  password=request.json["password"])
            db.session.add(nuevo_usuario)
            db.session.commit()
            return {'menaje':'Usuario creado'}
            
            
class LogIn(Resource):
    def post(self):
        u_user = request.json["id"]
        u_contrasena = request.json["password"]
        usuario = Usuarios.query.filter_by(id=u_user, password=u_contrasena).first()
        token_de_Acceso = create_access_token(identity=request.json["id"])
        if usuario:
            return {'token:': token_de_Acceso}
        else:
            return {'mensaje':'Usuario no encontrado'}, 400

class Usuario(Resource):
    def post(self):
        id = request.json["id"]
        return usaurioSchema.dump(Usuarios.query.get_or_404(id))
        
class Predict(Resource):
    def post(self):
        df = pd.read_csv('modelos/predictions.csv')
        result = df.loc[df['userid'] == request.json['id']]
        return json.loads(result.to_json(orient='records'))