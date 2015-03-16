from app import app
from flask import render_template
from models import Weather


@app.route('/', methods=['GET'])
def index():
	forecast = Weather  # get an instance of the class
	forecast.getForecast()
	forecast.getCurrent()
	weatherimg = app.config['IMGDIR'] + app.config['WEATHERIMG']
	return render_template('index.html', title='Index', weatherimg=weatherimg, forecast=forecast)

@app.route('/front', methods=['GET'])
def front():
    front = Weather  # get an instance of the class
    front.getFront()
    front_file = app.config['UPLOAD_FOLDER'] + "weatherfront.html"
    output_from_parsed_template = render_template('front.html', front=front)
    with open(front_file, "wb") as f:
        f.write(output_from_parsed_template)
        return output_from_parsed_template

