from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
DEBUG = True
PORT = os.environ.get("PORT")

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET")


if __name__ == '__main__':
    models.initialize()
    app.run(debug = DEBUG, port = PORT)