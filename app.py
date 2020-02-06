from flask import render_template, redirect, request, url_for

from .db import *
from . import app


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/users', methods=['GET'])
def users():
    # response.delay() фоновое не работает
    # response()

    return render_template(
        "users.html",
        users=User.query.all()
    )


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    website = request.form['website']

    addUser(User(name, username, email, phone, website))

    return redirect(url_for('users'))


@app.route('/update_user', methods=['POST'])
def update_user():
    id = request.form['id']

    new_id = request.form['new_id']
    name = request.form['new_name']
    username = request.form['new_username']
    email = request.form['new_email']
    phone = request.form['new_phone']
    website = request.form['new_website']

    update = updateUser(id, new_id, User(name, username, email, phone, website))

    return redirect(url_for('users'))


@app.route('/delete_user', methods=['POST'])
def delete_user():
    id = request.form['id']
    deleteUser(id)

    return redirect(url_for('users'))
