from . import celery
from .db import *

import requests


@celery.task()
def response():
    """background user request"""
    deleteAll()
    createTable()

    users_response = requests.get("http://jsonplaceholder.typicode.com/users")
    users_json = users_response.json()

    for user in users_json:
        addUser(User(user['name'],
                     user['username'],
                     user['email'],
                     user['phone'],
                     user['website']))

