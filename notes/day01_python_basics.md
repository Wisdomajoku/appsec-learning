# Day 1: Python Fundamentals & The Input Validation Boundary

**Date:** October 12, 2026  
**Focus:** Data types, dictionaries, truthiness, type confusion, and exception handling.

---

## 1. Vulnerability Mechanism: Python Truthiness & Type Confusion
* **What it is:** Python evaluates the boolean value of an object using truthiness. All non-empty strings (`"false"`, `"0"`, `"null"`) evaluate to `True`.
* **The Flaw:** Developers often write `if data.get("is_admin"):` expecting a boolean, but incoming network requests may contain string representations.
* **How it is exploited:** An attacker submits `{"is_admin": "false"}`. Python checks the truthiness of `"false"`, returns `True`, and grants elevated privileges.
* **Remediation:** Strict type validation (`isinstance(val, bool)`) or schema validation before business logic processes the input.

---

## 2. Unhandled Exceptions: Missing Keys & Syntax Errors
* **The Mechanism:** Accessing a non-existent dictionary key directly (`data["token"]`) raises a `KeyError`. Malformed JSON strings raise `json.JSONDecodeError`.
* **The Impact:**
  1. **Information Disclosure (CWE-209):** In debug mode, unhandled crashes dump stack traces, internal paths, and environment variables to the client.
  2. **Denial of Service (CWE-400):** Server returns HTTP 500 and aborts worker execution.
* **Remediation:** Use `data.get("key", default)` for optional parameters, wrap ingestion in `try/except`, and implement global error handlers that log internally and return generic error messages.

---

## 3. Defensive Layering Pattern
Every web service ingesting untrusted input must enforce three strict boundaries:
1. **Ingestion Shield:** Validate syntax (`try/except json.JSONDecodeError`).
2. **Structural Validation:** Confirm container shape (`isinstance(data, dict)`).
3. **Type & Range Enforcement:** Confirm primitive types (`isinstance(id, int)` and `id > 0`) before passing data to business logic.
