import json

from tests.base_test_case import BaseTestCase
from utils.helpers import party_to_post


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
