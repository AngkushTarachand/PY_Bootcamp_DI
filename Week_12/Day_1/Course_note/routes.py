import flask

from app import flask_app
from app.forms import Login


@flask_app.route("/<name>")
def index(name):
    return flask.render_template('index.html', firstname=firstname)


@flask.app.route("/login", methods=("GET", "POST"))
def loginPage():
    login_form = Login()

    if login_form.validate_on_submit():
        firstName = login_form.first_name.data
        lastName = login_form.last_name.data
        age = login_form.age.data

        print(f"the first name is: {firstName}")
        print(f"the last name is: {lastName}")
        print(f"the age is{age}")

        return flask.redirect(flask.url_for("index", name=firstName))

    return flask.render_template("login.html", form=login_form)
