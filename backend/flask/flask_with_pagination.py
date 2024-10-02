from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/products')
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    products = Product.query.paginate(page, per_page, error_out=False)
    return jsonify([{'id': p.id, 'name': p.name} for p in products.items])

if __name__ == '__main__':
    app.run(debug=True)
