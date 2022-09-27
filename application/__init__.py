from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from os import path

db = SQLAlchemy()
DB_NAME = 'atividades'
DB_HOST = 'mysql+pymysql://admin:123456789@meu-consultorio-app-mysql.ciofokjqok2t.us-east-1.rds.amazonaws.com:3306/atividades'

def create_app():
    from .product_user_model import User, Product
    from .views import views

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_HOST}'
    app.config['SECRET_KEY'] = 'secreet'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')


    create_database(app)
    
    return app


def create_database(app):
    db.create_all(app=app)
    print('Database On!')
    return('Database On!')