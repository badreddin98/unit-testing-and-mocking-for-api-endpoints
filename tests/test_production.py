import unittest
from unittest.mock import patch
from app import app

class TestProductionEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_production_lines_empty(self):
        """Test getting production lines when the list is empty"""
        with patch('app.production_lines', []):
            response = self.app.get('/production')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [])
    
    def test_add_production_line(self):
        """Test adding a new production line"""
        test_line = {
            'id': 1,
            'name': 'Line A',
            'status': 'active',
            'capacity': 1000
        }
        with patch('app.production_lines', []):
            response = self.app.post('/production', json=test_line)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, test_line)
    
    def test_get_production_line_not_found(self):
        """Test getting a non-existent production line"""
        with patch('app.production_lines', []):
            response = self.app.get('/production/999')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'Production line not found'})

if __name__ == '__main__':
    unittest.main()
