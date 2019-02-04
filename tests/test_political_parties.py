from tests.base_test_case import BaseTestCase


class TestParties(BaseTestCase):
    """Test case class for political parties"""
    def test_get_parties(self):
        """ Test get all political parties"""
        with self.client:
            response = self.client.get('/api/v1/parties')
            self.assertEqual(response._status_code, 200)
