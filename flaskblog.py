# flash => easy one time alerts
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# you should have the same case for secret key, otherwise you get runtime error
app.config["SECRET_KEY"] = "cbbfe3b99af3e90e17ceb78ed1c73a59"

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