"""test party version two"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_user


class TestParty(BaseTestCase):
    """Test case class for auth operations"""

    def test_get_parties(self):
        """Test can get parties"""
        with self.client:
            response = signup_user(self)
            result = json.loads(response.data)
            self.assertIn("token", result)
            response = self.client.get('/api/v2/parties', headers={'Authorization': f'Bearer {result["token"]}',
                                                                   'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 200)

    def test_get_with_no_token(self):
        """Test get parties with no token"""
        with self.client:
            response = self.client.get('api/v2/parties', headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 401)

