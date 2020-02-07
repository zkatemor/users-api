import markdown

from flask_restful import Resource, reqparse

from .tool import *
from .db import *
from . import app, api


@app.route('/')
def index():
    try:
        createTable()
        users_response()
        posts_response()
    except Exception as e:
        print(str(e))

    """present some documentation"""
    with open('README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


class UsersList(Resource):
    def get(self):
        """all users list"""
        users = User.query.all()
        js = get_users_json(users)
        return {'message': 'Success', 'data': js}, 200

    def post(self):
        """creating a user"""
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('username', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('phone', required=True)
        parser.add_argument('website', required=True)

        args = parser.parse_args()

        user = User(args['name'],
                    args['username'],
                    args['email'],
                    args['phone'],
                    args['website'])

        addResource(user)

        js = get_users_json([user])

        return {'message': 'Success', 'data': js}, 201


class Customer(Resource):
    def get(self, id):
        """lookup user details"""
        if User.query.filter(User.id == id).count():
            user = User.query.filter(User.id == id)
            js = get_users_json(user)
            return {'message': 'User found', 'data': js}
        else:
            return {'message': 'User not found', 'data': {}}, 404

    def delete(self, id):
        """delete user by id"""
        if User.query.filter(User.id == id).count():
            removeUser(id)
            return '', 204
        else:
            return {'message': 'User not found', 'data': {}}, 404


class PostsList(Resource):
    def get(self):
        """all posts list"""
        posts = Post.query.all()
        js = get_posts_json(posts)
        return {'message': 'Success', 'data': js}, 200

    def post(self):
        """creating a post"""
        parser = reqparse.RequestParser()

        parser.add_argument('userId', required=True)
        parser.add_argument('title', required=True)
        parser.add_argument('body', required=True)

        args = parser.parse_args()

        post = Post(args['userId'],
                    args['title'],
                    args['body'])

        addResource(post)

        js = get_posts_json([post])

        return {'message': 'Success', 'data': js}, 201


class Message(Resource):
    def get(self, id):
        """lookup post details"""
        if Post.query.filter(Post.id == id).count():
            post = Post.query.filter(Post.id == id)
            js = get_posts_json(post)
            return {'message': 'Post found', 'data': js}
        else:
            return {'message': 'Post not found', 'data': {}}, 404

    def delete(self, id):
        """delete post by id"""
        if Post.query.filter(Post.id == id).count():
            removePost(id)
            return '', 204
        else:
            return {'message': 'Post not found', 'data': {}}, 404


class UserPost(Resource):
    def get(self, userId):
        """viewing posts of a specific user"""
        if Post.query.filter(Post.userId == userId).count():
            post = Post.query.filter(Post.userId == userId)
            js = get_posts_json(post)
            return {'message': 'Success', 'data': js}
        else:
            return {'message': 'Posts not found', 'data': {}}, 404

    def delete(self, userId):
        """delete specific user posts"""
        if Post.query.filter(Post.userId == userId).count():
            removeUserPost(userId)
            return '', 204
        else:
            return {'message': 'User posts not found', 'data': {}}, 404


class Author(Resource):
    def get(self):
        """found author of the post by post id"""
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)

        args = parser.parse_args()
        id = args['id']

        user = User.query.join(User.posts, aliased=True) \
            .filter_by(id=id)

        js = get_users_json(user)

        return {'message': 'Success', 'data': js}


api.add_resource(UsersList, '/users')
api.add_resource(Customer, '/user/<int:id>')
api.add_resource(PostsList, '/posts')
api.add_resource(Message, '/post/<int:id>')
api.add_resource(UserPost, '/user_post/<int:userId>')
api.add_resource(Author, '/author')
