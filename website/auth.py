from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category="success")
                login_user(user,remember=True)

                return redirect(url_for('view.home'))
            else:
                flash("Incorrect password", category='error')
        else:
            flash("Email not exsist", category='error')
    return render_template("login.html",user = current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("logout.html",user = current_user)


@auth.route("/sigh-up", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        firstName = data.get("firstName")
        password1 = data.get("password1")
        password2 = data.get("password2")
        if len(email) < 4:
            flash("Email address must be more than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("First name must be more than 1 characters", category="error")
        elif len(password1) < 7:
            flash(
                "Password is too short.\nPassword must be more than 7 characters", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        else:

            if User.query.filter_by(email=email).first():
                flash("User is already exsisted", category="error")
                return render_template("sigh-up.html")

            new_user = User(email=email, password=generate_password_hash(
                password1, method="sha256"), first_name=firstName)
            login_user(new_user)
            db.session.add(new_user)
            db.session.commit()

            flash("Account created successfully", category="success")
            return redirect(url_for('view.home'))

    return render_template("sigh-up.html",user = current_user)
