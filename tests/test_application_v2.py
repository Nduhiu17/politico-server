import json

from tests.base_test_case import BaseTestCase
from utils.helpers import office_to_post, party_to_post, signup_admin, signup_user, application_to_post, \
    application_to_post1, application_to_post2, application_to_post3, application_to_post4, application_to_post5


class TestApplication(BaseTestCase):
    """Test case class for vote operations"""

    def test_post_application(self):
        """test a user can apply for candidature"""
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
        response = signup_user(self)
        result = json.loads(response.data)
        self.assertIn("token", result)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post1),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post2),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post3),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post4),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post5),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v2/applications', data=json.dumps(application_to_post),
                                    headers={'Authorization': f'Bearer {result["token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 409)

