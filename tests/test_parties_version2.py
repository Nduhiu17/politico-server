"""test party version two"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_user


class TestAuth(BaseTestCase):
    """Test case class for auth operations"""

    def test_user_can_sign_up(self):
        """Test to create a user"""
        with self.client:
            response = signup_user(self)
            result = json.loads(response.data)
            self.assertIn("token", result)
            response = self.client.get('/api/v2/parties',headers={'Authorization': f'Bearer {result["token"]}',
                                                                   'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 200)
