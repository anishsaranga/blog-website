# flash => easy one time alerts
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# you should have the same case for secret key, otherwise you get runtime error
app.config["SECRET_KEY"] = "cbbfe3b99af3e90e17ceb78ed1c73a59"
# db connection to sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" # /// indicates relative path in sqllite

db = SQLAlchemy(app)


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




posts = [
    {
        'author': 'Anish Saranga',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 13, 2024'
    },
    {
        'author': 'Love',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'February 14, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


# route to forms
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home")) # once validated, redirect to home page

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # admin login
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success") # 2nd arg is bootstrap class
            return redirect(url_for("home"))

        else:
            flash("Login unsuccessful, please check username and password", "danger") # 2nd arg is bootstrap class
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    # getting error for port 5000 on mac
    app.run(port=8000, debug=True)