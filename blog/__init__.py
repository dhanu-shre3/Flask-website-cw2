from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


app = Flask(__name__)
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

from blog import routes