"""
User Management API
A simple Flask REST API for managing users with in-memory storage.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# ============================================================================
# In-memory user storage (dictionary)
# Keys are string user IDs, values are dictionaries with user details.
# Pre-populated with sample users for testing purposes.
# ============================================================================
users = {
    "1": {"id": "1", "name": "Ishita Sharma", "age": 22},
    "2": {"id": "2", "name": "Rahul Verma", "age": 25},
    "3": {"id": "3", "name": "Priya Patel", "age": 28},
}

# Auto-incrementing ID counter, starting after the sample users
next_id = 4


# ============================================================================
# Route: GET /
# Purpose: Returns a welcome message to confirm the API is running.
# ============================================================================
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({
        "message": "Welcome to the User Management API!",
        "endpoints": {
            "GET /users": "List all users",
            "GET /users/<id>": "Get a specific user",
            "POST /users": "Create a new user",
            "PUT /users/<id>": "Update a user",
            "DELETE /users/<id>": "Delete a user",
        }
    }), 200


# ============================================================================
# Route: GET /users
# Purpose: Returns a list of all users stored in the dictionary.
# ============================================================================
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify({
        "total_users": len(users),
        "users": list(users.values())
    }), 200


# ============================================================================
# Route: GET /users/<user_id>
# Purpose: Returns a specific user by their ID.
# Returns: 200 with user data if found, 404 if user does not exist.
# ============================================================================
@app.route("/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    # Look up the user in the dictionary
    user = users.get(user_id)

    if user is None:
        return jsonify({"error": f"User with ID '{user_id}' not found"}), 404

    return jsonify({"user": user}), 200


# ============================================================================
# Route: POST /users
# Purpose: Creates a new user from JSON input.
# Expects: JSON body with "name" (string) and "age" (integer).
# Returns: 201 with the created user data on success.
# ============================================================================
@app.route("/users", methods=["POST"])
def create_user():
    global next_id

    # Parse the incoming JSON request body
    data = request.get_json()

    # Validate that required fields are present
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Both 'name' and 'age' fields are required"}), 400

    # Build the new user object with an auto-generated ID
    user_id = str(next_id)
    new_user = {
        "id": user_id,
        "name": data["name"],
        "age": data["age"]
    }

    # Store the user and increment the ID counter
    users[user_id] = new_user
    next_id += 1

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201


# ============================================================================
# Route: PUT /users/<user_id>
# Purpose: Updates an existing user's data.
# Expects: JSON body with "name" and/or "age" fields to update.
# Returns: 200 with updated user data, or 404 if user not found.
# ============================================================================
@app.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    # Check if the user exists
    if user_id not in users:
        return jsonify({"error": f"User with ID '{user_id}' not found"}), 404

    # Parse the incoming JSON data
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must contain JSON data"}), 400

    # Update only the fields that are provided in the request
    if "name" in data:
        users[user_id]["name"] = data["name"]
    if "age" in data:
        users[user_id]["age"] = data["age"]

    return jsonify({
        "message": "User updated successfully",
        "user": users[user_id]
    }), 200


# ============================================================================
# Route: DELETE /users/<user_id>
# Purpose: Deletes a user from the dictionary by their ID.
# Returns: 200 with success message, or 404 if user not found.
# ============================================================================
@app.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Check if the user exists before attempting deletion
    if user_id not in users:
        return jsonify({"error": f"User with ID '{user_id}' not found"}), 404

    # Remove the user and capture their data for the response
    deleted_user = users.pop(user_id)

    return jsonify({
        "message": "User deleted successfully",
        "deleted_user": deleted_user
    }), 200


# ============================================================================
# Application entry point
# debug=True enables auto-reload on code changes and detailed error pages.
# ============================================================================
if __name__ == "__main__":
    app.run(debug=True)
