import json

from tests.base_test_case import BaseTestCase
from utils.helpers import party_to_post, party1_to_post, party2_to_post, party3_to_post, party4_to_post, party5_to_post, \
    party6_to_post, party7_to_post


class TestParties(BaseTestCase):
    """Test case class for political parties"""

    def test_get_parties(self):
        """ Test get all political parties"""
        with self.client:
            response = self.client.get('/api/v1/parties')
            self.assertEqual(response._status_code, 200)

    def test_create_party(self):
        """Test to create a political party"""
        with self.client:
            response = self.client.post('api/v1/parties', data=json.dumps(party_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.post('api/v1/parties', data=json.dumps(party1_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party2_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party3_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party4_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party5_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party6_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party7_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)
            response = self.client.post('api/v1/parties', data=json.dumps(party_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 409)


