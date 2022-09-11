import flask
from random import randint

app = flask.Flask(__name__)

x = randint(0, 100)
print(x)


@app.route("/<number>")
def index(number):
    return flask.render_template("index.html", number=x, route_number=x)


if __name__ == "__main__":
    app.run()
