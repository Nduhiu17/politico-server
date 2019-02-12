import json

from tests.base_test_case import BaseTestCase
from utils.helpers import office_to_post, office1_to_post, office2_to_post, office4_to_post, office3_to_post


class TestOffice(BaseTestCase):
    """Test case class for political parties"""

    def post_office(self):
        response = self.client.post(path='api/v1/offices', data=json.dumps(office_to_post),
                                    content_type='application/json')
        return response

    def test_create_office(self):
        """Test to create a political office"""
        with self.client:
            response = self.post_office()
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v1/offices', data=json.dumps(office1_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_with_no_name(self):
        """Test posting with no name"""
        with self.client:
            response = self.client.post('api/v1/offices', data=json.dumps(office1_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_with_no_office_type(self):
        """Test posting with no office type"""
        with self.client:
            response = self.client.post('api/v1/offices', data=json.dumps(office2_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_with_integer_office_type(self):
        """Test posting with office type data of type integer"""
        with self.client:
            response = self.client.post('api/v1/offices', data=json.dumps(office3_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_with_integer_name(self):
        """Test posting with office name data of type integer"""
        with self.client:
            response = self.client.post('api/v1/offices', data=json.dumps(office4_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_posting_already_registered_party(self):
        """Test posting an already posted party"""
        with self.client:
            self.post_office()
            response = self.client.post('api/v1/offices', data=json.dumps(office_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 409)

    def test_get_offices(self):
        """ Test get all political offices"""
        with self.client:
            response = self.client.get('/api/v1/offices')
            self.assertEqual(response._status_code, 200)
            self.assertIsInstance(response.json['data'], list)

    def test_get_an_office(self):
        """ Test get a single political office"""
        with self.client:
            self.post_office()
            response = self.client.get('/api/v1/offices/1')
            self.assertEqual(response._status_code, 200)

    def test_get_non_existing_office(self):
        """ Test get non existing office"""
        with self.client:
            response = self.client.get('/api/v1/offices/1')
            self.assertEqual(response._status_code, 404)
