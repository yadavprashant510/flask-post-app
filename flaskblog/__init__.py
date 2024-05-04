from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '4e10bb420e7fe20190a0e99f35d55a25'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define a function to initialize the database


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes  # noqa


def initialize_database():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")


# Call the function to initialize the database
initialize_database()
