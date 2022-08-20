import flask

flask_app = flask.Flask(__name__)
flask_app.config['SECRET_KEY'] = 'you-will-never-know'

from app import routes