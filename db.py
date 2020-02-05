from . import db


def addUser(user):
    db.session.add(user)
