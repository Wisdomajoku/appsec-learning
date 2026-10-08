# AppSec 16-Week Plan

**Status:** LOCKED. Changes only at checkpoints (end of Week 6, 12, 16), and only if (a) I'm more than 1 week behind, or (b) my job-market notes show a hard requirement the plan misses.

**Start date:** October 8, 2026  **Planned end date (Week 16):** January 28, 2027

---

## Ground rules

- **Pace:** 4 hrs/day, 6 days/week, 1 rest day. Treat 70-80% as effective time (about 270-300 real hours total).
- **Learning loop (every topic):** concept -> tiny code example -> lab -> find it in source code -> fix it -> automate the check.
- **Never** read or watch something without a lab or code exercise right after.
- **One** main resource per topic.
- **Stuck?** Time-box 30-45 minutes, then ask or read a write-up.
- **A week is not done** until the notes entry exists.
- **Notes are in my own words.** Each entry covers: what the vulnerability is, how it works, how I exploited it, which control was missing, how to fix it.
- **Parking lot:** any "should I also learn X?" idea goes in `parking-lot.md`. Read it only at checkpoints.
- **No plan changes** from outside opinions mid-phase. Measure deliverables, not plan quality.
- **Weekend thread:** 20-30 minutes on MCP/AI security so it stays alive.
- **If behind:** cut something from the "Deferred" list below. Do not extend the plan.

### Daily time split

| Weeks | Code practice | Main work | Notes |
|---|---|---|---|
| 1-2 | 90 min | 2 hr | 30 min |
| 3-6 | 75 min | 2 hr 15 min | 30 min |
| 7-9 | 45-60 min | 2 hr 30 min | 30 min |
| 10-12 | 45 min | 2 hr 45 min | 30 min |
| 13-16 | as needed | 3+ hr | 30 min |

### Key terms

- **SAST:** analyzing source code without running it (Semgrep, CodeQL).
- **DAST:** testing the running application over HTTP (Burp, ZAP).
- **SCA:** checking third-party libraries for known vulnerabilities (OSV-Scanner, Trivy).
- **CI/CD:** automated pipeline that runs on every code change.
- **DevSecOps:** security checks inside that pipeline.
- **Workflow to repeat on any language:** find it (DAST) -> locate it in code (SAST) -> fix it -> add an automatic check (CI/CD).

### Resource backbone

- PortSwigger Web Security Academy (labs)
- OWASP Juice Shop, OWASP crAPI, PyGoat or VAmPI (practice apps)
- OWASP Top 10, OWASP API Security Top 10, OWASP ASVS (reference checklists)
- OWASP Cheat Sheet Series
- Semgrep, CodeQL, OSV-Scanner/Trivy, Gitleaks, OWASP ZAP
- MDN HTTP guides, *Automate the Boring Stuff with Python*, javascript.info, SQLBolt, *Pro Git*
- OWASP Threat Modeling Cheat Sheet, OWASP Threat Dragon

---

## Week 0: Setup and job calibration (3-5 days)

- [ ] Install Python (with virtual environments), Node.js/npm, Git, Docker, Burp Suite, VS Code
- [ ] Run Juice Shop and crAPI with Docker
- [ ] Read 15-20 current AppSec / security engineering job postings; record languages, frameworks, tools, years of experience
- [ ] Create GitHub repo `appsec-learning/` with `README.md`, `job-market-notes.md`, `parking-lot.md`, and this plan

**Deliverable:** the repo above.

---

## Phase 1: How applications work (Weeks 1-2)

### Week 1: Programming and web basics
- [ ] Python from zero: variables, strings, lists, dictionaries, conditions, loops, functions, imports, exceptions, files, JSON
- [ ] HTTP: request, response, method, URL, headers, body, status code, cookies, parameters
- [ ] Send HTTP requests from Python; watch them in Burp
- [ ] Flask basics: understand `GET /users/10` -> route match -> `id = "10"` -> function runs
- [ ] Notes entry for each study day

### Week 2: JavaScript, Node, and SQL
- [ ] JavaScript enough to read: request value -> variable -> function -> database -> response
- [ ] Basic Express server
- [ ] SQL: SELECT, INSERT, UPDATE, DELETE, WHERE, JOIN
- [ ] Connect Python and Node to a small database
- [ ] Key question answered in my own words: how does untrusted input become part of a database operation?

**Checkpoint:** I can follow one request from browser to code to database and back, in both languages.

---

## Phase 2: Break things (Weeks 3-6, mostly DAST)

### Week 3: First major vulnerabilities
- [ ] SQL injection: write a tiny vulnerable example, exploit it, fix it with parameterized queries
- [ ] PortSwigger SQLi labs
- [ ] XSS: stored, reflected, DOM
- [ ] Source -> transformation -> sink thinking
- [ ] Authentication (who are you?) vs authorization (what are you allowed to do?)

### Week 4: Sessions and access control
- [ ] Cookies, sessions, session management
- [ ] Horizontal and vertical privilege escalation, IDOR/BOLA, forced browsing
- [ ] Mental model: Alice requests invoice 100; server must check "does Alice own invoice 100?"
- [ ] PortSwigger access control and authentication labs; Juice Shop

### Week 5: Server-side vulnerabilities
- [ ] SSRF (core attack, impact, defenses, common bypass logic; then stop)
- [ ] File upload flaws
- [ ] Path traversal
- [ ] Security misconfiguration: debug mode, default credentials, exposed admin pages

