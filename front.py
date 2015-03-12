import os
from app import app
from flask import Flask, request, render_template, Response
from werkzeug import secure_filename
from app.models import Weather


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

@app.route('/front', methods=['GET'])
def metrics():  # pragma: no cover
    front = Weather  # get an instance of the class
    front.getFront()
    front_file = app.config['UPLOAD_FOLDER'] + "weather_front.html"
    output_from_parsed_template = render_template('front.html', front=front)
    with open(front_file, "wb") as f:
        f.write(output_from_parsed_template)
        return output_from_parsed_template


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])