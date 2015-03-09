from app import app
from flask import render_template
import requests
import json
import re
from collections import OrderedDict
from datetime import datetime


class Weather(object):

	@classmethod
	def getForecast(self):
	    article_json = app.config['ARTICLE_JSON']
	    data = requests.get(str(article_json))
	    if data.status_code == 200:
	    	content = ''
	    	offset = 1
	    	json_obj = data.json()['article']['body']
	    	for cnt in range(0, len(json_obj)):
	    		if 'type' in json_obj[cnt] and offset <=2:
	    			content += json_obj[cnt]['value'] + '  '
	    			offset += 1
	        cleanr =re.compile('<.*?>')
	        self.narrative = text_truncate(re.sub(cleanr,'', content))
	        return
	    else:
	        return False

	@classmethod
	def getCurrent(self):
		config_url = app.config['WEATHER_JSON']
		data = requests.get(str(config_url))
		if data.status_code == 200:
			self.threeday = OrderedDict()
			self.hilo = OrderedDict()
			self.weathericons = OrderedDict()
			self.json_obj = data.json()['primary_modules']
			self.getOneDay(self)
			self.getThreeDay(self)
			return
		else:
			return False

	@staticmethod
	def getOneDay(self):
		for cnt in range(0, len(self.json_obj)):
			if 'weather_seven_day' in self.json_obj[cnt]:
				self.hi_to_replace = self.json_obj[cnt]['weather_seven_day'][0]['tempFHi']
				self.lo_to_replace =  self.json_obj[cnt]['weather_seven_day'][0]['tempFLo']
				self.weather_icon = app.config['WEATHER_ICONS'] + str(self.json_obj[cnt]['weather_seven_day'][0]['dayTime']['weatherIcon']) + '.png'

	@staticmethod
	def getThreeDay(self):
		for cnt in range(0, len(self.json_obj)):
			if 'weather_seven_day' in self.json_obj[cnt]:
				for offset in range(1, 4):
					dayname = self.json_obj[cnt]['weather_seven_day'][offset]['dayCode']
					hi = self.json_obj[cnt]['weather_seven_day'][offset]['tempFHi']
					lo =  self.json_obj[cnt]['weather_seven_day'][offset]['tempFLo']
					weather_icon = app.config['WEATHER_ICONS'] + str(self.json_obj[cnt]['weather_seven_day'][offset]['dayTime']['weatherIcon']) + '.png'
					self.threeday['day' + str(offset)] = dayname[:3]
					self.hilo['day' + str(offset) + '_hi'] = hi
					self.hilo['day' + str(offset) + '_lo'] = lo
					self.weathericons['icon' + str(offset)] = weather_icon


@app.context_processor
def utility_processor():
    def date_now(format="%d.m.%Y %H:%M:%S"):
        return datetime.now().strftime(format)
    return dict(date_now=date_now)

@app.context_processor
def get_title():
    return dict(get_title=app.config['FORECAST_TITLE'])

@app.context_processor
def get_threeday():
    return dict(get_threeday=app.config['THREEDAY_TITLE'])

@app.context_processor
def article_url():
	return dict(article_url=app.config['ARTICLE_URL'])

@app.context_processor
def weather_url():
	return dict(weather_url=app.config['WEATHER_URL'])

def text_truncate(content, length=120, suffix='...'):
	return content[:length].rsplit(' ', 1)[0]+suffix
