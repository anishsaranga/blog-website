# flash => easy one time alerts
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager # easy to manage user sessions

app = Flask(__name__)
# you should have the same case for secret key, otherwise you get runtime error
app.config["SECRET_KEY"] = "cbbfe3b99af3e90e17ceb78ed1c73a59"
# db connection to sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" # /// indicates relative path in sqllite

db = SQLAlchemy(app)
bcrypt = Bcrypt(app) # hashing passwords
login_manager = LoginManager(app) # manage user sessions
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flaskblog import routes
