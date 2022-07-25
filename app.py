from flask import Flask, jsonify, request
app = Flask(__name__)

customers = [
    {'id': 1, 'firstname': 'Paul', 'surname': 'Heath'},
    {'id': 2, 'firstname': 'Colin', 'surname': 'Trap'},
    {'id': 3, 'firstname': 'Lisa', 'surname': 'Noble'}
]

@app.route('/health')
def health():
    return 'Healthcheck status ok'

@app.route('/customers')
def get_customers():
    return jsonify(customers)

@app.route('/customers', methods=['POST'])    
def add_customer():
    customers.append(request.get_json())
    return '', 204

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id:int):
    global customers
    cust_to_delete = next(filter(lambda cust: cust['id'] == id, customers), None)
    if cust_to_delete:
        print(f'deleting customer {cust_to_delete}')
        customers.remove(cust_to_delete)
        return f'deleted customer with id {id}', 204
    else:
         return 'customer not found', 404
    