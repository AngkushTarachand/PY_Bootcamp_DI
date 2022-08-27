import flask
from app import flask_app, db
from app.models import Human, Dog


@flask_app.route("/")
def index():
    bob = Human(name='Bob')
    rex = Dog(name="Rex", race="Bulldog", human=bob)
    lacy = Dog(name="Lucy", race="Bulldog", human=bob)

    db.session.add_all([bob, rex, lacy])
    db.session.commit()

    return ""


@flask_app.route("/get_dog")
def get_dogs():
    bob = Human.query.filter_by(id='1').first()

    return flask.render_template('get_dog.html', dogs=bob.dogs)
