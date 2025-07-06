# User Service

from flask import Flask, jsonify

app = Flask(__name__)

# Simple in-memory database
db = {
    1: {"name": "Alice"},
    2: {"name": "Bob"}
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = db.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    # Runs on port 5001
    app.run(port=5001, debug=True)
