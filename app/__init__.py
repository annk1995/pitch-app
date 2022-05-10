from flask import Flask
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from os import path
from flask_login import login_manager

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] ="okayokay"
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)




    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")


    return app