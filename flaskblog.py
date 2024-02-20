from flask import Flask, render_template, url_for

app = Flask(__name__)


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
def hello_world():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(port=8000, debug=True)