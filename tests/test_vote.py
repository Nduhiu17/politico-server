import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_admin, office_to_post, party_to_post, user, candidate_to_register, vote, vote1, vote2, \
    vote3, user33, candidate_to_register11


class TestVote(BaseTestCase):
    """Test case class for vote operations"""

    def test_post_vote(self):
        """test a user can vote"""
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
        response = self.client.post('/api/v2/votes', data=json.dumps(vote),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'voted successfully')
        response = self.client.post('/api/v2/votes', data=json.dumps(vote),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 409)

        response = self.client.post('/api/v2/votes', data=json.dumps(vote1),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/votes', data=json.dumps(vote2),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/votes', data=json.dumps(vote3),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_vote_different_county(self):
        """test a user can vote"""
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
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user33),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response._status_code, 201)

        response = self.client.post('/api/v2/office/1/register', data=json.dumps(candidate_to_register11),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Successfully created candidate')
        response = self.client.post('/api/v2/votes', data=json.dumps(vote2),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
