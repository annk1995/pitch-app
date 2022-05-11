from crypt import methods
from flask import Blueprint, flash,render_template,redirect,url_for,request,flash
from . import db
from .models import User

auth = Blueprint("auth",__name__)

@auth.route("login",methods=['GET','POST'])
def login():
    email =request.form.get("email")
    password=request.form.get("password")
    return render_template("login.html")

@auth.route("/sign_up",methods=['GET','POST'])
def sign_up():
    if request.method == 'POSTS':
     email =request.form.get("email")
     username =request.form.get("username")
     password1 =request.form.get("password1")
     password2=request.form.get("password2")


    
     email_exists = User.query.filter_by(email=email).first()
     username_exists =User.query.filter_by(username=username).first()
     if email_exists:
         flash('this email already exists', category ='error')
    elif username_exists:
         flash('username is already in use',category='error')
    elif password1!=password2:
         flash('password don\'t match!',category='error')
    elif len(username) < 2:
        flash('username is too short', category='error')
    elif len(password1)<6:
        flash('password is too short',category='error')
    elif len(email) < 4:
        flash('email is not valid',category='error')
    else:
     new_user =User(email=email,username=username,password=password1)
     db.session.add(new_user)
     db.session.commit()
     flash('user created')
     return redirect (url_for('views.home'))



     return render_template("signup.html")


     

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))
    
