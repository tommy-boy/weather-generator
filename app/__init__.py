from flask import Flask, jsonify, make_response
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object('configs.default.CommonConfig')
app.config.from_envvar('WEATHER-GENERATOR', silent=True)
from app import views

toolbar = DebugToolbarExtension(app)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(403)
def unauthorized(error):
    return make_response(jsonify( { 'error': 'Domain not Authorized' } ), 403)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
