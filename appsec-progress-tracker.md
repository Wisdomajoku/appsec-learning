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

**Week:** 1  
**Day:** 1  
**Current phase:** Phase 1: How applications work (Weeks 1-2)  

---

# Overall Progress

* [x] Week 0 — Setup and job calibration
* [ ] Week 1 — Programming and web basics
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
* [ ] Week 13 — Application security assessment: recon and threat model
* [ ] Week 14 — Application security assessment: black-box assessment
* [ ] Week 15 — Application security assessment: source confirmation and remediation
* [ ] Week 16 — Application security assessment: regression pipeline and final report

---

# Demonstrated Skills

## Programming

### Python
* [ ] Variables and basic data types
* [ ] Lists and dictionaries
* [ ] Conditions
* [ ] Loops
* [ ] Functions
* [ ] Imports/modules
* [ ] Exceptions
* [ ] Files
* [ ] JSON
* [ ] HTTP requests
* [ ] Can read a small Flask application
* [ ] Can trace request data through Python code

### JavaScript / Node
* [ ] Basic JavaScript syntax
* [ ] Variables and functions
* [ ] Objects
* [ ] Basic asynchronous code
* [ ] Express routes
* [ ] Request/response handling
* [ ] Can trace request data through Node/Express code

### SQL
* [ ] SELECT
* [ ] INSERT
* [ ] UPDATE
* [ ] DELETE
* [ ] WHERE
* [ ] JOIN
* [ ] Understand application-to-database flow
* [ ] Recognize unsafe query construction
* [ ] Understand parameterized queries

### Command line (pick up as needed; NOT a gate for any week)
* [ ] Comfortable running commands for the tools in the plan (Docker, Git, Semgrep, etc.)
* [ ] Basic file and directory operations
* [ ] Environment variables

---

# Web / Application Security

* [ ] Understand HTTP requests and responses
* [ ] Understand cookies
* [ ] Understand sessions
* [ ] Understand authentication
* [ ] Understand authorization
* [ ] Understand client vs server trust
* [ ] Understand security boundaries
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

* [ ] Can identify attacker-controlled input
* [ ] Can identify trust boundaries
* [ ] Can trace data flow
* [ ] Understand SOURCE → TRANSFORMATION → SINK
* [ ] Can identify security-sensitive operations
* [ ] Can identify missing authorization checks
* [ ] Can distinguish authentication from authorization
* [ ] Can form attack hypotheses
* [ ] Can reason about exploitability
* [ ] Can assess security impact
* [ ] Can identify root cause
* [ ] Can explain remediation
* [ ] Can apply a known vulnerability concept to an unfamiliar application

---

# Application Testing

* [ ] Can map a basic web application's attack surface
* [ ] Can identify application endpoints
* [ ] Can use Burp Proxy
* [ ] Can modify requests
* [ ] Can manipulate parameters
* [ ] Can inspect responses
* [ ] Can test authentication
* [ ] Can test authorization
* [ ] Can test APIs manually
* [ ] Can use PortSwigger labs independently
* [ ] Can use Juice Shop independently
* [ ] Can use crAPI independently
* [ ] Can document evidence professionally

---

# Code Review

* [ ] Can navigate an unfamiliar codebase
* [ ] Can locate an endpoint from an HTTP request
* [ ] Can trace request → handler → function
* [ ] Can trace function → database/file/API
* [ ] Can identify attacker-controlled sources
* [ ] Can identify dangerous sinks
* [ ] Can identify missing security controls
* [ ] Can identify authorization flaws in source
* [ ] Can identify unsafe input handling
* [ ] Can identify exposed secrets
* [ ] Can identify server-side request paths
* [ ] Can explain source-level root cause
* [ ] Can implement or describe an appropriate fix
* [ ] Can retest a security fix

---

# SAST

## Semgrep
* [ ] Understand what SAST means
* [ ] Understand basic Semgrep rules
* [ ] Run Semgrep against source code
* [ ] Interpret findings
* [ ] Identify false positives
* [ ] Validate real findings
* [ ] Write custom Semgrep rule #1
* [ ] Write custom Semgrep rule #2
* [ ] Write custom Semgrep rule #3

