# We are using Flask, a lightweight web framework, to act as our API Gateway
# and to serve the frontend files for now.
from flask import Flask, send_from_directory, jsonify

print("!!! Running the LATEST version of app.py !!!")

# Initialize the Flask application
# We tell Flask where to find the static frontend files.
# The '..' means go up one directory from 'api-gateway' to the project root,
# then into the 'frontend' folder.
app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# --- HTML Serving Routes ---

# This route serves the main homepage (index.html)
@app.route('/')
def index():
    # send_from_directory will securely find and send the file.
    return send_from_directory(app.static_folder, 'index.html')

# This is a "catch-all" route. It will serve any other .html file from the frontend folder.
# This allows us to navigate to /product.html, /about.html etc.
@app.route('/<path:filename>')
def serve_html(filename):
    # We ensure the filename ends with .html for security
    if filename.endswith(".html"):
        return send_from_directory(app.static_folder, filename)
    else:
        # We return a 404 Not Found error for any other direct path requests.
        return "File not found", 404

# --- FAKE API ROUTES (Temporary for Frontend Development) ---

# This route will act as our temporary API endpoint for a single product.
# It simulates fetching one product by its ID.
@app.route('/api/v1/products/<product_id>')
def get_product_detail(product_id):
    # In a real application, you would query your database for this ID.
    # For now, we return a hardcoded "fake" product.
    print(f"API called for product ID: {product_id}") # A print statement to help with debugging
    fake_product = {
        "id": product_id,
        "name": "Vintage Inspired T-Shirt",
        "price": 39.99,
        "description": "A classic t-shirt with a vintage look and feel. Made from 100% organic cotton for ultimate comfort.",
        "category": "T-Shirts",
        "images": [
            "images/product-detail-01.jpg",
            "images/product-detail-02.jpg",
            "images/product-detail-03.jpg"
        ]
    }
    return jsonify(fake_product)

# This route will act as our temporary API for the list of all products.
# It simulates fetching all products for the main shop page.
@app.route('/api/v1/products')
def get_all_products():
    # In a real application, this would fetch from your database.
    print("API called for all products") # A print statement for debugging
    fake_products_list = [
        {"id": "101", "name": "Esprit Ruffle Shirt", "price": 16.64, "image": "images/product-01.jpg"},
        {"id": "102", "name": "Herschel supply", "price": 35.31, "image": "images/product-02.jpg"},
        {"id": "103", "name": "Classic Trench Coat", "price": 75.00, "image": "images/product-03.jpg"},
        {"id": "104", "name": "Front Pocket Jumper", "price": 34.75, "image": "images/product-04.jpg"},
        {"id": "105", "name": "Front-Zip Sweatshirt", "price": 29.50, "image": "images/product-05.jpg"},
        {"id": "106", "name": "Black T-Shirt", "price": 18.99, "image": "images/product-06.jpg"}
    ]
    return jsonify(fake_products_list)

# This is the standard Python entry point.
# THIS MUST BE THE LAST THING IN THE FILE.
if __name__ == '__main__':
    # We run the app in debug mode on port 5000.
    # Debug mode automatically reloads the server when you save changes.
    app.run(port=5000, debug=True)