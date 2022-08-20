import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/say_hi")
def say_hi():
    return "Hi there"


@app.route("/say_hello/<username>")
def say_hello(username):
    return f"Hi {username}"


if __name__ == "__main__":
    app.run(port=8080)
