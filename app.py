from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS

# Define the /products route
@app.route('/products', methods=['GET'])
def get_products():
    # Return a JSON array of product objects
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

# Start the Flask server
if __name__ == '__main__':
    port = int(os.getenv('PORT', 3030))  # Get the port from environment or default to 3030
    app.run(host='0.0.0.0', port=port)
