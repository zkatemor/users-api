from . import db


class User(db.Model):
    """table with users"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(80), unique=True)
    website = db.Column(db.String(80), unique=True)

    def __init__(self, name, username, email, phone, website):
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    """table with posts"""
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, userId, title, body):
        self.userId = userId
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Post %r>' % self.body
