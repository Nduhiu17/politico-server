"""test for version 2"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import user


class TestAuth(BaseTestCase):
    """Test case class for auth operations"""

    def test_create_office(self):
        """Test to create a political office"""
        with self.client:
            response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)