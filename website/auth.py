from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("logout.html")


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
            flash("Password is too short.\nPassword must be more than 7 characters", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        else:
            flash("Account created successfully", category="success")

    return render_template("sigh-up.html")
