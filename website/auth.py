from flask import Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/sigh-up")
def register():
    return render_template("sigh-up.html")