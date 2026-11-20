# AppSec Progress Tracker

**Companion file:** `appsec-16-week-plan.md` (frozen plan). This file records what I have *demonstrated*. Do not copy plan content in here.

**Update rhythm:** weekly (end of the week). Session log after each session. Not daily ticking.

**Tick rule:** a box is ticked only when the skill is demonstrated through explanation, code, lab work, source review, practical testing, or other concrete evidence.

---

## Program

**Program:** AppSec Deep Proficiency  
**Duration:** 16 weeks  
**Target pace:** 4 hours/day, 6 days/week  
**Start date:** October 8, 2026  
**Status:** In Progress  

---

# Current Position

**Week:** 2  
**Day:** 1 (Starting Week 2: JavaScript, Node, and SQL)  
**Current phase:** Phase 1: How applications work (Weeks 1-2)  

---

# Overall Progress

* [x] Week 0 — Setup and job calibration
* [x] Week 1 — Programming and web basics
* [ ] Week 2 — JavaScript, Node, and SQL
* [ ] Week 3 — SQL injection, XSS, authentication
* [ ] Week 4 — Sessions and access control
* [ ] Week 5 — Server-side vulnerabilities
* [ ] Week 6 — API security
* [ ] Week 7 — Navigating a codebase
* [ ] Week 8 — Security-focused code review
* [ ] Week 9 — SAST
* [ ] Week 10 — Threat modeling
* [ ] Week 11 — GitHub Actions and security scanning
* [ ] Week 12 — DAST in the pipeline
* [ ] Week 13 — Capstone recon and threat model
* [ ] Week 14 — Capstone black-box assessment
* [ ] Week 15 — Capstone source confirmation and remediation
* [ ] Week 16 — Capstone regression pipeline and final report

---

# Demonstrated Skills

## Programming

### Python
* [x] Variables and basic data types
* [x] Lists and dictionaries
* [x] Conditions
* [x] Loops
* [x] Functions
* [x] Imports/modules
* [x] Exceptions
* [x] Files
* [x] JSON
* [x] HTTP requests
* [x] Can read a small Flask application
* [x] Can trace request data through Python code

### JavaScript / Node
* [ ] Basic JavaScript syntax
* [ ] Variables and functions
* [ ] Objects
* [ ] Basic asynchronous code
* [ ] Express routes
* [ ] Request/response handling
* [ ] Can trace request data through Node/Express code

### SQL
* [x] SELECT
* [x] INSERT
* [ ] UPDATE
* [ ] DELETE
* [x] WHERE
* [ ] JOIN
* [x] Understand application-to-database flow
* [x] Recognize unsafe query construction
* [x] Understand parameterized queries

### Command line (pick up as needed; NOT a gate for any week)
* [x] Comfortable running commands for the tools in the plan (Docker, Git, Semgrep, etc.)
* [x] Basic file and directory operations
* [x] Environment variables

---

# Web / Application Security

* [x] Understand HTTP requests and responses
* [x] Understand cookies
* [x] Understand sessions
* [x] Understand authentication
* [x] Understand authorization
* [x] Understand client vs server trust
* [x] Understand security boundaries
* [ ] SQL injection
* [ ] Reflected XSS
* [ ] Stored XSS
* [ ] DOM XSS
* [ ] CSRF
* [ ] IDOR / BOLA
* [ ] Horizontal privilege escalation
* [ ] Vertical privilege escalation
* [ ] Forced browsing
* [ ] SSRF
* [ ] Path traversal
* [ ] File upload vulnerabilities
* [ ] Security misconfiguration
* [ ] JWT security
* [ ] API authorization
* [ ] Rate limiting
* [ ] Mass assignment
* [ ] Business-logic vulnerabilities

---

# Security Reasoning

* [x] Can identify attacker-controlled input
* [x] Can identify trust boundaries
* [x] Can trace data flow
* [x] Understand SOURCE → TRANSFORMATION → SINK
* [x] Can identify security-sensitive operations
* [x] Can identify missing authorization checks
* [x] Can distinguish authentication from authorization
* [ ] Can form attack hypotheses
* [ ] Can reason about exploitability
* [x] Can assess security impact
* [x] Can identify root cause
* [x] Can explain remediation
* [ ] Can apply a known vulnerability concept to an unfamiliar application

