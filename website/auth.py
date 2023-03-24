from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route("/login",methods =['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    data = request.form
    return render_template("logout.html")

@auth.route("/sigh-up",methods =['GET','POST'])
def register():
    return render_template("sigh-up.html")