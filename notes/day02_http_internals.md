# Day 2: HTTP Protocol Internals & The Wire Format

**Date:** October 22, 2026  
**Focus:** HTTP/1.1 wire anatomy, CRLF boundaries, Host header routing, and cookie flags.

---

## 1. The Wire Format & Delimiters
* **Mechanism:** HTTP/1.1 is plain-text ASCII transmitted over a TCP socket. Lines terminate with CRLF (`\r\n`).
* **The Boundary:** Headers and body are strictly separated by a double CRLF (`\r\n\r\n`).
* **Security Risk (HTTP Response Splitting):** If user-controlled input is reflected into HTTP response headers without sanitization, an attacker injecting `\r\n\r\n` can terminate headers early and inject an arbitrary payload into the response body (XSS or cache poisoning).

---

## 2. Host Header & Virtual Hosting
* **Mechanism:** Introduced in HTTP/1.1 to enable multiple domain names (virtual hosts) to run on a single IP address. Omission results in `400 Bad Request`.
* **Security Risk (Host Header Injection):** If an application constructs password reset links or absolute URLs using the incoming `Host` header without a whitelist, an attacker can manipulate the header (`Host: attacker-controlled.com`) to harvest sensitive reset tokens or poison web caches.

---

## 3. State Management & Cookie Security Flags
HTTP is stateless. State is maintained via the `Cookie` and `Set-Cookie` headers.
* **`HttpOnly`:** Prevents client-side scripts from reading `document.cookie` (mitigates direct token theft via XSS).
  * *Limitation (Session Riding):* Even with `HttpOnly`, an attacker with XSS can still issue authenticated requests using `fetch()` because the browser automatically attaches the cookie behind the scenes.
* **`Secure`:** Ensures cookies are transmitted exclusively over encrypted TLS (`https://`), mitigating passive MitM eavesdropping.
* **`SameSite`:** Restricts cross-site cookie transmission (`Strict`, `Lax`, `None`), mitigating Cross-Site Request Forgery (CSRF).

---

## 4. Socket Diagnostics: Errno 111 vs Errno 104
* **`[Errno 111] Connection refused`:** Layer 4 TCP failure. Port is closed; kernel sends `RST` on initial `SYN`.
* **`[Errno 104] Connection reset by peer`:** TCP handshake succeeded, but the peer server prematurely closed or reset the connection during data transfer (e.g., service boot latency, WAF drop, or backend crash).
* **CWE-209 Lesson:** Uncaught socket exceptions leak local paths (`/home/mazi/...`), usernames, and file names via tracebacks.
