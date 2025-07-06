# Order Service

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# In a real scenario, the user service URL would come from a config file or service discovery
USER_SERVICE_URL = "http://127.0.0.1:5001"

@app.route("/orders", methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    # Call the user service to verify the user exists
    try:
        user_response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        user_response.raise_for_status() # Raises an exception for 4xx or 5xx status codes
        user_data = user_response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "User service is unavailable or user not found", "details": str(e)}), 503

    # If user is found, proceed to create the order (simplified)
    print(f"User {user_data['name']} verified. Creating order...")
    # ... order creation logic here ...

    return jsonify({"status": "Order created", "user": user_data}), 201

if __name__ == '__main__':
    # Runs on port 5003
    app.run(port=5003, debug=True)
