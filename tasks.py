from .db import *

import requests


def users_response():
    """user request"""
    deleteAll()
    createTable()

    response = requests.get("http://jsonplaceholder.typicode.com/users")
    users_json = response.json()

    for user in users_json:
        addUser(User(user['name'],
                     user['username'],
                     user['email'],
                     user['phone'],
                     user['website']))

    return users_json


def posts_response():
    """post request"""
    deleteAll()
    createTable()

    response = requests.get("http://jsonplaceholder.typicode.com/posts")
    posts_json = response.json()

    for post in posts_json:
        addPost(Post(post['userId'],
                     post['title'],
                     post['body']))

    return posts_json
