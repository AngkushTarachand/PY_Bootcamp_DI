import flask

from app import flask_app
from app.forms import Login

users = ["user1", "user2", "user3"]


@flask_app.route("/<name>")
def index(name):
	return flask.render_template("index.html", firstname=name, users=users)


@flask_app.route("/login", methods=("GET", "POST"))
def loginPage():
	login_form = Login()

	if login_form.validate_on_submit():
		username = login_form.username.data
		password = login_form.password.data

		print(f"the username is: {username}")
		print(f"the password is: {password}")

		# check if there is a user with the provided username and password

		return flask.redirect(flask.url_for("index", name=username))

	return flask.render_template("login.html", form=login_form)


@flask_app.route("/register")
def registerPage():
	return flask.render_template("register.html")
