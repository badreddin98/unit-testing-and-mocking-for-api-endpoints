import unittest
from unittest.mock import patch
from app import app

class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_employees_empty(self):
        """Test getting employees when the list is empty"""
        with patch('app.employees', []):
            response = self.app.get('/employees')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, [])
    
    def test_add_employee(self):
        """Test adding a new employee"""
        test_employee = {
            'id': 1,
            'name': 'John Doe',
            'position': 'Engineer'
        }
        with patch('app.employees', []):
            response = self.app.post('/employees', json=test_employee)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, test_employee)
    
    def test_get_employee_not_found(self):
        """Test getting a non-existent employee"""
        with patch('app.employees', []):
            response = self.app.get('/employees/999')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'error': 'Employee not found'})

if __name__ == '__main__':
    unittest.main()
