"""Python Flask Server"""

from flask import render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from app import db, app
import json
import crud
import openweathermap

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """This is going to be our homepage"""

    return render_template('homepage.html', )

@app.route("/users", methods=["POST"])
def register_new_user():
    """Creates a new user in our DB"""
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.find_user_by_email(email)

    if user:
        flash("Email is already in use. Please try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account has successfully been created.")

    return redirect("/")

@app.route("/login", methods=["POST"])
def login_user():
    """Processes the user login via manual credentials."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.find_user_by_email(email)

    if not user or user.password != password:
        flash("Your credentials seem to be incorrect. Please try again.")
    else:
        session['email'] = user.email
        flash(f"Welcome back, {user.email}")

    return redirect('/')

@app.route("/logout", methods=["POST"])
def logout_user():

    session.pop('email', None)

    return redirect('/')

@app.route("/weather", methods=["POST"])
def get_weather():
   
   data = request.json


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)