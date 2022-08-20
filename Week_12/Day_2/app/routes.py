import flask

from app import flask_app
from app.forms import Login

@flask_app.route("/")
def index:
    return flask.render_template("index.html")

@flask_app.route("/login", method=("GET", "POST"))
def login():
    login_form = Login()

    if login_form.validate_on_submit():
        first_name = login_form.first_name.data
        last_name = login_form.last_name.data
        experience = login_form.experience.data
        education = login_form.education.data
        language = login_form.language.data

        print(f"the first name is {first_name}")
        print(f"the last name is {last_name}")
        print(f"the experience is {experience}")
        print(f"the education is {education}")
        print(f"the language is {language}")

        return flask.redirect("login.html", form=login_form)

@flask_app.route("/register")
def register_page():
    return flask.render_template("register.html")

