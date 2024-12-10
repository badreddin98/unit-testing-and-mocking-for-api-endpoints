import unittest
from unittest.mock import patch
from app import app

class TestProductEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_products_empty(self):
        """Test getting products when the list is empty"""
        with patch('app.products', []):
            response = self.app.get('/products')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [])
    
    def test_add_product(self):
        """Test adding a new product"""
        test_product = {
            'id': 1,
            'name': 'Test Product',
            'price': 99.99
        }
        with patch('app.products', []):
            response = self.app.post('/products', json=test_product)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, test_product)
    
    def test_get_product_not_found(self):
        """Test getting a non-existent product"""
        with patch('app.products', []):
            response = self.app.get('/products/999')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'Product not found'})

if __name__ == '__main__':
    unittest.main()
