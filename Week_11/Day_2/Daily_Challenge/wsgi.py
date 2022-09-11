import flask

flask_app = flask.Flask(__name__)


@flask_app.route('/exercises')
def exercises():
    text = None
    with open("/lesson1/exercises.md", mode='r') as file:
        text = file.read()
    return flask.render_template('index.html', exercise_text=text)


@flask_app.route('/lesson')
def lesson():
    text = None
    with open('lesson1/in-this-chapter.md', mode='r') as file:
        text = file.read()
    return flask.render_template('index.html', lesson_text=text)


if __name__ == "__main__":
    flask_app.run(debug=True)
