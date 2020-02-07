from flask import redirect, request, url_for, json, jsonify
from flask_restful import Resource, reqparse

from .tasks import *
from .db import *
from . import app, api


def get_json(users):
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


class UsersList(Resource):
    def get(self):
        users = User.query.all()
        js = get_json(users)
        return {'message': 'Success', 'data': js}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('username', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('phone', required=True)
        parser.add_argument('website', required=True)

        args = parser.parse_args()
        addUser(args)

        users = User.query.all()
        js = get_json(users)
        return {'message': 'Success', 'data': js}, 201


class Customer(Resource):
    def get(self, id):
        if User.query.filter(User.id == id).count():
            user = User.query.filter(User.id == id)
            js = get_json(user)
            return {'message': 'User found', 'data': js}
        else:
            return {'message': 'User not found', 'data': {}}, 404

    def delete(self, id):
        if User.query.filter(User.id == id).count():
            removeUser(id)
            return '', 204
        else:
            return {'message': 'User not found', 'data': {}}, 404


api.add_resource(UsersList, '/users')
api.add_resource(Customer, '/user/<int:id>')
