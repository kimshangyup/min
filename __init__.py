from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_migrate import Manager, Migrate, MigrateCommand


app=Flask(__name__)




bcrypt=Bcrypt(app)
app.secret_key='\xe98\xd4[\xd4\x01\xd9)\xfb\x11F\xb6\xe8\xd2\xed\xc2\x94\xc8\xf4W5\xd8;\x89'
app.config['SQLALCHEMY_ECHO']=True
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://ubuntu:sy1120@localhost/ubuntu'
#WARNING : change p.rogramming to your psql password
#manager=Manager(app)
#migrate=Migrate(app,db)

#manager.add_command('db',MigrateCommand)

from controller import *


