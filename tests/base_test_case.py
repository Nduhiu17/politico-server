from unittest import TestCase

from app import app
from app.V1.offices.models import OFFICE_MOCK_DATABASE
from app.V1.parties.models import MOCK_DATABASE


class BaseTestCase(TestCase):
    """ Base class for Tests """

    def setUp(self):
        """Base test class set up method"""
        client = app.test_client()

        self.client = client

    def tearDown(self):
        """Method to delete data from data structures"""

        MOCK_DATABASE['parties'].clear()
        OFFICE_MOCK_DATABASE['offices'].clear()
