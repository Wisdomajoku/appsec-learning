# Day 6: End-to-End Request Tracing & Week 1 Synthesis

**Date:** November 17, 2026  
**Focus:** The 7-stage HTTP request lifecycle, authentication header ingestion, data-level filters vs. access control, and SQLite thread safety.

---

## 1. The 7-Stage Request Lifecycle
1. **The Wire:** Raw ASCII bytes over TCP (`\r\n` line endings, `\r\n\r\n` boundary).
2. **Reverse Proxy:** TLS termination, host routing, rate limiting.
3. **Framework Router:** Pattern matching via URL Map, pre-execution converter filtering (`<int:id>`).
4. **Ingestion (The Source):** Parsing raw bytes into `request.args`, `request.headers`, and `request.json`.
5. **Transformation:** Auth verification, type validation, schema checks.
6. **Execution (The Sink):** Passing data to external interpreters (SQL, shell, filesystem).
7. **Serialization:** Converting records to JSON and transmitting HTTP status/headers back over TCP.

---

## 2. Access-Control Checks vs. Data-Level Filters
* **Access-Control Check:** Explicit authorization evaluation (`if not user.is_admin: return 403`). Halts execution immediately.
* **Data-Level Filter:** Scoping logic injected directly into the data query (`WHERE account_id = ? AND is_confidential = 0`). Returns an empty result set (`records_count: 0`) with HTTP 200, preventing data leakage while mitigating resource enumeration side-channels.

---

## 3. Concurrency & Database Connection Lifecycle
* **Mechanism:** Multithreaded web servers (Flask/Werkzeug) spawn separate threads per request.
* **Failure Mode (CWE-362):** SQLite connections created in the main application thread throw `ProgrammingError` when accessed by request worker threads, resulting in unhandled HTTP 500 errors.
* **Remediation:** Manage database connections per request context or enable thread sharing in development (`check_same_thread=False`).
