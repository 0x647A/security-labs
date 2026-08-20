# HTTP Host Header Attacks

Write-ups and step-by-step solutions for the **HTTP Host header** labs from the
[PortSwigger Web Security Academy](https://portswigger.net/web-security/host-header).

The HTTP `Host` header is a mandatory request header that specifies the domain the
client wants to reach. Many applications trust this client-controlled value implicitly
and reuse it to build absolute URLs, make routing decisions, or gate access. Because an
attacker fully controls the `Host` header, this trust leads to a range of
vulnerabilities: password reset poisoning, authentication and access-control bypasses,
web cache poisoning, SSRF, and routing-based attacks.

---

## Labs

| # | Lab | Difficulty | Write-up |
|---|-----|------------|----------|
| 1 | Basic password reset poisoning | Apprentice | [View](./Basic%20password%20reset%20poisoning/README.md) |
| 2 | Host header authentication bypass | Apprentice | [View](./Host%20header%20authentication%20bypass/README.md) |

---

## Key Takeaways

- **The `Host` header is attacker-controlled.** Never trust it for security decisions.
- **Do not build security-sensitive URLs from the `Host` header** (for example, password
  reset links). Use a hardcoded or configuration-driven base URL instead.
- **Do not use the `Host` header for access control.** Network origin must be derived
  from the connection (the client's IP address from the socket), never from a header.
- **Validate the `Host` header against an allowlist** of expected domains and reject
  anything unexpected, ideally at the reverse proxy before the request reaches the
  application.

---

## References

- [PortSwigger: HTTP Host header attacks](https://portswigger.net/web-security/host-header)
- [PortSwigger: Password reset poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning)
- [OWASP: Host header injection](https://owasp.org/www-project-web-security-testing-guide/)
