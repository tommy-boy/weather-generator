#!flask/bin/python
import os
from app import app

if __name__ == '__main__':
	# port = int(os.environ.get("PORT", 5000))
	# app.run(host = '127.0.0.0', port = port, debug = app.config['DEBUG'])
	app.run(debug=app.config['DEBUG'])