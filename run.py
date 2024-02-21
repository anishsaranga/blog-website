from flaskblog import app


if __name__ == "__main__":
    # getting error for port 5000 on mac
    app.run(port=8000, debug=True)