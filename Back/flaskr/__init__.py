from flask import Flask
def create_app(config_name):
    app= Flask(__name__)
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS']=True
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://u2m45vs8bivl7h:p82765ac638851a2a57befbb9c6f734646e32b33794ade80ddb194b3b64ca7cda@ceu9lmqblp8t3q.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dcuqbml40smda4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    return app