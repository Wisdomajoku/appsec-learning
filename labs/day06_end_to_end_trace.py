#!/usr/bin/env python3
"""
Day 6 Lab: End-to-End Request Tracing Engine
Demonstrates the full 7-stage lifecycle of an HTTP request:
Raw Network Bytes -> Header Ingestion -> Auth Middleware -> Routing ->
Parameter Extraction -> Database Query Sink -> JSON Serialization.
"""
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE financial_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id TEXT NOT NULL,
            client_name TEXT NOT NULL,
            balance INTEGER NOT NULL,
            is_confidential INTEGER NOT NULL
        )
    """)
    records = [
        ("ACC-101", "Acme Corp", 540000, 0),
        ("ACC-102", "Cyberdyne Systems", 1250000, 1),
        ("ACC-103", "Stark Industries", 890000, 0),
        ("ACC-104", "Wayne Enterprises", 3400000, 1)
    ]
    cursor.executemany("""
        INSERT INTO financial_records (account_id, client_name, balance, is_confidential)
        VALUES (?, ?, ?, ?)
    """, records)
    conn.commit()
    return conn

db_conn = init_db()

# Simulated API Key Vault
VALID_API_KEYS = {
    "key-analyst-99": {"role": "analyst", "can_read_confidential": False},
    "key-admin-01": {"role": "admin", "can_read_confidential": True}
}

# --- MIDDLEWARE / HELPER ---
def authenticate_request():
    """
    Validates Stage 4/5: Inspects incoming HTTP headers for authentication.
    """
    api_key = request.headers.get("X-API-Key")
    if not api_key or api_key not in VALID_API_KEYS:
        return None
    return VALID_API_KEYS[api_key]


# --- ENDPOINT 1: Parameterized Data Retrieval ---
@app.route("/api/v1/records", methods=["GET"])
def get_records():
    """
    Trace: GET /api/v1/records?account=ACC-101
    """
    # 1. Ingestion: Header Auth
    user_context = authenticate_request()
    if not user_context:
        return jsonify({"error": "Unauthorized: Missing or invalid X-API-Key header"}), 401

    # 2. Ingestion: Query Parameters (The Source)
    account_filter = request.args.get("account")
    
    cursor = db_conn.cursor()
    
    # 3. Authorization Boundary & Sink Execution
    if not user_context["can_read_confidential"]:
        # Analysts only see non-confidential records
        if account_filter:
            query = "SELECT account_id, client_name, balance FROM financial_records WHERE account_id = ? AND is_confidential = 0"
            cursor.execute(query, (account_filter,))
        else:
            query = "SELECT account_id, client_name, balance FROM financial_records WHERE is_confidential = 0"
            cursor.execute(query)
    else:
        # Admins see all records
        if account_filter:
            query = "SELECT account_id, client_name, balance FROM financial_records WHERE account_id = ?"
            cursor.execute(query, (account_filter,))
        else:
            query = "SELECT account_id, client_name, balance FROM financial_records"
            cursor.execute(query)

    rows = cursor.fetchall()
    return jsonify({
        "caller_role": user_context["role"],
        "records_count": len(rows),
        "data": [dict(r) for r in rows]
    }), 200


# --- ENDPOINT 2: Audit Query Preview (Flawed Endpoint) ---
@app.route("/api/v1/audit-preview", methods=["GET"])
def audit_preview():
    """
    Educational inspection endpoint demonstrating parameter reflection and SQL sinks.
    """
    account = request.args.get("account", "ALL")
    
    # Flawed architectural pattern: manual query formatting string
    debug_query = f"SELECT * FROM financial_records WHERE account_id = '{account}'"
    
    return jsonify({
        "debug_sql_statement": debug_query,
        "source_received": account,
        "headers_received": dict(request.headers)
    }), 200


if __name__ == "__main__":
    print("[*] Day 6 End-to-End Tracing Server listening on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
