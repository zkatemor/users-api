from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .flask_celery import make_celery

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
celery = make_celery(app)
