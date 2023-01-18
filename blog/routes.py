from flask import Flask, render_template, url_for, redirect, request, Blueprint, flash
from blog import app
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash




@app.route("/")

@app.route("/home") 
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')    

@app.route("/portfolio") 
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog')    

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title='contact')    


@app.route("/blogpost1")
# @login_required
def blogpost1():
    return render_template('blogpost1.html',  title='BlogPost')    

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user='current_user')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('blogpost1'))

    return render_template("signup.html", user='current_user')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("blogpost1"))