import unittest
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_greeting(self):
        response = self.client.get('/greeting?name=Test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Test!', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
