# Day 4: Backend Routing Architecture & Authorization Boundaries

**Date:** October 29, 2026  
**Focus:** Flask routing engine, URL map matching, parameter converters, and the IDOR mechanism.

---

## 1. The Routing Boundary: Pre-Execution Filtering
* **Mechanism:** When a route uses a type converter like `<int:param>`, Flask's routing engine enforces regex matching (`^\d+$`) *before* triggering the view function.
* **Security Value:** If non-digits are submitted (`/users/admin`), Flask rejects the request with a generic `404 Not Found` at the framework layer. The Python view function never executes, shielding business logic from injection and type confusion attacks.
* **Timing Attack Side-Channel:** Rejection at the routing layer responds faster (~1-2 ms) than rejection inside a function (~15-30 ms), allowing attackers to infer routing structure via statistical latency analysis.

---

## 2. Parameter Types: Integer Enumeration vs. UUIDs
* **Untyped Strings (`<username>`):** Vulnerable to path traversal (`../`), SQL injection fragments, and unvalidated character sets unless sanitized manually.
* **Sequential Integers (`<int:id>`):** Solves type safety, but exposes the application to mass enumeration / scraping by iterating through IDs.
* **UUIDv4 (`<uuid:id>`):** High-entropy 128-bit identifiers eliminate predictable enumeration, though they do not replace access control checks.

---

## 3. IDOR / BOLA (Insecure Direct Object Reference)
* **The Vulnerability:** Occurs when an endpoint takes an object ID directly from untrusted input (the **Source**) and retrieves the resource from storage (the **Sink**) without validating that the authenticated user owns or has permission to access that resource.
* **The Root Cause:** Confusing *resource existence* (`if invoice exists`) with *resource authorization* (`if invoice.owner == current_user`).
* **Remediation:** Enforce ownership validation at the function layer:
  ```python
  if invoice.owner_id != current_user.id:
      return jsonify({"error": "Forbidden"}), 403
