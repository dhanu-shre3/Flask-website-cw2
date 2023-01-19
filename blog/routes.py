from flask import Flask, render_template, url_for, redirect, request, Blueprint, flash
from blog import app
from . import db
from .models import Post, User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash




@app.route("/")

@app.route("/home") 
def home():
    return render_template('home.html', title='Home', user=current_user)

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

@app.route("/draft")
def draft():
    return render_template('draft.html', title='draft')    



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
                return redirect(url_for('create_post'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

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
            return redirect(url_for('create_post'))

    return render_template("signup.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("comment"))

@app.route("/comment")
def comment():
    posts = Post.query.all()
    return render_template("comment.html", user=current_user, post=posts)


@app.route("/create_post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Comment cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Comment created!', category='success')
            return redirect(url_for('comment'))

    return render_template('create_post.html', user=current_user)

@app.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Comment does not exist.", category='error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Comment deleted.', category='success')

    return redirect(url_for('comment'))

@app.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('comment'))

    posts = Post.query.filter_by(author=user.id).all()
    return render_template("comment.html", user=current_user, posts=posts, username=username)    