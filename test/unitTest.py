import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app

class APITestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_vowel_count(self):
        response = self.app.post('/vowel_count', json={"words": ["batman", "robin", "coringa"]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"batman": 2, "robin": 2, "coringa": 3})
        
    def test_sort_asc(self):
        response = self.app.post('/sort', json={"words": ["batman", "robin", "coringa"], "order": "asc"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ["batman", "coringa", "robin"])

    def test_sort_desc(self):
        response = self.app.post('/sort', json={"words": ["batman", "robin", "coringa"], "order": "desc"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ["robin", "coringa", "batman"])
        
    def test_invalid_content_type(self):
        response = self.app.post('/vowel_count', data='{"words": ["batman", "robin", "coringa"]}')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Content-Type must be application/json"})
        
    def test_invalid_method(self):
        response = self.app.get('/vowel_count')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json, {"error": "Method not allowed"})

if __name__ == '__main__':
    unittest.main()
