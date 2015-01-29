from flask import request, render_template, session, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy

from __init__ import app

db= SQLAlchemy(app)
	
from models import *


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/test')
def test():
	return 'hello world'
