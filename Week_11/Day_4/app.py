import flask

app = flask.Flask(__name__)


@app.route("/homepage")
def homepage():
    return flask.render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)