import flask

app = flask.Flask(__name__)

users = ['bob', 'alice']
articles_list = ['article1', 'article2']


@app.route("/blog")
def blog(user):
    return flask.render_template("blog.html", user_name=users)


@app.route("/blog/articles")
def articles():
    return "articles"


if __name__ == "__main__":
    app.run()
