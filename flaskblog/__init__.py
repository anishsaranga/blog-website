# flash => easy one time alerts
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# you should have the same case for secret key, otherwise you get runtime error
app.config["SECRET_KEY"] = "cbbfe3b99af3e90e17ceb78ed1c73a59"
# db connection to sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" # /// indicates relative path in sqllite

db = SQLAlchemy(app)

from flaskblog import routes
