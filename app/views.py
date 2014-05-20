from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html')

@app.route('/')
@app.route('/why_steam')
def index():
	return render_template('why_steam.html')

@app.route('/')
@app.route('/code_camps')
def index():
	return render_template('code_camps.html')