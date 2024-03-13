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
                                  password=request.json["password"],
                                  rate = 0)
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

def calculate_distance(user1, user2):
    gender_distance = 1 if user1['gender'] != user2['gender'] else 0
    country_distance = 7 if user1['country'] != user2['country'] else 0
    age_distance = abs(int(user1['age']) - int(user2['age']))
    return gender_distance + country_distance + age_distance

class Predict(Resource):
    def post(self):
        df1 = pd.read_csv('modelos/predictions.csv')
        result = df1.loc[df1['userid'] == request.json['id']]
        if(len(result) == 0):
            df = pd.read_csv('modelos/userid-profile.tsv', sep='\t', skiprows = 1, on_bad_lines='skip',header = None,names = ["id","gender","age","country","registered"])
            df['age'] = df['age'].fillna(0).astype(int)
            min_distance = float('inf')
            closest_user = None
            id = request.json["id"]
            usuario = usaurioSchema.dump(Usuarios.query.get_or_404(id))
            for _, row in df.iterrows():
                distance = calculate_distance(usuario, row)
                if distance < min_distance:
                    min_distance = distance
                    closest_user = row
                    closest_user =closest_user["id"]
                    result = df1.loc[df1['userid'] == closest_user]
        return json.loads(result.to_json(orient='records'))

    
class Calificar(Resource):
    def post(self):
        usuario = Usuarios.query.get_or_404(request.json["id"])
        data = request.get_json()
        usuario.rate = data['rate']
        db.session.commit()
        return {'mensaje':'Calificado'}