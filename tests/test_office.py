import json

from tests.base_test_case import BaseTestCase
from utils.helpers import office_to_post


class TestOffice(BaseTestCase):
    """Test case class for political parties"""

    def test_create_office(self):
        """Test to create a political office"""
        with self.client:
            response = self.client.post('api/v1/offices', data=json.dumps(office_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
