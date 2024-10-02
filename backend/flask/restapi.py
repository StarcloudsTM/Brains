from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 1200},
        {'id': 2, 'name': 'Phone', 'price': 800}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
