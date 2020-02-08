from .model import User, Post
from . import db

import sqlalchemy as sa


def addResource(resource):
    """add resourse to database"""
    db.session.add(resource)
    db.session.commit()


def removeUser(id):
    """remove user (and user's posts) from database"""
    removeUserPost(id)
    User.query.filter(User.id == id).delete()
    db.session.commit()


def removePost(id):
    """remove post from database"""
    Post.query.filter(Post.id == id).delete()
    db.session.commit()


def removeUserPost(userId):
    """remove user's posts from database"""
    Post.query.filter(Post.userId == userId).delete()
    db.session.commit()


def updateUser(id, new_user):
    """update info about user"""
    try:
        if new_user.name:
            User.query.filter_by(id=id).update({'name': new_user.name})

        if new_user.username:
            User.query.filter_by(id=id).update({'username': new_user.username})

        if new_user.email:
            User.query.filter_by(id=id).update({'email': new_user.email})

        if new_user.phone:
            User.query.filter_by(id=id).update({'phone': new_user.phone})

        if new_user.website:
            User.query.filter_by(id=id).update({'website': new_user.website})

        db.session.commit()

    except Exception as e:
        return str(e)


def updatePost(id, new_post):
    """update info about user"""
    try:
        if new_post.userId:
            Post.query.filter_by(id=id).update({'userId': new_post.userId})

        if new_post.title:
            Post.query.filter_by(id=id).update({'title': new_post.title})

        if new_post.body:
            Post.query.filter_by(id=id).update({'body': new_post.body})

        db.session.commit()

    except Exception as e:
        return str(e)


def deleteAll():
    """delete database"""
    db.drop_all()


def createTable():
    """init database"""
    db.create_all()


def database_is_empty():
    """check if the database is empty"""
    table_names = sa.inspect(sa.engine).get_table_names()
    is_empty = table_names == []
    return is_empty

