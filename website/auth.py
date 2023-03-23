from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sigh-up")
def register():
    return "<p>sigh-up</p>"