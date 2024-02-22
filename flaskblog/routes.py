from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8") # hashing form password, decode utf-8 to generate hash in utf 8 format
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # storing hashed password
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created!", "success") # success is the bootstrap class
        return redirect(url_for("home")) # once validated, redirect to home page

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        # get user entered details
        user = User.query.filter_by(email=form.email.data).first()
        # check if user exists and password is matching
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login unsuccessful, please check email and password", "danger") # 2nd arg is bootstrap class
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")
