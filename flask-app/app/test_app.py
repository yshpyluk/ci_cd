from app import app
import unittest 


class DummyTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_something(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200)
