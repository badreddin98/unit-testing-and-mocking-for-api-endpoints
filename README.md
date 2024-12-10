# Factory Management System API Testing

This project demonstrates unit testing and mocking for a Factory Management System API endpoints.

## Project Structure
```
.
├── README.md
├── requirements.txt
├── app.py
└── tests/
    ├── __init__.py
    ├── test_employee.py
    ├── test_product.py
    ├── test_order.py
    ├── test_customer.py
    └── test_production.py
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
python -m pytest tests/
```
