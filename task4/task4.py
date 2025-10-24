from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory users data
users = {
    "1": {"name": "Achyuta", "email": "achyuta@example.com"},
    "2": {"name": "Ajay", "email": "ajay@example.com"}
}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# GET single user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# POST add user
@app.route('/users', methods=['POST'])
def add_user():
    # Safely parse JSON
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON or missing Content-Type"}), 400

    # Safe key access
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    # Generate new user ID
    new_id = str(max([int(k) for k in users.keys()]) + 1 if users else 1)
    users[new_id] = {"name": name, "email": email}

    return jsonify({"message": "User added", "user": users[new_id]}), 201

# PUT update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON or missing Content-Type"}), 400

    # Update only valid keys
    users[user_id].update({k: v for k, v in data.items() if k in ["name", "email"]})
    return jsonify({"message": "User updated", "user": users[user_id]})

# DELETE user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": f"User {user_id} deleted"})

# Run Flask app
if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5000",debug=True)