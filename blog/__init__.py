from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail, Message



db = SQLAlchemy()
DB_NAME = "database.db"


app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dssummers2424@gmail.com'
app.config['MAIL_PASSWORD'] = 'trpxmsvwngtdhele'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


app.config['SECRET_KEY'] = '123456abba' 
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


from .models import User


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def create_database(app):
    if not path.exists("blog/" + DB_NAME):
        with app.app_context():
          db.create_all()
        print("Created database!")

create_database(app)

def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {name}", body=f" Name: {name}\n E-Mail: {email}\n\n\n{message}", sender=email, recipients=['dhanushree0424@gmail.com'])
        mail.send(msg)
        return render_template("contact.html", success=True)

    return render_template('contact.html', title='contact')    

 


from blog import routes
