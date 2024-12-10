import unittest
from unittest.mock import patch
from app import app

class TestCustomerEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_customers_empty(self):
        """Test getting customers when the list is empty"""
        with patch('app.customers', []):
            response = self.app.get('/customers')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [])
    
    def test_add_customer(self):
        """Test adding a new customer"""
        test_customer = {
            'id': 1,
            'name': 'Jane Doe',
            'email': 'jane@example.com'
        }
        with patch('app.customers', []):
            response = self.app.post('/customers', json=test_customer)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, test_customer)
    
    def test_get_customer_not_found(self):
        """Test getting a non-existent customer"""
        with patch('app.customers', []):
            response = self.app.get('/customers/999')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'Customer not found'})

if __name__ == '__main__':
    unittest.main()
