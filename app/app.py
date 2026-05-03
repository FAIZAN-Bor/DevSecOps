from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob",   "role": "developer"},
]

# You accidentally hardcode a password
SECRET_KEY = "mypassword123"
db_password = "admin@123"

@app.route("/")
def home():
    return jsonify({
        "message": "DevSecOps Demo App",
        "version": "1.0.0",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users}), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)