import flask

app = flask.Flask(__name__)

users = ['user1', 'user2']
article = ['article1', 'article2']


@app.route("/")
def index():
    return "Hello World"


@app.route('/blog')
def welcome_user():
    return f"Hello {users}"


@app.route('/blog/article')
def display_article():
    return article


@app.route("/say_hi/<username>")
def say_hello(username):
    return f"""
    <html>
        <head>
            <title>
                Homepage - microblog
            </title>
        </head>
        <body>
            <h1>
                Hello, {username}
            </h1>
        </body>
    </html>
"""


if __name__ == "__main__":
    app.run(port=8080)