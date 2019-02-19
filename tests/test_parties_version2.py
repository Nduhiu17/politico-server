"""test party version two"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_user, party_to_post, party7_to_post, party8_to_post, signup_admin, party_to_post_empty


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

    def test_post_party(self):
        """test party can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_post_party_by_non_admin(self):
        """test party can be posted"""
        response = signup_user(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 403)

    def test_post_party_twice(self):
        """test party can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 409)

    def test_post_non_strings(self):
        """test party can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/parties', data=json.dumps(party7_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_post_empty_strings(self):
        """test party can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post_empty),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_post_not_enough_fields(self):
        """test party can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/parties', data=json.dumps(party8_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_get_a_party(self):
        """Test can get party"""
        with self.client:
            response = signup_admin(self)
            result = json.loads(response.data)
            self.assertIn("token", result)
            response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                        headers={'Authorization': f'Bearer {result["token"]}',
                                                 'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 201)

            response = self.client.get('/api/v2/parties/1', headers={'Authorization': f'Bearer {result["token"]}',
                                                                     'Content-Type': 'application' '/json'})
            print(response)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['data']['hqaddress'], 'New york')
            response = self.client.get('/api/v2/parties/10', headers={'Authorization': f'Bearer {result["token"]}',
                                                                      'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json['error'], 'No party with that id')
