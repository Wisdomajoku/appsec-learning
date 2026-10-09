# AppSec Job Market Calibration (15 Representative Postings)

## Market Signals Summary
* **Primary Languages:** Python and TypeScript/JavaScript dominate general AppSec, with Go and Java prevalent in backend systems.
* **Dominant Frameworks:** REST APIs (FastAPI, Express, Flask), React/Next.js frontends, microservice architectures.
* **Required Security Tooling:**
  * **SAST:** Semgrep (industry consensus for customizable rules) and CodeQL.
  * **DAST:** Burp Suite (universal offensive standard), ZAP.
  * **SCA / Secrets:** Snyk, Trivy, Gitleaks, OSV-Scanner.
* **Baseline Experience Levels:** 2 to 5 years software/security engineering (heavily favors developers who understand security over pure compliance analysts).
* **Emerging Architectural Themes:** Threat modeling, CI/CD pipeline automation (GitHub Actions), API authorization (BOLA/IDOR), and AI/LLM application security.

## Calibration Matrix

| # | Company | Role Title | Core Languages | Core Frameworks / Stack | Tooling Mentioned | Exp Level | Key Requirements |
|---|---|---|---|---|---|---|---|
| 01 | Stripe | Product Security Engineer | Ruby, Java, Go, Python | Distributed systems, REST APIs | Semgrep, CodeQL, Burp Suite | 3+ yrs | Threat modeling, secure code review, API auth (OAuth/JWT) |
| 02 | Datadog | AppSec Engineer | Go, Python, TypeScript | Microservices, Docker, K8s | Semgrep, Snyk, GitHub Actions | 2-4 yrs | CI/CD security automation, SAST triage, developer enablement |
| 03 | Brex | Application Security Engineer | Elixir, TypeScript, Python | React, GraphQL, REST | Burp Suite, Semgrep, Trivy | 3+ yrs | FinTech security, IDOR/BOLA testing, business logic reviews |
| 04 | Cloudflare | Security Engineer - AppSec | Go, Rust, Python, C/C++ | Edge APIs, WebSockets | ZAP, Burp Suite, CodeQL | 3-5 yrs | HTTP protocol depth, SSRF/RCE defenses, WAF rule authoring |
| 05 | Figma | Product Security Engineer | TypeScript, Python, Ruby | React, WebGL, Node.js | Semgrep, Gitleaks, Burp Suite | 2-5 yrs | Code review, access control modeling, tenant isolation |
| 06 | Coinbase | Security Software Engineer | Go, Python, Solidity | AWS, Microservices, REST | CodeQL, Slither, Burp Suite | 3+ yrs | Cryptographic controls, auth flows, secure SDLC pipeline |
| 07 | OpenAI | Product Security Engineer | Python, TypeScript, Go | FastAPI, Node.js, Kubernetes | Semgrep, Burp Suite, Trivy | 3+ yrs | Threat modeling AI systems, prompt injection defenses, API authorization |
| 08 | Okta | Senior AppSec Engineer | Java, Python, Go | Spring Boot, React, Node | Checkmarx, Burp Suite, Snyk | 4+ yrs | Identity protocols (SAML, OIDC, OAuth), authentication bypass analysis |
| 09 | Reddit | Application Security Engineer | Python, Go, TypeScript | GraphQL, REST, Kafka | Semgrep, Burp Suite, GitHub Actions | 2-4 yrs | Bug bounty triage, SAST rule customization, vulnerability reporting |
| 10 | MongoDB | Software Engineer - Security | Go, Python, C++ | Distributed DB, Docker | CodeQL, Semgrep, OSV-Scanner | 2-4 yrs | Supply chain security, dependency scanning (SCA), safe query interfaces |
| 11 | Palantir | Application Security Engineer | Java, TypeScript, Python | Microservices, React | Burp Suite, CodeQL, ZAP | 1-3 yrs | Threat modeling, secure API design, access control (RBAC/ABAC) |
| 12 | Netflix | Security Software Engineer | Java, Python, Node.js | Spring Boot, AWS, GraphQL | Semgrep, Burp Suite, Custom tools | 3+ yrs | Automated security tooling in CI, self-service developer security |
| 13 | DoorDash | Product Security Engineer | Kotlin, Python, Go | Microservices, gRPC, REST | Burp Suite, Snyk, Semgrep | 3+ yrs | API security (BOLA/BFLA), SSRF mitigation, security design reviews |
| 14 | Anthropic | Security Engineer - AppSec | Python, TypeScript | Next.js, Cloud APIs | Semgrep, Burp Suite, GitHub Actions | 2-5 yrs | Red teaming internal web applications, securing LLM evaluation harnesses |
| 15 | GitLab | Application Security Engineer | Ruby, Go, JavaScript | Ruby on Rails, Vue.js | Semgrep, Brakeman, ZAP, Gitleaks | 2-4 yrs | Asynchronous secure code reviews, reproducing HackerOne reports |

## Calibration Assessment & Plan Validation
1. **Language Alignment:** Our plan centers on **Python** and **JavaScript/TypeScript**, with SQL for database interactions. This covers ~80% of market expectations. (Go and Java are logged to `parking-lot.md` for post-curriculum expansion).
2. **Tooling Alignment:** Our core toolchain (**Burp Suite, Semgrep, CodeQL, Trivy, Gitleaks, ZAP, GitHub Actions**) is an exact match for the industry standard toolset.
3. **Core Capability Alignment:** Employers test:
   * Can you find the bug dynamically? (DAST — Weeks 3–6)
   * Can you pinpoint the exact source code vulnerability and fix it? (SAST & Code Review — Weeks 7–9)
   * Can you automate checks so it never happens again? (DevSecOps — Weeks 10–12)
   * Can you assess an unfamiliar full-stack application and write a professional report? (Assessment — Weeks 13–16)
4. **Conclusion:** The 16-week locked curriculum requires **zero modifications**.
