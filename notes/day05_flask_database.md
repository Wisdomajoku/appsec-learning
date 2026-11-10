# Day 5: Flask State Handling & Database Flow (SQLite)

**Date:** November 10, 2026  
**Focus:** Flask `request` context, SQLite integration, parameterization mechanics, Source-to-Sink tracing, and HTTP method safety.

---

## 1. The Database Sink: Code vs. Data Separation
* **The Vulnerability (SQL Injection):** Using string concatenation (f-strings, `.format()`, `%s`) combines developer SQL instructions and untrusted user input into a single channel. The SQL compiler cannot distinguish between the query structure and user data.
* **The Defense (Parameterized Queries):** `cursor.execute("SELECT ... WHERE col = ?", (param,))` separates query structure from user input into two isolated channels:
  1. The SQL template is pre-compiled into a fixed execution plan.
  2. The parameters are passed strictly as literal values, rendering injection syntax inert.

---

## 2. Source-to-Sink Data Flow
* **Source:** `request.args.get("department")` (untrusted query parameter entering from the network).
* **Transformation:** Python extraction, stripping, and packaging into a tuple.
* **Sink:** `cursor.execute(query, (department,))` (the interface where Python passes data to the underlying database engine).

---

## 3. Safe Methods vs. State Mutation Risks (RFC 9110)
* **`GET` (Safe & Idempotent):** Intended strictly for read-only operations. Must never modify database state.
* **Risks of State-Changing `GET` Requests:**
  1. **CSRF via Zero-Scripting:** Can be triggered via simple HTML tags (`<img src="...">`, `<link>`) on third-party sites without needing JavaScript.
  2. **Accidental Execution:** Web crawlers, search engine indexers, and browser prefetching engines automatically follow `GET` links, causing accidental mass deletion or modification.
  3. **Credential & Sensitive Data Leakage:** Query strings are saved in plaintext across browser history, server access logs, and HTTP `Referer` headers.
