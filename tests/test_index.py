import requests


class TestIndex:
    def test_connection(self):
        requests.get('http://localhost:80')

    def test_index(self):
        request_result = requests.get('http://127.0.0.1:5000')
        assert request_result.content == b'Hello world!', 'Something went wrong.'
