"""test party version two"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_user, party_to_post, party7_to_post, party8_to_post, signup_admin, party_to_post_empty, \
    party_update_data, party_update_data1, party_update_data2, party_update_data3, party_update_data4


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
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['data']['hqaddress'], 'New york')
            response = self.client.get('/api/v2/parties/10', headers={'Authorization': f'Bearer {result["token"]}',
                                                                      'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json['error'], 'No party with that id')

    def test_update_a_party(self):
        """Test updating a  party"""
        with self.client:
            response = signup_admin(self)
            result = json.loads(response.data)
            self.assertIn("token", result)
            response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                        headers={'Authorization': f'Bearer {result["token"]}',
                                                 'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 201)
            response = self.client.patch('/api/v2/parties/1/name', data=json.dumps(party_update_data),
                                         headers={'Authorization': f'Bearer {result["token"]}',
                                                  'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], 'updated successfully')

    def test_update_a_party_with_no_data(self):
        """Test can get parties"""
        with self.client:
            response = signup_admin(self)
            result = json.loads(response.data)
            self.assertIn("token", result)
            response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                        headers={'Authorization': f'Bearer {result["token"]}',
                                                 'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 201)
            response = self.client.patch('/api/v2/parties/1/name', data=json.dumps(party_update_data1),
                                         headers={'Authorization': f'Bearer {result["token"]}',
                                                  'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['error'], 'Party name is required')

            response = self.client.patch('/api/v2/parties/1/name', data=json.dumps(party_update_data2),
                                         headers={'Authorization': f'Bearer {result["token"]}',
                                                  'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['error'], 'Empty strings are not allowed')

            response = self.client.patch('/api/v2/parties/1/name', data=json.dumps(party_to_post),
                                         headers={'Authorization': f'Bearer {result["token"]}',
                                                  'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 409)
            self.assertEqual(response.json['error'], 'Party name already taken')
            response = self.client.patch('/api/v2/parties/10/name', data=json.dumps(party_update_data3),
                                         headers={'Authorization': f'Bearer {result["token"]}',
                                                  'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json['error'], 'No party found with that id')
            response = self.client.patch('/api/v2/parties/1/name', data=json.dumps(party_update_data4),
                                         headers={'Authorization': f'Bearer {result["token"]}',
                                                  'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['error'], 'Name should be of type strings')
