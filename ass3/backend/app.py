from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Allow CORS for frontend requests

# Hardcoded user credentials (replace these with your actual credentials)
users = {
    "user1": {
        "username": "user1",
        "password": "123"
    }
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Get JSON data from request body
    username = data.get("username")
    password = data.get("password")

    if not username and not password:
        return jsonify({"message": "Username and password are required"}), 400

    if not username:
        return jsonify({"message": "Username Required"}), 401

    if not password :
        return jsonify({"message": "Password Required"}), 401

    return jsonify({'message': 'Login successful'})

if __name__ == '__main__':
    app.run(debug=True)
