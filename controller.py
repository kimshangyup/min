#-*- coding:utf-8 -*-

from flask import request, render_template, session, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import timedelta
import requests
from itsdangerous import URLSafeSerializer

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
			if user_query.is_active==True:
				session['logged_in']=True
				session['username']=username
				if user_query.is_admin:
					session['is_admin']=True
				else:
					session['is_admin']=False
			else:
				return u'메일 인증 먼저 하세요'
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
	send_simple_message(username=username,email=email)
	return redirect(url_for('index'))


@app.route('/admin')
def admin_page():
	if 'is_admin' in session and session['is_admin']:
		return 'Admin'
	else:
		return 'User'



@app.route('/activate/<hash_value>')
def activate(hash_value):
	s=URLSafeSerializer(app.config.get('SECRET_KEY'))
	a=s.loads(hash_value)
	user_query=User2.query.filter(User2.email==a).first()
	user_query.is_active=True
	db.session.add(user_query)
	db.session.commit()
	return u'인증이 완료되었습니다'

@app.before_request
def make_session_timeout():
	session.permanent=True
	app.permanent_session_lifetime=timedelta(minutes=5)

def send_simple_message(username,email):
	s=URLSafeSerializer(app.config.get('SECRET_KEY'))
	hash_value=s.dumps(email)
	return requests.post(
		"https://api.mailgun.net/v2/sandbox79e52ac751eb4923ba69abb7fa180171.mailgun.org/messages",
		auth=("api", "key-c6b7a97cf8c37a902f6ebd8e85edfa65"),
		data={"from": "no-reply <no-reply@no-reply.com>",
			u"to": username+u"<"+email+u">",
			"subject": "Hello",
			"text": "http://54.64.200.183:5000/activate/"+hash_value})


