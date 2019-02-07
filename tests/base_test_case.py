import json
from unittest import TestCase

from app import app
from app.V1.offices.models import OFFICE_MOCK_DATABASE
from app.V1.parties.models import MOCK_DATABASE
from utils.helpers import party_to_post


class BaseTestCase(TestCase):
    """ Base class for Tests """

    def setUp(self):
        """Base test class set up method"""
        client = app.test_client()
        self.client = client
        # self.post_party = self.client.post('/api/v1/parties', data=json.dumps(party_to_post),
        #                                 headers={'Content-Type': 'application' '/json'})

    def tearDown(self):
        """Method to delete data from data structures"""

        MOCK_DATABASE['parties'].clear()
        OFFICE_MOCK_DATABASE['offices'].clear()
