import json

from tests.base_test_case import BaseTestCase
from utils.helpers import office_to_post, office1_to_post, office2_to_post, office4_to_post, office3_to_post, \
    office5_to_post, office6_to_post


class TestOffice(BaseTestCase):
    """Test case class for political parties"""

    def test_create_office(self):
        """Test to create a political office"""
        with self.client:
            response = self.client.post('api/v1/offices', data=json.dumps(office_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v1/offices', data=json.dumps(office1_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/offices', data=json.dumps(office2_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/offices', data=json.dumps(office3_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/offices', data=json.dumps(office4_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/offices', data=json.dumps(office5_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/offices', data=json.dumps(office6_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
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
            response = self.client.post('api/v1/offices', data=json.dumps(office_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.get('/api/v1/offices/1')
            self.assertEqual(response._status_code, 200)
