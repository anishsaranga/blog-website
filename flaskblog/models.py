from flaskblog import db
from datetime import datetime


"""
    DB MODELS
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False) # 60 chars hashed values
    posts = db.relationship("Post", backref="author", lazy=True) ## backref is just like adding a new column in the post table
          # referencing 'Post' class here, that's why capital P    # lazy true means, sqlalchemy loads data when necessary
    # dunder / magic methods
    # how our obj is printed when we print it out
    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file})"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # default current time; no paranthesis, because we want to pass function and not current time
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False) ## foreign key
    # referencing the table user, therefore small u


    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"