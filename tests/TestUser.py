import unittest
from app import create_app


class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
    
    def test_create_user_should_returns_201(self):
        response = self.app.post('/users',
                        json={
                            'name': 'marcos',
                            'email': 'marcos@email.com'
                            })
        self.assertEqual(201, response.status_code)

    def test_create_user_with_not_email_should_returs_400(self):
        response = self.app.post('/users',
                        json={
                            'name': 'marcos'
                            })
        self.assertEqual(400, response.status_code)