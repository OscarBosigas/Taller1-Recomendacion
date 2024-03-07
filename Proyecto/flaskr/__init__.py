from flask import Flask
def create_app(config_name):
    app= Flask(__name__)
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS']=True
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://OscarBosigas:jATKoinQO6M1@ep-lucky-heart-a5uomq52.us-east-2.aws.neon.tech/Recomendacion?sslmode=require'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    return app