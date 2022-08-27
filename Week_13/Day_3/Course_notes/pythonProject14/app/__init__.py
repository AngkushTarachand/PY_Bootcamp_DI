import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

flask_app = flask.Flask(__name__)
flask_app.config.from_object(Config)

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes, models
