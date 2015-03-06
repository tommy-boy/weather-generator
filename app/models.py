from app import app
from flask import render_template, request
import requests
import json
import re
from collections import OrderedDict
from datetime import datetime


class Weather(object):
	# def getConfig():
	#     config_url = "http://configfactory.azcentral.com/weathergenerator/default/config.json"
	#     headers = {'Content-Type': 'application/json'}
	#     data = requests.get(config_url, params = request.args, headers=headers)
	#     if data.status_code == 200:
	#         return data.json()
	#     else:
	#         return False


    @classmethod
    def getForecast(self):
	    article_json = app.config['ARTICLE_JSON']
	    data = requests.get(str(article_json))
	    if data.status_code == 200:
	    	narrative = ''
	    	pos = 1
	    	json_obj = data.json['article']['body']
	    	for cnt in range(0, len(json_obj)):
	    		if 'type' in json_obj[cnt] and pos <=2:
	    			narrative += json_obj[cnt]['value'] + '  '
	    			pos += 1
	        cleanr =re.compile('<.*?>')
	        narrative = re.sub(cleanr,'', narrative)
	        return text_truncate(narrative)
	    else:
	        return False

    @classmethod
    def getCurrent(self):
		config_url = app.config['WEATHER_JSON']
		data = requests.get(str(config_url))
		if data.status_code == 200:
			json_obj = data.json['primary_modules']
			for cnt in range(0, len(json_obj)):
				if 'weather_seven_day' in json_obj[cnt]:
					hi_to_replace = json_obj[cnt]['weather_seven_day'][0]['tempFHi']
					lo_to_replace =  json_obj[cnt]['weather_seven_day'][0]['tempFLo']
					weather_icon = app.config['WEATHER_ICONS'] + str(json_obj[cnt]['weather_seven_day'][0]['dayTime']['weatherIcon']) + '.png'
			return (hi_to_replace, lo_to_replace, weather_icon)
		else:
			return False

    @classmethod
    def getThreeDay(self):
		config_url = app.config['WEATHER_JSON']
		data = requests.get(str(config_url))
		if data.status_code == 200:
			threeday = OrderedDict()
			weathericons = OrderedDict()
			hilo = OrderedDict()
			json_obj = data.json['primary_modules']
			for cnt in range(0, len(json_obj)):
				if 'weather_seven_day' in json_obj[cnt]:
					for offset in range(1, 4):
						# dayname_to_replace = "day" + str(offset)
						dayname = json_obj[cnt]['weather_seven_day'][offset]['dayCode']
						hi_to_replace = json_obj[cnt]['weather_seven_day'][offset]['tempFHi']
						lo_to_replace =  json_obj[cnt]['weather_seven_day'][offset]['tempFLo']
						weather_icon = app.config['WEATHER_ICONS'] + str(json_obj[cnt]['weather_seven_day'][offset]['dayTime']['weatherIcon']) + '.png'
						threeday['day' + str(offset)] = dayname[:3]
						hilo['day' + str(offset) + '_hi'] = hi_to_replace
						hilo['day' + str(offset) + '_lo'] = lo_to_replace
						weathericons['icon' + str(offset)] = weather_icon
			return (threeday, weathericons, hilo)
		else:
			return False

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




  
