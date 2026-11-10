#!/usr/bin/env python3
"""
Day 5 Lab: Flask State Handling & Database Flow (SQLite)
Demonstrating request context inspection, database connection lifecycles,
and the boundary between string formatting and parameterized queries.
"""
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_FILE = ":memory:" # Use in-memory SQLite for ephemeral lab testing

def get_db_connection():
    """
    Creates a new connection to the database.
    Setting row_factory = sqlite3.Row allows column access by name (like a dictionary).
    """
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """
    Seeds the in-memory database with tables and baseline records.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
    """)
    
    # Insert baseline records
    seed_data = [
        ("alice", "Engineering", 120000),
        ("bob", "Design", 95000),
        ("charlie", "Engineering", 130000),
        ("david", "Finance", 110000)
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO employees (username, department, salary)
        VALUES (?, ?, ?)
    """, seed_data)
    
    conn.commit()
    return conn

# Global database connection for persistent in-memory access during the session
db_conn = init_database()


# ENDPOINT 1: Safe Query Parameter Search (Parameterized Sink)
@app.route("/api/v1/employees", methods=["GET"])
def search_employees():
    """
    SOURCE: request.args (Query parameter ?department=...)
    TRANSFORMATION: Extraction and validation
    SINK: Parameterized cursor.execute()
    """
    # 1. Source: Extract untrusted query parameter
    department = request.args.get("department")
    
    cursor = db_conn.cursor()
    
    if department:
        # DEFENSIVE PATTERN: SQL structure separated from untrusted data
        query = "SELECT id, username, department FROM employees WHERE department = ?"
        # Notice: Data passed as a tuple: (department,)
        cursor.execute(query, (department,))
    else:
        # If no filter provided, return all
        cursor.execute("SELECT id, username, department FROM employees")
        
    rows = cursor.fetchall()
    
    # Convert Row objects to standard dictionaries for JSON serialization
    results = [dict(row) for row in rows]
    
    return jsonify({
        "count": len(results),
        "filter_applied": department,
        "employees": results
    }), 200


# ENDPOINT 2: Safe JSON Ingestion & Database Insertion
@app.route("/api/v1/employees", methods=["POST"])
def add_employee():
    """
    SOURCE: request.get_json() (JSON body)
    TRANSFORMATION: Structure validation, type validation
    SINK: Parameterized INSERT INTO query
    """
    # 1. Source: Parse JSON body defensively
    body = request.get_json()
    if not isinstance(body, dict):
        return jsonify({"error": "Malformed request: Expected a JSON object"}), 400
        
    username = body.get("username")
    department = body.get("department")
    salary = body.get("salary")
    
    # 2. Validation boundary (Layer 4 from Day 1)
    if not username or not isinstance(username, str):
        return jsonify({"error": "Invalid or missing 'username'"}), 422
    if not department or not isinstance(department, str):
        return jsonify({"error": "Invalid or missing 'department'"}), 422
    if not isinstance(salary, int) or salary <= 0:
        return jsonify({"error": "Field 'salary' must be a positive integer"}), 422
        
    # 3. Sink: Parameterized INSERT statement
    cursor = db_conn.cursor()
    try:
        query = "INSERT INTO employees (username, department, salary) VALUES (?, ?, ?)"
        cursor.execute(query, (username.strip(), department.strip(), salary))
        db_conn.commit()
        new_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        return jsonify({"error": f"Employee '{username}' already exists"}), 409
        
    return jsonify({
        "status": "success",
        "message": f"Employee created with ID {new_id}",
        "record": {"id": new_id, "username": username, "department": department}
    }), 201


# ENDPOINT 3: Architectural Comparison (Unsafe Construction vs Parameterized)
@app.route("/api/v1/debug-query", methods=["GET"])
def debug_query_comparison():
    """
    Educational endpoint demonstrating the exact SQL string produced by
    string concatenation vs. parameterized queries.
    """
    untrusted_input = request.args.get("input", "Engineering")
    
    # 1. What string concatenation does:
    concatenated_sql = f"SELECT * FROM employees WHERE department = '{untrusted_input}';"
    
    # 2. What parameterization does:
    parameterized_template = "SELECT * FROM employees WHERE department = ?;"
    parameter_tuple = (untrusted_input,)
    
    return jsonify({
        "untrusted_source": untrusted_input,
        "concatenated_string_result": concatenated_sql,
        "parameterized_architecture": {
            "immutable_query_template": parameterized_template,
            "isolated_data_channel": parameter_tuple
        },
        "appsec_takeaway": "Notice how concatenation makes the user input part of the SQL syntax itself."
    }), 200


if __name__ == "__main__":
    print("[*] Starting Day 5 Database-Backed Flask API on http://127.0.0.1:5000")
    print("[*] Press Ctrl+C to stop.")
    app.run(host="127.0.0.1", port=5000, debug=False)
