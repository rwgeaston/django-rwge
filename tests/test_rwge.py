from unittest import TestCase
import random
from json import dumps

from django.test import Client
from django.conf import settings


class RWGETests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_basic_response(self):
        random.seed(1)
        response = self.client.post(
            f'/{settings.RWGE_URL}',
            dumps({'type': 'MESSAGE', 'message': {'text': 'netherlands'}}),
            content_type='application/json',
        )

        self.assertEqual(response.json(), {'text': "the netherlands don't exist"})
