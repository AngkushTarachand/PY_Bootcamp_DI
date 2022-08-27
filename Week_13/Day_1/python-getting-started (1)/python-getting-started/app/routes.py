import flask

from app import flask_app, db
from app.forms import Login, Register
from app.models import Users

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

		user = Users.query.filter_by(username=username).first()

		if user.password == password:
			return flask.redirect(flask.url_for("index", name=username))

		# check if there is a user with the provided username and password

	return flask.render_template("login.html", form=login_form)


@flask_app.route("/register", methods=['GET', 'POST'])
def registerPage():

	register_form = Register()
	if register_form.validate_on_submit():
		username = register_form.username.data
		password = register_form.password.data

		print(f"the username is: {username}")
		print(f"the password is: {password}")

		user = Users(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return flask.redirect(flask.url_for("loginPage"))

	return flask.render_template("register.html", form=register_form)
