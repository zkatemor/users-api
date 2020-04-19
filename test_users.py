import json
import os
import unittest
from dotenv import load_dotenv

from app import create_app
from manage import app

load_dotenv()


class UsersTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(os.environ['TEST_APP_SETTINGS'])
        self.client = app.test_client()

        self.name = "test name"
        self.username = "test username"
        self.email = "test email"
        self.phone = "test phone"
        self.website = "test.test"

        self.name_update = "test name_update"
        self.username_update = "test username_update"
        self.email_update = "test email_update"
        self.phone_update = "test phone_update"
        self.website_update = "test.test_update"

        self.name_update_detail = "test name_update_detail"
        self.username_update_detail = "test username_update_detail"

    def test_users_get(self):
        response = self.client.get('/users')

        actual = response.status_code
        expected = 200

        self.assertEqual(actual, expected)

    def test_users_create(self):
        data = {
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "website": self.website
        }
        response = self.client.post('/users', data=data)

        actual = response.status_code
        expected = 201

        self.assertEqual(actual, expected)

    def test_users_put(self):
        data = {
            "name": self.name_update,
            "username": self.username_update,
            "email": self.email_update,
            "phone": self.phone_update,
            "website": self.website_update
        }
        response = self.client.put('/users/5', data=data)

        actual = response.status_code
        expected = 204

        self.assertEqual(actual, expected)

    def test_users_patch(self):
        data = {
            "name": self.name_update_detail,
            "username": self.username_update_detail,
        }
        response = self.client.patch('/users/5', data=data)

        actual = response.status_code
        expected = 200

        self.assertEqual(actual, expected)

    def test_users_get_one(self):
        data = {
            "id": 6
        }
        response = self.client.get('/users', data=data)

        actual = response.status_code
        expected = 200

        self.assertEqual(actual, expected)

    def test_users_delete(self):
        data = {
            "id": 2
        }
        response = self.client.delete('/users', data=data)

        actual = response.status_code
        expected = 204

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
