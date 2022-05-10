from flask import Blueprint,render_template

auth = Blueprint("auth",__name__)

@auth.route("/")
def login():
    return "login"

@auth.route("/signup")
def sign_up():
    return "signup"
    

@auth.route("/logout")
def logout():
    return "logout"
    