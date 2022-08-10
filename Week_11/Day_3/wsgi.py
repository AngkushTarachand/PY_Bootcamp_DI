import flask

app = flask.Flask(__name__)

users = {"Laurent", "Ally", "Angkush", "Shivastav"}
book_dict = {"index": 1, "name": "Hello", "author": "JK"}


@app.route("/blog")
def blog():
    return flask.render_template("blog.html", users=users)


@app.route("/blog/articles")
def article():
    return flask.render_template("articles.html", articles=book_dict)


if __name__ == "__main__":
    app.run(port=8080)
