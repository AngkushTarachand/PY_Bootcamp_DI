import flask
app = flask.Flask(__name__)


@app.route("/")
def index():
    template = """
<html>
    <head>
        <title> Home page </title>
    </head>
    <body>
        hello World
    </body>
</html>    
    
"""
    return flask.render_template_string(template)


if __name__ == "__main__":
    app.run()
