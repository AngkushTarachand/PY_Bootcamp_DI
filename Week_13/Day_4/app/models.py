from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phonenumbers = db.relationship('Phone_number')


class Phone_number()
    id = id.Column(db.Integer, primary_key=True)
    number = id.Column(db.String)
    owner