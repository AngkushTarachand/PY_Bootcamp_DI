import flask
import datetime
from app import flask_app


@flask_app.route("/greet")
def index():
    x = datetime.datetime.now()
    hour = x.hour
    print(hour)
    print(type(hour))

    def greet():
        if 8 > hour > 13:
            msg = "Good Morning"
        elif 13 > hour > 17:
            msg = "Good Afternoon"
        elif 17 > hour > 21:
            msg = "Good evening"
        elif hour > 21 or hour < 8:
            msg = "Good night"

    return flask.render_template("index.html", msg=greet())
