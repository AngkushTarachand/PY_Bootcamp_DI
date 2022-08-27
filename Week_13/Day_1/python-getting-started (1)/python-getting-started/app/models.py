from app import db


class Users(db.Model):
	username = db.Column(db.String(64), primary_key=True)
	password = db.Column(db.Integer)
