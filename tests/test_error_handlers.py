import json

from tests.base_test_case import BaseTestCase
from utils.helpers import office_to_post, office_to_post8


class TestHandlers(BaseTestCase):
    """Test case class for political parties"""

    def test_handler_405(self):
        response = self.client.delete(path='api/v1/offices', data=json.dumps(office_to_post),
                                      content_type='application/json')
        self.assertEqual(response._status_code, 405)

    def test_handler_404(self):
        response = self.client.delete(path='api/v1/offices/nhhj', data=json.dumps(office_to_post),
                                      content_type='application/json')
        self.assertEqual(response._status_code, 404)

    def test_handler_400(self):
        response = self.client.post(path='api/v1/offices', data=json.dumps(office_to_post8),
                                      content_type='application/json')
        self.assertEqual(response._status_code, 400)

