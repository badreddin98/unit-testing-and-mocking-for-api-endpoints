import unittest
from unittest.mock import patch
from app import app

class TestOrderEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_orders_empty(self):
        """Test getting orders when the list is empty"""
        with patch('app.orders', []):
            response = self.app.get('/orders')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [])
    
    def test_create_order(self):
        """Test creating a new order"""
        test_order = {
            'id': 1,
            'customer_id': 1,
            'products': [{'id': 1, 'quantity': 2}],
            'total': 199.98
        }
        with patch('app.orders', []):
            response = self.app.post('/orders', json=test_order)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, test_order)
    
    def test_get_order_not_found(self):
        """Test getting a non-existent order"""
        with patch('app.orders', []):
            response = self.app.get('/orders/999')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'Order not found'})

if __name__ == '__main__':
    unittest.main()
