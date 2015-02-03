from controller import db
from __init__ import bcrypt


class Base(db.Model):
	__abstract__=True
	id=db.Column(db.Integer,primary_key=True)


class User2(Base):
	__tablename__= 'user2'

	username= db.Column(db.String(), unique=True, nullable=False)
	password= db.Column(db.String(), nullable=False)
	email= db.Column(db.String(), unique=True)
	posts=db.relationship('Post2',backref='author',lazy='dynamic')
	is_admin=db.Column(db.Boolean, default=False)
	is_active=db.Column(db.Boolean, default=False)

	def __init__(self, username, password, email):
		self.username=username
		self.password=bcrypt.generate_password_hash(password=password)
		self.email=email

	def check_password_hash(self,password):
		if bcrypt.check_password_hash(pw_hash=self.password,password=password):
			return True
		else:
			return False

	def __repr__(self):
		return "<E-mail %s>" % self.email


class Post2(Base):
	__tablename__='post2'

	title=db.Column(db.String(64))
	body=db.Column(db.Text)
	user_id=db.Column(db.Integer,db.ForeignKey('user2.id'))

	def __init__(self,user_id,title,body):
		self.user_id=user_id
		self.title=title
		self.body=body
		
