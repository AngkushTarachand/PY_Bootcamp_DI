from app import db


class Human(db.Model):
    id = db.Column(db.Integer, primary_ley=True, autoincrement=True)
    name = db.Column(db.String(64))
    dogs = db.relationship('Dog', backref='human', lazy='dynamic')


class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    race = db.Column(db.String(64))
    master = db.Column(db.Integer, db.ForeignKey('human.id'))

