"""tests  for office version two"""
import json

from tests.base_test_case import BaseTestCase
from utils.helpers import signup_admin, office_to_post, signup_user, office1_to_post, office_to_post8, office3_to_post, \
    office5_to_post, office_to_post10, office_to_post23


class TestOffice(BaseTestCase):
    """Test case class for office operations"""

    def test_post_office(self):
        """test office can be posted by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['data']['office_type'], 'federal')

    def test_post_office_by_non_admin(self):
        """test posting an office by non admin"""
        response = signup_user(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json['error'], 'Admin only')

    def test_post_not_enough_fields(self):
        """test posting with no enough fields by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office1_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'name and office type are required')

    def test_post_non_strings(self):
        """test posting with  by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post8),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Post data of type strings')

    def test_post_non_allowed_office(self):
        """test posting with  by admin"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office3_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/offices', data=json.dumps(office5_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post10),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'That office type is not allowed')

    def test_post_office_name_twice(self):
        """test posting office twice"""
        response = signup_admin(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['data']['office_type'], 'federal')
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['error'], 'Office type already registered')
        response = self.client.post('/api/v2/offices', data=json.dumps(office_to_post23),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['error'], 'Office name already registered')