## CodeQL
* [ ] Understand the basic CodeQL model
* [ ] Understand code representation/database concept
* [ ] Understand security queries conceptually
* [ ] Interpret a CodeQL finding
* [ ] Understand how CodeQL differs from basic pattern matching

---

# Threat Modeling

* [ ] Asset
* [ ] Actor
* [ ] Entry point
* [ ] Trust boundary
* [ ] Data flow
* [ ] Attack surface
* [ ] Threat
* [ ] Security control
* [ ] STRIDE
* [ ] Can create a basic data-flow diagram
* [ ] Can identify trust boundaries
* [ ] Can generate attack hypotheses
* [ ] Can threat-model an AI-enabled application

---

# DevSecOps / Security Pipeline

* [ ] Git repository
* [ ] Branch
* [ ] Commit
* [ ] Pull request
* [ ] GitHub Actions workflow
* [ ] Job
* [ ] Step
* [ ] Runner
* [ ] Understand SAST in CI
* [ ] Understand dependency scanning
* [ ] Understand secrets scanning
* [ ] Understand DAST in CI
* [ ] Configure Semgrep
* [ ] Configure OSV-Scanner or Trivy
* [ ] Configure Gitleaks
* [ ] Configure ZAP
* [ ] Build a working security pipeline
* [ ] Make CI fail on a deliberately introduced vulnerability
* [ ] Fix the vulnerability
* [ ] Demonstrate CI passing after remediation

---

# Professional Reporting

* [ ] Write a clear vulnerability title
* [ ] Assign severity appropriately
* [ ] State affected component
* [ ] State prerequisites
* [ ] Write reproducible attack steps
* [ ] Capture evidence
* [ ] Explain impact
* [ ] Explain root cause
* [ ] Recommend remediation
* [ ] Document retesting
* [ ] Write a complete security finding independently

---

# Portfolio Artifacts

## Vulnerability Write-Ups
* [ ] Finding 1
* [ ] Finding 2
* [ ] Finding 3

## Code Review
* [ ] Code-review project
* [ ] Source-level findings
* [ ] Data-flow explanation
* [ ] Security fixes
* [ ] Real Git commits/PRs

## Security Pipeline
* [ ] Semgrep
* [ ] Dependency scanning
* [ ] Gitleaks
* [ ] ZAP
* [ ] GitHub Actions
* [ ] Demonstrated security regression gate

## Application Security Assessment
* [ ] Architecture
* [ ] Threat model
* [ ] Attack surface
* [ ] Attack hypotheses
* [ ] Black-box assessment
* [ ] Findings
* [ ] Source-code confirmation
* [ ] Root-cause analysis
* [ ] Remediation
* [ ] Retesting
* [ ] CI regression gate
* [ ] Final report
* [ ] Published portfolio artifact

---

# Current Weak Areas
*Update weekly from actual exercises and feedback on my work, not from how I feel about it.*

---

# Current Strengths
*Update only from demonstrated ability.*

---

# Checkpoints

## Week 0 Checkpoint
**Status:** Complete (2026-10-09)
**Evidence:** Local toolchain verified (Python 3.14 venv, Node 24, Git, Docker); Juice Shop running on localhost:3000; central repository appsec-learning initialized and synced with GitHub; job-market-notes.md calibrated against 15 active enterprise AppSec postings.
**Remaining:** None. Week 0 closed.

---

## Week 2 Checkpoint
**Status:** Not started  
**Can I trace a request from browser → HTTP → code → database → response, in both Python and Node?**
* [ ]  
**Evidence:**

---

## Week 6 Checkpoint (plan changes allowed here, per plan rules)
**Status:** Not started  
**Can I solve beginner/intermediate web and API labs with limited assistance?**
* [ ]  
**Can I explain the attack, security failure, impact and remediation?**
* [ ]  
**Evidence:**

---

## Week 9 Checkpoint
**Status:** Not started  
**Can I locate the source-level root cause of a vulnerability?**
* [ ]  
**Can I explain the relevant data flow?**
* [ ]  
**Can I write and validate a custom Semgrep rule?**
* [ ]  
**Evidence:**

---

