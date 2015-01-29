from flask import Flask

app=Flask(__name__)
app.secret_key='asdfasdff'
app.config['SQLALCHEMY_ECHO']=True
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://ubuntu:p.rogramming@localhost/ubuntu'
#WARNING : change p.rogramming to your psql password

from controller import *

