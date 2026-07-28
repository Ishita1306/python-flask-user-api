# 🚀 User Management API

A simple and lightweight RESTful API built with **Python Flask** for managing users. This API uses an in-memory dictionary for data storage, making it ideal for learning REST concepts, prototyping, and testing.

---

## 📋 Project Overview

This project demonstrates how to build a complete CRUD (Create, Read, Update, Delete) REST API using Flask. Users are stored in a Python dictionary — no database setup required. The API comes pre-loaded with sample users so you can start testing immediately.

---

## ✨ Features

- **Full CRUD Operations** — Create, Read, Update, and Delete users
- **In-Memory Storage** — Fast, zero-configuration data storage using a Python dictionary
- **JSON API** — All requests and responses use JSON format
- **Input Validation** — Proper error handling for missing fields and invalid IDs
- **Proper HTTP Status Codes** — 200, 201, 400, and 404 responses
- **Sample Data** — Pre-loaded with 3 sample users for immediate testing
- **Debug Mode** — Auto-reload on code changes during development

---

## 📁 Project Structure

```
python-flask-user-api/
│
├── app.py              # Main Flask application with all routes
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

---

## 🔗 API Endpoints

| Method   | Endpoint            | Description              | Status Code |
|----------|---------------------|--------------------------|-------------|
| `GET`    | `/`                 | Welcome message          | 200         |
| `GET`    | `/users`            | Get all users            | 200         |
| `GET`    | `/users/<user_id>`  | Get a specific user      | 200 / 404   |
| `POST`   | `/users`            | Create a new user        | 201 / 400   |
| `PUT`    | `/users/<user_id>`  | Update an existing user  | 200 / 404   |
| `DELETE` | `/users/<user_id>`  | Delete a user            | 200 / 404   |

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ishita1306/python-flask-user-api.git
   cd python-flask-user-api
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

```bash
python app.py
```

The server will start at **http://127.0.0.1:5000** with debug mode enabled.

You should see output similar to:
```
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
```

---

## 📬 Example API Requests

You can test the API using **Postman**, **cURL**, or any HTTP client.

### 1. GET `/` — Welcome Message

**Request:**
```
GET http://127.0.0.1:5000/
```

**Response (200):**
```json
{
    "message": "Welcome to the User Management API!",
    "endpoints": {
        "GET /users": "List all users",
        "GET /users/<id>": "Get a specific user",
        "POST /users": "Create a new user",
        "PUT /users/<id>": "Update a user",
        "DELETE /users/<id>": "Delete a user"
    }
}
```

---

### 2. GET `/users` — Get All Users

**Request:**
```
GET http://127.0.0.1:5000/users
```

**Response (200):**
```json
{
    "total_users": 3,
    "users": [
        {"id": "1", "name": "Ishita Sharma", "age": 22},
        {"id": "2", "name": "Rahul Verma", "age": 25},
        {"id": "3", "name": "Priya Patel", "age": 28}
    ]
}
```

---

### 3. GET `/users/1` — Get a Specific User

**Request:**
```
GET http://127.0.0.1:5000/users/1
```

**Response (200):**
```json
{
    "user": {
        "id": "1",
        "name": "Ishita Sharma",
        "age": 22
    }
}
```

**If user not found (404):**
```json
{
    "error": "User with ID '99' not found"
}
```

---

### 4. POST `/users` — Create a New User

**Request:**
```
POST http://127.0.0.1:5000/users
Content-Type: application/json

{
    "name": "Amit Kumar",
    "age": 30
}
```

**Response (201):**
```json
{
    "message": "User created successfully",
    "user": {
        "id": "4",
        "name": "Amit Kumar",
        "age": 30
    }
}
```

---

### 5. PUT `/users/1` — Update a User

**Request:**
```
PUT http://127.0.0.1:5000/users/1
Content-Type: application/json

{
    "name": "Ishita Sharma Updated",
    "age": 23
}
```

**Response (200):**
```json
{
    "message": "User updated successfully",
    "user": {
        "id": "1",
        "name": "Ishita Sharma Updated",
        "age": 23
    }
}
```

---

### 6. DELETE `/users/2` — Delete a User

**Request:**
```
DELETE http://127.0.0.1:5000/users/2
```

**Response (200):**
```json
{
    "message": "User deleted successfully",
    "deleted_user": {
        "id": "2",
        "name": "Rahul Verma",
        "age": 25
    }
}
```

---

## 🧪 Testing with cURL

```bash
# Welcome
curl http://127.0.0.1:5000/

# Get all users
curl http://127.0.0.1:5000/users

# Get user by ID
curl http://127.0.0.1:5000/users/1

# Create a new user
curl -X POST http://127.0.0.1:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Amit Kumar", "age": 30}'

# Update a user
curl -X PUT http://127.0.0.1:5000/users/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Ishita Updated", "age": 23}'

# Delete a user
curl -X DELETE http://127.0.0.1:5000/users/2
```

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