## Week 12 Checkpoint (plan changes allowed here, per plan rules)
**Status:** Not started  
**Can I explain SAST vs SCA vs secrets scanning vs DAST?**
* [ ]  
**Can I build and troubleshoot a basic AppSec CI pipeline?**
* [ ]  
**Evidence:**

---

## Week 16 Final Checkpoint
**Status:** Not started  
**Can I independently assess an unfamiliar web/API application?**
* [ ]  
**Can I identify meaningful vulnerabilities?**
* [ ]  
**Can I trace them into source code?**
* [ ]  
**Can I explain and implement remediation?**
* [ ]  
**Can I retest the fix?**
* [ ]  
**Can I integrate appropriate regression checks into CI/CD?**
* [ ]  
**Can I produce a professional security assessment?**
* [ ]  
**Evidence:**

---

# Deferred Topics
Outside the 16-week core. Revisit only at checkpoints, via `parking-lot.md`:
* Deep deserialization
* Request smuggling
* Deep GraphQL security
* Cloud security
* Kubernetes
* Terraform
* Additional programming languages
* Mobile AppSec
* Advanced cryptography
* Deep Bash/Linux scripting

---

# AI / MCP Maintenance
Target: 20–30 minutes on one weekend day.
* [ ] MCP security practice maintained
* [ ] AI security notes maintained
* [ ] Existing AI-security work remains active

**Notes:**

---

# Application Progress
**Application start target:** Week 13  
**Applications submitted:**  
*  
**Interviews:**  
*  
**Technical assessments:**  
*  
**Feedback / recurring skill gaps:**  
*  

---

# Session Log

Four fields per session. Detailed learning goes in the daily notes entry, not here.

```text
Date / Topic:
What I demonstrated:
What I got wrong:
Next session:
Log entries
Session 0.1 (October 8, 2026) — Environment Baseline & Toolchain
code
Text
Date / Topic: 2026-10-08 / Week 0 Setup & Toolchain Baseline
What I demonstrated: Host environment diagnostic; verified Python 3.14.6 + venv, Node v24.19, npm 11.19, Git 2.53; resolved Kali dpkg package interruption and installed Docker Engine + Docker Compose; verified Docker container execution via hello-world.
What I got wrong: Subshell suspension when running newgrp with stacked commands; attempting to install debian docker-compose-plugin rather than Kali native docker-compose package.
Next session: Deploy Juice Shop/crAPI targets, verify Burp Suite proxy interception, initialize GitHub remote repo, and begin job market calibration.

### Session 1.1 (October 12, 2026) — Python Defensive Data Structures
```text
Date / Topic: 2026-10-12 / Week 1 Day 1 — Python Input Validation & Truthiness Mechanics
What I demonstrated: Built and executed defensive request parser (labs/day01_input_parser.py); analyzed how Python evaluates truthiness on non-empty strings causing privilege escalation; identified CWE-209 (Info Disclosure) and CWE-400 (DoS) risks stemming from unhandled KeyError and JSONDecodeError crashes; documented layered validation architecture.
What I got wrong: Initially missed distinguishing string literal "false" from boolean False in conditional truthiness evaluation before walking through Python memory model.
Next session: Week 1 Day 2 — HTTP Protocol internals: request/response anatomy, headers, cookies, and network-level trust boundaries.

### Session 1.2 (October 22, 2026) — HTTP Protocol Mechanics & Socket Probing
```text
Date / Topic: 2026-10-22 / Week 1 Day 2 — HTTP Under the Hood & Protocol Security
What I demonstrated: Built and executed raw TCP socket engine (labs/day02_raw_http.py) targeting Juice Shop; parsed HTTP/1.1 status lines, CRLF boundaries (\r\n\r\n), and Set-Cookie headers; explained virtual hosting mechanics and Host Header Injection risks; analyzed HttpOnly defense boundaries against XSS session riding; distinguished TCP Errno 111 (connection refused) from Errno 104 (connection reset).
What I got wrong: Initially encountered Errno 104 due to sending requests before Node.js finished booting inside container; verified container readiness using docker logs.
Next session: Week 1 Day 3 — Programmatic HTTP with Python `requests` & proxying through Burp Suite.
