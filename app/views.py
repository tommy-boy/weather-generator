from app import app
from flask import render_template, request
from models import Weather


@app.route('/', methods=['GET'])
def index():
	gen = Weather  # get an instance of the class
	narrative = gen.getForecast()
	today_hi, today_lo, weather_icon, threeday, weathericons, hilo = gen.getCurrent()
	weatherimg = app.config['IMGDIR'] + app.config['WEATHERIMG']
	return render_template('index.html', title='Index', narrative=narrative, weatherimg=weatherimg, today_hi=today_hi, today_lo=today_lo, weather_icon=weather_icon, threeday=threeday, weathericons=weathericons, hilo=hilo)

