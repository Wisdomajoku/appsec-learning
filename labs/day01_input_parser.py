#!/usr/bin/env python3
"""
Day 1 Lab: Defensive Request Parser
Demonstrating safe handling of untrusted dictionaries, type coercion,
and exception handling in Python.
"""
import json

def parse_incoming_request(raw_payload: str) -> dict:
    """
    Simulates parsing and validating an incoming user profile update.
    Untrusted input must be checked for:
    1. Valid JSON syntax
    2. Proper data types
    3. Absence of unauthorized privilege escalation
    """
    # 1. Safe JSON parsing with exception handling
    try:
        data = json.loads(raw_payload)
    except json.JSONDecodeError as err:
        return {
            "status": 400,
            "error": "Malformed JSON payload",
            "details": f"Decode error at line {err.lineno}, column {err.colno}"
        }

    # 2. Structure validation: Ensure root is a dictionary (not a bare list or int)
    if not isinstance(data, dict):
        return {
            "status": 400,
            "error": "Invalid payload format: Expected a JSON object"
        }

    # 3. Safe key extraction (avoiding KeyError)
    username = data.get("username")
    user_id = data.get("user_id")
    is_admin = data.get("is_admin", False)

    # 4. Input validation and type enforcement
    if not username or not isinstance(username, str):
        return {"status": 422, "error": "Field 'username' must be a non-empty string"}

    # Validate user_id must be a positive integer
    if not isinstance(user_id, int) or user_id <= 0:
        return {"status": 422, "error": "Field 'user_id' must be a positive integer"}

    # 5. Type coercion vulnerability defense:
    # If the attacker passes a string "false" or "False", bool("false") in Python is True!
    # Enforce strict boolean type checking:
    if not isinstance(is_admin, bool):
        return {"status": 422, "error": "Field 'is_admin' must be a boolean (true/false)"}

    # If all checks pass:
    return {
        "status": 200,
        "message": "Payload validated successfully",
        "validated_user": {
            "username": username.strip(),
            "user_id": user_id,
            "is_admin": is_admin
        }
    }


def run_security_test_cases():
    """
    Test suite containing both benign payloads and hostile test cases.
    """
    test_cases = [
        # Test 1: Valid benign payload
        ('{"username": "alice", "user_id": 101, "is_admin": false}', "Benign User"),
        
        # Test 2: Malformed JSON syntax (missing quote / truncated request)
        ('{"username": "bob", "user_id": 102,', "Syntax Crash Payload"),
        
        # Test 3: Type confusion (user_id as string instead of integer)
        ('{"username": "charlie", "user_id": "103", "is_admin": false}', "Type Confusion user_id"),
        
        # Test 4: String-to-boolean bypass attempt ("false" as a string)
        ('{"username": "david", "user_id": 104, "is_admin": "false"}', "Boolean String Bypass"),
        
        # Test 5: Root type anomaly (passing a raw list instead of a JSON object)
        ('[1, 2, 3]', "Array Smuggling / Root Object Anomaly"),
        
        # Test 6: Missing required fields
        ('{"is_admin": true}', "Missing Username & User ID")
    ]

    print("=" * 60)
    print("RUNNING APPSEC INPUT PARSER TEST SUITE")
    print("=" * 60)

    for i, (payload, description) in enumerate(test_cases, 1):
        print(f"\n[Test {i}] Case: {description}")
        print(f"Payload: {payload}")
        result = parse_incoming_request(payload)
        print(f"Response (HTTP {result['status']}): {result}")

    print("\n" + "=" * 60)
    print("ALL TEST CASES PROCESSED DEFENSIVELY (ZERO UNCAUGHT CRASHES)")
    print("=" * 60)


if __name__ == "__main__":
    run_security_test_cases()
