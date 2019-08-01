import requests

import config_data


class TestIndex:
    address = f'http://{config_data.vm_ip}:{config_data.flask_port}'

    def test_connection(self):
        """
        Smoke test to check is connection allowed.
        :return:
        """
        requests.get(TestIndex.address)

    def test_index(self):
        request_result = requests.get(TestIndex.address)
        assert request_result.content == b'Hello world!', 'Something went wrong.'
