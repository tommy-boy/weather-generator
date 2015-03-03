from app import app
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

class CommonConfig(object):
    DEBUG = True
    app.secret_key = '\xd1\xfc\x92f,\x9e\xfd\xfc\x06}\xe1\x97'
