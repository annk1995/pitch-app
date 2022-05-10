from flask import Blueprint

auth = Blueprint("views",__name__)

@auth.route("/")
def login():
    return "login"

@auth.route("/signup")
def signup():
    return "signup"
    

@auth.route("/logout")
def logout():
    return "logout"
    