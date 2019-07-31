import unittest

import requests

class TestIndex(unittest.TestCase):
    def test_connection(self):
        requests.get('http://localhost:80')

    def test_index(self):
        request_result = requests.get('http://127.0.0.1:5000')
        self.assertEqual(request_result.content, b'Hello world!', 'Something went wrong.')

