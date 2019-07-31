import requests


class TestIndex:
    def test_connection(self):
        requests.get('http://192.168.0.106:80')

    def test_index(self):
        request_result = requests.get('http://192.168.0.106:80')
        assert request_result.content == b'Hello world!', 'Something went wrong.'
