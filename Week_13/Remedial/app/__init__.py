import flask

flask_app = flask.Flask(__name__)
flask_app.config['SECRET_KEY'] = "hht"

from app import routes
