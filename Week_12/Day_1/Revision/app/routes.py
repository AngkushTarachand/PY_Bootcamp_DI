import flask

from app import flask_app

users = ['users1', 'users2', 'users3']


@flask_app.route("/<name>")
def index(name):
    return flask.render_template("index.html", firstname=name, users=users)


@flask_app.route("/login")
def login():
    return flask.render_template("login.html")


@flask_app.route("/register")
def register_page():
    return flask.render_template("register.html")
