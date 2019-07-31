import sys
import os
import unittest
from multiprocessing import Process

import requests

sys.path.extend([os.getcwd()])

from app import app
import time

class MyTestCase(unittest.TestCase):
    def test_connection(self):
        requests.get('http://localhost:80')

    def test_index(self):
        request_result = requests.get('http://127.0.0.1:5000')
        self.assertEqual(request_result.content, b'Hello world!', 'Something went wrong.')


if __name__ == '__main__':
    flask_app_thread = Process(target=app.run, args=('0.0.0.0', 80, True), daemon=True)
    flask_app_thread.start()
    time.sleep(10)
    unittest.main()
