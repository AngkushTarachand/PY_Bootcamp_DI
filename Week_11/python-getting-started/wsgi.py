import flask

app = flask.Flask(__name__)

users = ["user1", "user2", "user3"]


@app.route("/<name>")
def index(name):
	return flask.render_template("index.html", firstname=name, users=users)


@app.route("/login")
def loginPage():
	return flask.render_template("login.html")

@app.route("/register")
def registerPage():
	return flask.render_template("register.html")


if __name__ == "__main__":
	app.run()
