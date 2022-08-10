import flask

app = flask.Flask(__name__)


@app.route("/home")
def homepage():
    return flask.render_template("homepage.html")


@app.route("/blog/articles")
def articles():
    return flask.render_template("articles.html")


@app.route("/blog/profile")
def profile():
    return flask.redirect(flask.url_for('homepage'))


if __name__ == "__main__":
    app.run()
