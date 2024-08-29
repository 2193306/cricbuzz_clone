import unittest
from app import create_app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Live Cricket Scores', response.data)

if __name__ == '__main__':
    unittest.main()
