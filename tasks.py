from .app import celery, db
from .model import User

import requests


# sample
@celery.task()
def response():
    users_response = requests.get("http://jsonplaceholder.typicode.com/users")
    return users_response.json()
