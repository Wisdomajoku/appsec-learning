#!/usr/bin/env python3
"""
Day 4 Lab: Backend Routing Architecture (Flask)
Demonstrating route mapping, dynamic parameter extraction, 
type converters, and endpoint authorization boundaries.
"""
from flask import Flask, jsonify, request

# BRICK 1: Initialize the Flask application
app = Flask(__name__)

# Mock database records in memory (simulating a database lookup)
MOCK_DATABASE = {
    101: {"username": "alice", "email": "alice@corp.local", "role": "engineer"},
    102: {"username": "bob", "email": "bob@corp.local", "role": "designer"},
    103: {"username": "charlie", "email": "charlie@corp.local", "role": "admin"}
}

MOCK_INVOICES = {
    5001: {"owner_id": 101, "amount": "$450.00", "description": "Cloud hosting"},
    5002: {"owner_id": 102, "amount": "$1,200.00", "description": "Design software license"}
}


# ENDPOINT 1: Static Route (Health Check)
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "online",
        "service": "AppSec User Management Service",
        "version": "1.0.0"
    }), 200


# ENDPOINT 2: Dynamic String Route (Untyped Parameter)
@app.route("/profile/<username>", methods=["GET"])
def get_user_by_name(username):
    """
    Accepts ANY arbitrary string in the URL path.
    Notice: If an attacker sends /profile/../../etc/passwd, Flask matches this route.
    """
    return jsonify({
        "matched_route": "/profile/<username>",
        "extracted_parameter": username,
        "type": str(type(username))
    }), 200


# ENDPOINT 3: Dynamic Typed Route (Integer Converter Defense)
@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    """
    Enforces that user_id MUST be an integer at the routing layer.
    If the client passes non-digits (e.g. /users/abc), Flask returns 404 immediately.
    """
    user_record = MOCK_DATABASE.get(user_id)
    
    if not user_record:
        return jsonify({"error": f"User ID {user_id} not found"}), 404

    return jsonify({
        "user_id": user_id,
        "data": user_record
    }), 200


# ENDPOINT 4: Architectural Flaw Demonstration (Missing Authorization Check)
@app.route("/api/v1/invoices/<int:invoice_id>", methods=["GET"])
def get_invoice(invoice_id):
    """
    VULNERABILITY PREVIEW: Insecure Direct Object Reference (IDOR).
    Notice what is missing:
    The code extracts invoice_id and fetches it, but NEVER checks:
    "Does the logged-in user actually OWN this invoice?"
    """
    invoice = MOCK_INVOICES.get(invoice_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404
        
    return jsonify({
        "invoice_id": invoice_id,
        "details": invoice
    }), 200


if __name__ == "__main__":
    print("[*] Starting AppSec Flask Server on http://127.0.0.1:5000")
    print("[*] Press Ctrl+C to stop the server.")
    app.run(host="127.0.0.1", port=5000, debug=False)
