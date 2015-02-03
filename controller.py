from flask import request, render_template, session, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import timedelta

from __init__ import app

db= SQLAlchemy(app)
	
from models import *


@app.route('/')
def index():
	post_query=Post2.query.order_by('id desc').all()
	return render_template('index.html',post_query=post_query)

@app.route('/write')
def write():
	if 'logged_in' in session:
		if session['logged_in']==True:
			return render_template('write.html')
		else:
			return redirect(url_for('login'))
	else:
		return redirect(url_for('index'))

@app.route('/write/check',methods=['POST'])
def write_check():
	post_title=request.form['title']
	post_body=request.form['text']
	user_query=User2.query.filter(User2.username==session['username']).first()
	p=Post2(user_query.id,post_title,post_body)
	db.session.add(p)
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/logout')
def logout():
	session['logged_in']=False
	session.pop('username',None)
	return redirect(url_for('index'))

@app.route('/login')
def login():
	if 'logged_in' in session:
		if session['logged_in']:
			return redirect(url_for('index'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/login/check',methods=['POST'])
def login_check():
	username=request.form['username']
	password=request.form['password']
	user_query=User2.query.filter(User2.username==username).first()
	if user_query:
		if user_query.check_password_hash(password):
			session['logged_in']=True
			session['username']=username
			return redirect(url_for('index'))
		else:
			return 'password wrong'
	else:
		return 'id wrong'

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signup/check',methods=['POST'])
def signup_check():
	username=request.form['username']
	password=request.form['password']
	email=request.form['email']
	user2=User2(username,password,email)
	db.session.add(user2)
	db.session.commit()
	return redirect(url_for('index'))


@app.before_request
def make_session_timeout():
	session.permanent=True
	app.permanent_session_lifetime=timedelta(minutes=5)