from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(80), unique=True)
    website = db.Column(db.String(80), unique=True)

    def __init__(self, id, name, username, email, phone, website):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

    def __repr__(self):
        return '<User %r>' % self.username
