"""test for version 2"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import user, user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, \
    user13, user14, user15, user16, user31, user32


class TestAuth(BaseTestCase):
    """Test case class for auth operations"""

    def test_user_can_sign_up(self):
        """Test to create a user"""
        with self.client:
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)

    def test_registering_data_twice(self):
        """Test registering email twice"""
        with self.client:
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 409)

    def test_registering_with_no_data(self):
        """Test registering email twice"""
        with self.client:
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user1),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user2),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user3),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user4),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user5),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user6),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user7),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user8),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user9),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user10),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user11),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user32),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user31),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 409)

    def test_user_can_login(self):
        """Test to create a political office"""
        with self.client:
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v2/auth/login', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 200)

    def test_login_with_inadequate_data(self):
        """Test to create a political office"""
        with self.client:
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v2/auth/login', data=json.dumps(user12),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/login', data=json.dumps(user13),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/login', data=json.dumps(user14),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 404)
            response = self.client.post('api/v2/auth/login', data=json.dumps(user15),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v2/auth/login', data=json.dumps(user16),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)


