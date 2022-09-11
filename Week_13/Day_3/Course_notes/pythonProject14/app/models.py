from app import db

human_dog_table = db.Table('dogs',
                           db.Column('human_id', db.Integer, db.ForeignKey('human.id')),
                           db.Column('dog_id', db.Integer, db.ForeignKey('dog.id')
                                     ))


class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    dogs = db.relationship('Dog', secondary=human_dog_table, back_populates="humans")


class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    race = db.Column(db.String(64))
    humans = db.relationship('Human', secondary=human_dog_table, back_populates="dogs")
