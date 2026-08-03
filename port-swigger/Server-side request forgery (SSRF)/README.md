# Server-Side Request Forgery (SSRF)

Write-ups for the **Server-Side Request Forgery (SSRF)** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/ssrf).

Each lab folder contains a step-by-step walkthrough, an explanation of why the attack works, remediation guidance, and annotated Burp Suite screenshots.

---

## What is SSRF?

Server-Side Request Forgery (SSRF) is a vulnerability that lets an attacker induce a server-side application to make HTTP requests to an arbitrary destination of the attacker's choosing. Because the request originates from the server, it can reach resources the attacker cannot access directly, such as:

- The application server itself, via `localhost` or `127.0.0.1`.
- Internal back-end systems that are firewalled off from the public internet.
- Cloud metadata endpoints (for example, `169.254.169.254`).

SSRF is typically exploited to bypass network-based access controls, enumerate internal infrastructure, and reach services that were assumed to be unreachable from outside the perimeter.

---

## Labs

| # | Lab | Level |
|---|-----|-------|
| 1 | [Basic SSRF against the local server](./Basic%20SSRF%20against%20the%20local%20server/) | Apprentice |
| 2 | [Basic SSRF against another back-end system](./Basic%20SSRF%20against%20another%20back-end%20system/) | Apprentice |

---

## Common Remediation

- Maintain a strict **allowlist** of permitted destination hosts and URL schemes.
- **Resolve and validate** the target hostname before making the request, rejecting private, loopback, and link-local addresses, and re-validate after resolution to defend against DNS rebinding.
- Never rely on network location (source IP) for **authorization**; internal services should authenticate every request.
- Apply **egress filtering** so application servers can only reach the hosts they legitimately need.

---

## Reference

- [PortSwigger Web Security Academy - SSRF](https://portswigger.net/web-security/ssrf)
