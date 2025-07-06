# Catalog Service

from flask import Flask, jsonify

app = Flask(__name__)

# Simple in-memory database
db = {
    100: {"name": "Laptop", "price": 1200},
    101: {"name": "Mouse", "price": 25}
}

@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = db.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    # Runs on port 5002
    app.run(port=5002, debug=True)