### Week 6: API security
- [ ] REST, JSON, API authentication, JWT, rate limiting, mass assignment
- [ ] Object-level and function-level authorization
- [ ] OWASP API Security Top 10 (2023) using crAPI

**Deliverable:** three professional findings. Each includes: title, severity, affected component, prerequisites, steps to reproduce, evidence, impact, root cause, remediation, retest.

**Checkpoint 1 (end of Week 6):** I can solve most beginner and intermediate Academy labs without hints. Read `parking-lot.md`. Adjust the plan only per the rules at the top.

---

## Phase 3: Code review (Weeks 7-9, SAST)

The question changes from "can I break it?" to "why does the code allow it?"

### Week 7: Navigating a codebase
- [ ] Start from a known vulnerability and trace backwards: request -> endpoint -> handler -> function -> database/file/API
- [ ] Do not read whole repositories
- [ ] Use Juice Shop (note: it is TypeScript, which is JavaScript plus type annotations)

### Week 8: Security-focused review
- [ ] Spot: untrusted input reaching a dangerous operation
- [ ] Spot: user identity reaching a resource with no authorization check
- [ ] Spot: secrets in source code
- [ ] Spot: user-controlled URLs reaching server-side requests
- [ ] Repeat on a vulnerable Python app (PyGoat or VAmPI): who is authenticated, what is validated, what is missing

### Week 9: SAST tools
- [ ] Semgrep first, then CodeQL (conceptually: analyzes code with queries)
- [ ] Triage: scanner finding -> read the code -> real or false alarm -> exploitability -> severity -> fix

**Deliverables:**
- three custom Semgrep rules, each explained
- a code-review report with fixes submitted as real pull requests

**Checkpoint:** for any bug from Phase 2, I can point to the exact lines of code and write the fix.

---

## Phase 4: Threat modeling and pipeline (Weeks 10-12)

### Week 10: Threat modeling
- [ ] Terms: asset, actor, entry point, trust boundary, data flow, attack surface, threat, control
- [ ] STRIDE: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege
- [ ] Draw a data flow diagram for one of my AI applications; mark trust boundaries

### Week 11: GitHub Actions and scanning
- [ ] Terms: repository, branch, commit, pull request, workflow, job, step, runner
- [ ] Pipeline running Semgrep, a dependency scan (OSV-Scanner or Trivy), and Gitleaks
- [ ] Each pull request passes or fails

### Week 12: DAST in the pipeline
- [ ] OWASP ZAP basics
- [ ] Extend pipeline: SAST -> dependency scan -> secrets -> build -> start test app -> ZAP scan -> result
- [ ] Keep the test app tiny (this is the hardest week technically)

**Deliverable:** a pipeline repo that fails when it catches a vulnerability.

**Checkpoint 2 (end of Week 12):** I can explain what each scanner does, what it cannot catch, and why all three are needed. Read `parking-lot.md`.

---

## Phase 5: Production Security Assessment (Weeks 13-16)

**The app:** small and scoped, for example Flask with 3-4 endpoints (`/login`, `/accounts/:id`, `/transfer`, `/chat`), a database, and one simple LLM call. An AI assistant may be used to scaffold it; say so in the write-up, since the skill being demonstrated is the assessment.

### Week 13: Recon and threat model
- [ ] Map endpoints, roles, assets, trust boundaries
- [ ] Write attack hypotheses (e.g., AT-01: can user A access user B's account? AT-02: can a low-privileged user call an admin function? AT-03: can input manipulate an outbound request? AT-04: can prompt input influence a privileged action?)
- [ ] **Start applying to jobs this week**

### Week 14: Black-box assessment
- [ ] Test authentication, authorization, input handling, business logic, API security, SSRF, configuration, AI attack surface
- [ ] Use browser, Burp, manual testing. No source code yet.

### Week 15: Source confirmation and fixes
- [ ] For each finding: observation -> reproduce -> locate code -> root cause -> fix -> retest
- [ ] This is the most important week of the plan

### Week 16: Regression pipeline and report
- [ ] Wire in Semgrep, dependency scan, Gitleaks, ZAP
- [ ] Deliberately reintroduce one vulnerability: CI fails -> fix -> CI passes
- [ ] Publish the full report

**Checkpoint 3 (end of Week 16):** portfolio published, applications underway. Read `parking-lot.md` and decide next steps.

---

## Portfolio at the end (four artifacts, not twenty)

1. Three vulnerability write-ups with evidence, root cause, and remediation
2. A code-review project: source location, data flow, why vulnerable, patch
3. A security pipeline repo (Semgrep, dependency scan, Gitleaks, ZAP on GitHub Actions)
4. The full application assessment: threat model, black-box assessment, source review, remediation, regression gate, final report

---

## Deferred until after the plan

Deserialization, request smuggling, GraphQL deep dives, cloud security (AWS/Azure/GCP), Kubernetes, Terraform, additional programming languages, mobile security, advanced cryptography.

---

## Progress log

Add one line per week: date, what was completed, deliverable status, anything blocking.

| Week | Dates | Completed | Deliverable done? | Blockers |
|---|---|---|---|---|
| 0 | Oct 08 - Oct 14 | | | |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |
| 14 | | | | |
| 15 | | | | |
| 16 | | | | |
