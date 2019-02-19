import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_admin, office_to_post, party_to_post, user, candidate_to_register, signup_user, user_u, \
    candidate_to_register1, candidate_to_register2, candidate_to_register3, candidate_to_register4


class TestCandidate(BaseTestCase):
    """Test case class for candidate operations"""

    def test_post_candidate(self):
        """test candidate can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response._status_code, 201)

        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Successfully created candidate')

    def test_post_candidate_by_non_admin(self):
        """test candidate can be posted by non admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user_u),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response._status_code, 201)
        response = signup_user(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json['error'], 'Admin only')

    def test_posting_invalidly_candidate(self):
        """test posting candindate with invalid data"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v2/parties', data=json.dumps(party_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response._status_code, 201)

        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register1),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'party and candidate ids are required')
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register2),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Post data of type strings')
        response = self.client.post('/api/v2/office/3/register', data=json.dumps(candidate_to_register3),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Office not found')
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Successfully created candidate')
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['error'], 'Candindate already registered')
        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register4),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Empty strings are not allowed')

