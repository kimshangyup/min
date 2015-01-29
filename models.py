from controller import db


class User(db.Model):
	__tablename__= 'users'

	id= db.Column(db.Integer, primary_key=True)
	username= db.Column(db.String(), unique=True, nullable=False)
	password= db.Column(db.String(), nullable=False)
	email= db.Column(db.String(), unique=True)

	def __init__(self, username, password, email):
		self.username=username
		self.password=password
		self.email=email

	def __repr__(self):
		return "<E-mail %s>" % self.email