from . import celery
from .model import User
from .db import *

import requests


@celery.task()
def response():
    """background user request"""
    users_response = requests.get("http://jsonplaceholder.typicode.com/users")
    users_json = users_response.json()

    for user in users_json:
        addUser(User(user['id'],
                     user['name'],
                     user['username'],
                     user['email'],
                     user['phone'],
                     user['website']))

    db.session.commit()
