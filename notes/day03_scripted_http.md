# Day 3: Scripted HTTP Automation & Proxy Interception

**Date:** October 23, 2026  
**Focus:** Programmatic HTTP requests with Python `requests`, Burp Suite proxy routing, TLS interception mechanics, and session persistence.

---

## 1. TLS Interception & Certificate Validation (CWE-295)
* **Mechanism:** Burp Suite intercepts HTTPS connections as a Man-in-the-Middle (MitM), signing forged certificates using its own custom CA. Python rejects this by default with `SSLError: CERTIFICATE_VERIFY_FAILED`.
* **The Lab Workaround:** `session.verify = False` disables certificate chain validation, allowing the script to communicate through the local proxy.
* **Production Risk:** Disabling TLS verification in production code exposes the client to network-level eavesdropping and session hijacking via rogue proxies or ARP/DNS spoofing (CWE-295).

---

## 2. Session Persistence vs. Ad-Hoc Requests
* **Mechanism:** Standalone calls (`requests.get()`, `requests.post()`) are stateless and discard `Set-Cookie` headers immediately after completion.
* **The Solution:** `requests.Session()` maintains an internal cookie jar, automatically attaching session cookies to subsequent requests across multi-step authentication or exploit workflows.
* **Performance:** Sessions maintain persistent TCP connections (HTTP Keep-Alive), significantly accelerating automated testing scripts.

---

## 3. The AppSec Value of Script Proxying
* **Granular Observability:** Eliminates the "black-box scripting trap" by displaying the exact raw bytes emitted by automation.
* **Rapid Triage:** Enables sending automated requests directly to Burp **Repeater** (`Ctrl+R`) to isolate and manipulate payloads manually without altering script code.
* **Fidelity:** Bypasses browser-enforced sanitization and header restrictions, providing full control over the wire format.
