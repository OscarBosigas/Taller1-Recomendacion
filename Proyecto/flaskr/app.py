from flaskr import create_app
from flask import jsonify
from .modelos import *
from .vistas import *
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for

app = create_app('default')
app_context = app.app_context()
app_context.push()


db.init_app(app)
db.create_all()

CORS = CORS(app)

api = Api(app)
api.add_resource(SignIn, '/api/auth/signup')
api.add_resource(LogIn, '/api/auth/login')
api.add_resource(Usuario, '/usuario')

jwt = JWTManager(app)

@app.route('/')
def index():
    return render_template('base.html')
