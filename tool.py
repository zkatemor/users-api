from .db import *

import requests


def users_response():
    """user request"""
    response = requests.get("http://jsonplaceholder.typicode.com/users")
    users_json = response.json()

    for user in users_json:
        addResource(User(user['name'],
                         user['username'],
                         user['email'],
                         user['phone'],
                         user['website']))

    return users_json


def posts_response():
    """post request"""
    response = requests.get("http://jsonplaceholder.typicode.com/posts")
    posts_json = response.json()

    for post in posts_json:
        addResource(Post(post['userId'],
                         post['title'],
                         post['body']))

    return posts_json


def get_users_json(users):
    json_users = []

    for user in users:
        dict = {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'website': user.website
        }
        json_users.append(dict)

    return json_users


def get_posts_json(posts):
    json_posts = []

    for post in posts:
        dict = {
            'id': post.id,
            'userId': post.userId,
            'title': post.title,
            'body': post.body
        }
        json_posts.append(dict)

    return json_posts
