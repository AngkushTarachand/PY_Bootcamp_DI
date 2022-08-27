import flask

from app import flask_app, db
from app.models import Human, Dog


@flask_app.route('/')
def index():
	bob = Human(name='Bob')
	alice = Human(name='Alice')
	rex = Dog(name='Rex', race='Bulldog', humans=[bob, alice])
	lacy = Dog(name='Lacy', race='Bulldog', humans=[bob])

	# db.session.add(bob)
	# db.session.add(rex)
	# db.session.add(lacy)

	db.session.add_all([bob, alice, rex, lacy])
	db.session.commit()

	return "added successfully to the database"


@flask_app.route("/get_dog")
def get_dogs():
	bob = Human.query.filter_by(id='2').first()

	return flask.render_template('get_dog.html', dogs=bob.dogs)
