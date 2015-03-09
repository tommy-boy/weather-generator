from app import app
from flask import render_template, request
from models import Weather


@app.route('/', methods=['GET'], endpoint='/')
@app.route('/index', methods=['GET'])
def index():
	forecast = Weather  # get an instance of the class
	forecast.getForecast()
	forecast.getCurrent()
	weatherimg = app.config['IMGDIR'] + app.config['WEATHERIMG']
	return render_template('index.html', title='Index', weatherimg=weatherimg, forecast=forecast)

