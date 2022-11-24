from flask import Flask, jsonify, after_this_request
from flask_login import LoginManager
from dotenv import load_dotenv
import os

import models

from resources.user import user
from resources.layout import layout

from flask_cors import CORS
CORS(user, origins = ['https://www.biy.app', 'http://localhost:3000'], supports_credentials = True)
CORS(layout, origins = ['https://www.biy.app', 'http://localhost:3000'], supports_credentials = True)

load_dotenv()
DEBUG = True
PORT = os.environ.get("PORT")

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET")
app.register_blueprint(user, url_prefix = '/user')
app.register_blueprint(layout, url_prefix = '/layout')

# FOR DEPLOYMENT ONLY
# app.config.update(
#     SESSION_COOKIE_SECURE=True,
#     SESSION_COOKIE_HTTPONLY=True,
#     SESSION_COOKIE_SAMESITE='None',
# )

@app.before_request
def before_request():
    """Connect to the db before each request"""
    print("This should be shown before each request")
    models.DATABASE.connect()

    @after_this_request
    def after_request(response):
        """Close the db connection after each request"""
        print("This should be shown after each request")
        models.DATABASE.close()
        return response

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


if __name__ == '__main__':
    models.initialize()
    app.run(debug = DEBUG, port = PORT)

if os.environ.get('FLASK_ENV') != 'development':
    print('\non heroku!')
    models.initialize()