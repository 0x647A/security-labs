# PortSwigger Web Security Academy – Apprentice Level

Solutions and notes from **59 Apprentice-level labs** on the PortSwigger Web Security Academy platform.

The Apprentice level builds foundational knowledge of how web vulnerabilities work in practice - exploitation mechanics, underlying root causes, and how to prevent them.

---

## Lab Coverage

| Category | Labs |
|---|---|
| Access Control Vulnerabilities | 9 |
| Cross-Site Scripting (XSS) | 9 |
| Business Logic Vulnerabilities | 4 |
| Information Disclosure | 4 |
| Clickjacking | 3 |
| Authentication | 3 |
| SQL Injection | 2 |
| NoSQL Injection | 2 |
| Cross-Origin Resource Sharing (CORS) | 2 |
| File Upload Vulnerabilities | 2 |
| JWT Attacks | 2 |
| HTTP Host Header Attacks | 2 |
| Server-Side Request Forgery (SSRF) | 2 |
| XML External Entity (XXE) Injection | 2 |
| Cross-Site Request Forgery (CSRF) | 1 |
| Path Traversal | 1 |
| OS Command Injection | 1 |
| GraphQL API Vulnerabilities | 1 |
| Insecure Deserialization | 1 |
| OAuth Authentication | 1 |
| Race Conditions | 1 |
| WebSockets | 1 |
| Web Cache Deception | 1 |
| Web LLM Attacks | 1 |
| API Testing | 1 |

---

## Writeup Format

Each lab follows a consistent structure:

- **Vulnerability Overview** — root cause, why it's dangerous, what the query/token/request looks like before and after injection
- **Steps to Solve** — numbered walkthrough with screenshots at each step
- **Why This Works** — technical explanation of the exploitation mechanics
- **Remediation** — concrete defensive guidance (parameterized queries, validation, secure headers, etc.)

---

## Tools

- **Burp Suite** — proxy, repeater, intercept
- **Burp JWT Editor** — JWT algorithm confusion and signing attacks
- **Browser DevTools** — Application tab for cookie/JWT inspection
- **jwt.io** — JWT decoding and tampering

---

## Acknowledgements

For scripts and additional explanations, I referenced:
- [cyberw1ng on Medium](https://cyberw1ng.medium.com/)
- [Michael10Sommer on YouTube](https://www.youtube.com/@Michael10Sommer)

---

## Disclaimer

All materials are created **for educational purposes only**. Labs are solved exclusively in legal, intentionally vulnerable environments provided by PortSwigger. Techniques shown here must **not** be used against systems without explicit permission.
