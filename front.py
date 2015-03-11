import os
from app import app
from flask import render_template
from app.models import Weather


@app.route('/front')
def front():
	front = Weather  # get an instance of the class
	front.getFront()
	return render_template('front.html', front=front)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])