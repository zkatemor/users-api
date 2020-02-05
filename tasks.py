from . import celery
from .model import User

import requests


@celery.task()
def response():
    """background user request"""
    users = []
    users_response = requests.get("http://jsonplaceholder.typicode.com/users")
    users_json = users_response.json()

    for user in users_json:
        users.append(User(user['id'], user['name'], user['username'],
                          user['email'], user['phone'], user['website']))

    return users