---

# Application Testing

* [ ] Can map a basic web application's attack surface
* [x] Can identify application endpoints
* [x] Can use Burp Proxy
* [x] Can modify requests
* [x] Can manipulate parameters
* [x] Can inspect responses
* [ ] Can test authentication
* [ ] Can test authorization
* [x] Can test APIs manually
* [ ] Can use PortSwigger labs independently
* [x] Can use Juice Shop independently
* [ ] Can use crAPI independently
* [ ] Can document evidence professionally

---

# Code Review

* [ ] Can navigate an unfamiliar codebase
* [x] Can locate an endpoint from an HTTP request
* [x] Can trace request → handler → function
* [x] Can trace function → database/file/API
* [x] Can identify attacker-controlled sources
* [x] Can identify dangerous sinks
* [x] Can identify missing security controls
* [x] Can identify authorization flaws in source
* [x] Can identify unsafe input handling
* [ ] Can identify exposed secrets
* [ ] Can identify server-side request paths
* [x] Can explain source-level root cause
* [x] Can implement or describe an appropriate fix
* [ ] Can retest a security fix

---

# SAST
(Unlocks Week 9)

---

# Threat Modeling
(Unlocks Week 10)

---

# DevSecOps / Security Pipeline
(Unlocks Week 11)

---

# Professional Reporting
(Unlocks Week 6)

---

# Portfolio Artifacts
(Unlocks Weeks 6, 9, 11, 16)

---

# Current Weak Areas
* Unhandled thread-safety in SQLite database connection objects inside multithreaded web servers (addressed in Day 6).
* Initial tendency to conflate route-level regex matching rejections with view function internal validation.

---

# Current Strengths
* Strong mechanical understanding of two-channel prepared statements vs. single-channel concatenation.
* Accurate mental model of Python truthiness and its exploitation vectors.
* Protocol-level fluency with raw HTTP streams, CRLF delimiters, and custom header injection.

---

# Checkpoints

## Week 0 Checkpoint
**Status:** Complete (2026-10-09)  
**Evidence:** Toolchain operational (Python 3.14, Node 24, Git, Docker); Juice Shop verified on localhost:3000; central hub repository appsec-learning synced to GitHub; job-market-notes.md calibrated against 15 active enterprise AppSec postings.

---

## Week 2 Checkpoint
**Status:** In Progress (Starting Week 2)  
**Can I trace a request from browser → HTTP → code → database → response, in both Python and Node?**
* [ ] Python: Demonstrated in Week 1, Day 6.
* [ ] Node.js: Scheduled for Week 2.

---

# Session Log

### Session 1.6 (November 17, 2026) — Week 1 Synthesis & End-to-End Tracing
```text
Date / Topic: 2026-11-17 / Week 1 Day 6 — End-to-End Request Tracing & Skills Audit
What I demonstrated: Traced full 7-stage HTTP request lifecycle in labs/day06_end_to_end_trace.py; contrasted data-level filtering against access-control checks; parsed raw TCP headers into Python authentication contexts; diagnosed SQLite threading concurrency crashes in Flask; conducted formal demonstrated skills audit for Week 0 and Week 1.
What I got wrong: Diagnosed unexpected HTTP 500 responses as unhandled SQLite thread safety exceptions across worker threads.
Next session: Week 2 Day 1 — JavaScript runtime mechanics, syntax lego bricks, and async execution for AppSec.

### Session 2.1 (November 20, 2026) — JavaScript Runtime Mechanics & Type Juggling
```text
Date / Topic: 2026-11-20 / Week 2 Day 1 — JavaScript Syntax Grammar & Event Loop Mechanics
What I demonstrated: Executed JavaScript runtime experiments in labs/day07_js_mechanics.js; analyzed type coercion exploits using loose equality (==) vs strict equality (===); identified cross-language truthiness differences (JS empty array [] evaluating to true vs Python evaluating to false); contrasted Node.js single-threaded event loop DoS risks against Python multi-threaded worker models.
What I got wrong: Initially assumed if (items) syntax was invalid rather than recognizing that in JavaScript, evaluating an empty array variable inside an if statement always evaluates to true.
Next session: Week 2 Day 2 — Building a basic Express.js web server: routing, middleware, and request/response lifecycles.
