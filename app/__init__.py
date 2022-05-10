from flask import Flask
from flask_sqlalchemy import sqlalchemy
from os import path
from flask_login import login_manager

def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] ="okayokay"

    from .views import views
    app.register_blueprint(views,url_prefix="/")

    return app