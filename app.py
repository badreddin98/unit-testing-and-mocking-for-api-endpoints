from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database
employees = []
products = []
orders = []
customers = []
production_lines = []

# Employee endpoints
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def add_employee():
    employee = request.json
    employees.append(employee)
    return jsonify(employee), 201

@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = next((emp for emp in employees if emp.get('id') == emp_id), None)
    if employee:
        return jsonify(employee)
    return jsonify({'error': 'Employee not found'}), 404

# Product endpoints
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201

@app.route('/products/<int:prod_id>', methods=['GET'])
def get_product(prod_id):
    product = next((prod for prod in products if prod.get('id') == prod_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# Order endpoints
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((ord for ord in orders if ord.get('id') == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({'error': 'Order not found'}), 404

# Customer endpoints
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    customer = request.json
    customers.append(customer)
    return jsonify(customer), 201

@app.route('/customers/<int:cust_id>', methods=['GET'])
def get_customer(cust_id):
    customer = next((cust for cust in customers if cust.get('id') == cust_id), None)
    if customer:
        return jsonify(customer)
    return jsonify({'error': 'Customer not found'}), 404

# Production endpoints
@app.route('/production', methods=['GET'])
def get_production_lines():
    return jsonify(production_lines)

@app.route('/production', methods=['POST'])
def add_production_line():
    line = request.json
    production_lines.append(line)
    return jsonify(line), 201

@app.route('/production/<int:line_id>', methods=['GET'])
def get_production_line(line_id):
    line = next((l for l in production_lines if l.get('id') == line_id), None)
    if line:
        return jsonify(line)
    return jsonify({'error': 'Production line not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
