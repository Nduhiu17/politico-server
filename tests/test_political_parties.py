import json

from tests.base_test_case import BaseTestCase
from utils.helpers import party_to_post, party4_to_post, party5_to_post,party6_to_post, party7_to_post, party8_to_post


class TestParties(BaseTestCase):
    """Test case class for political parties"""

    def test_get_parties(self):
        """ Test get all political parties"""
        with self.client:
            response = self.client.get('api/v1/parties', headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 200)

    def post_party(self):
        response = self.client.post(path='api/v1/parties', data=json.dumps(party_to_post),
                                    content_type='application/json')
        return response

    def test_create_party(self):
        """Test to create a political party"""
        with self.client:
            response = self.post_party()
            self.assertEqual(response._status_code, 201)

    def test_post_with_no_name(self):
        """Test posting with no name"""
        with self.client:
            response = self.client.post('api/v1/parties', data=json.dumps(party4_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_with_no_hqaddress(self):
        """Test posting with no hqaddress"""
        with self.client:
            response = self.client.post('api/v1/parties', data=json.dumps(party5_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_with_no_logourl(self):
        """Test posting with no logourl"""
        with self.client:
            response = self.client.post('api/v1/parties', data=json.dumps(party6_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_posting_integers(self):
        """Test posting integers"""
        with self.client:
            response = self.client.post('api/v1/parties', data=json.dumps(party7_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_post_existing_party(self):
        """Test posting an existing party"""
        with self.client:
            self.post_party()
            response = self.client.post('api/v1/parties', data=json.dumps(party_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 409)

    def test_get_party(self):
        """Test for getting a political party"""
        with self.client:
            response = self.client.post('api/v1/parties', data=json.dumps(party_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.get('api/v1/parties/1', headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 200)

    def test_get_non_existing_party(self):
        """Test for getting a non existing party"""
        with self.client:
            response = self.client.get('api/v1/parties/10000', headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 404)

    def test_edit_party(self):
        """Tests for editing a political party"""
        with self.client:
            self.post_party()
            response = self.client.patch('api/v1/parties/1/name', data=json.dumps(party8_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 201)
            response = self.client.patch('api/v1/parties/1/name', data=json.dumps(party4_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_edit_party_with_no_name(self):
        """Tests for editing a political party with no name"""
        with self.client:
            self.post_party()
            response = self.client.patch('api/v1/parties/1/name', data=json.dumps(party4_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_edit_party_with_invalid_data(self):
        """Tests for editing a political party with no name"""
        with self.client:
            self.post_party()
            response = self.client.patch('api/v1/parties/1/name', data=json.dumps(party7_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 400)

    def test_edit_party_with_existing_name(self):
        """Tests for editing a political party with an existing name"""
        with self.client:
            self.post_party()
            response = self.client.patch('api/v1/parties/1/name', data=json.dumps(party_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 409)

    def test_delete_party(self):
        """Tests for deleting a political party"""
        self.post_party()
        response = self.client.delete('api/v1/parties/1', headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.json['status'], 204)

    def test_delete_non_existing_party(self):
        """Tests for deleting a political party"""
        self.post_party()
        response = self.client.delete('api/v1/parties/10', headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.json['status'], 404)

    def test_docs(self):
        """Test documentation link"""
        with self.client:
            response = self.client.get('/', headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 200)
