from models import User2
from __init__ import db

users=User2.query.all()

for user in users:
	user.is_admin=False
	db.session.commit()