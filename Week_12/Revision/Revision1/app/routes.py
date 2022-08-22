import flask

from app import flask_app


@flask_app.route("/")
def index():
    return flask.render_template("index.html")


# @flask_app.route("/login")
# def login_page():
#     return flask.render_template("login.html")
#
#
# @flask_app.route("/register")
# def register_page():
#     return flask.render_template("register.html")
