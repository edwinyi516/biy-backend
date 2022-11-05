from flask import Flask
from flask import jsonify
from flask_login import LoginManager
from dotenv import load_dotenv
import os

import models

from resources.user import user

from flask_cors import CORS
CORS(user, origins = ['httpL//localhost:3000'], supports_credentials = True)

load_dotenv()
DEBUG = True
PORT = os.environ.get("PORT")

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET")
app.register_blueprint(user, url_prefix = '/user')

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