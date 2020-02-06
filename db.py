from .model import User
from . import db

import sqlalchemy as sa


def addUser(user):
    """add user to database"""
    db.session.add(user)
    db.session.commit()


def removeUser(id):
    """remove user from database"""
    User.query.filter(User.id == id).delete()
    db.session.commit()


def updateUser(id, new_id, new_user):
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

        if id != new_id and new_id:
            User.query.filter_by(id=id).update({'id': new_id})

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

