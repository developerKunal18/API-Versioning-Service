from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 65000, "category": "electronics"},
    {"id": 2, "name": "Keyboard", "price": 1800, "category": "accessories"},
    {"id": 3, "name": "Mouse", "price": 900, "category": "accessories"},
]

def get_products():
    return PRODUCTS

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/v1/products")
def products_v1():
    return jsonify({"version": "v1", "products": get_products()})

@app.get("/api/v2/products")
def products_v2():
    products = get_products()
    return jsonify({
        "version": "v2",
        "count": len(products),
        "data": [{**product, "currency": "INR"} for product in products],
    })

@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "resource_not_found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
