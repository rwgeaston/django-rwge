from unittest import TestCase
from json import dumps

from django.test import Client
from django.conf import settings


class RWGETests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_basic_response(self):
        response = self.client.post(
            f'/{settings.RWGE_URL}',
            dumps({'type': 'MESSAGE', 'message': {'text': 'hi rwge'}}),
            content_type='application/json',
        )

        self.assertEqual(response.json(), {'text': 'You said: "hi rwge"'})
