from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .flask_celery import make_celery
from .config import Config
import requests


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
celery = make_celery(app)


@app.route('/', methods=['GET'])
def index():
    users_response = requests.get("http://jsonplaceholder.typicode.com/users")
    return render_template(
        "index.html",
        users=users_response.json(),
    )
