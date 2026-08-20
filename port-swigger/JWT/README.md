# JWT Security Labs

Write-ups for the **JSON Web Token (JWT)** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/jwt). Each write-up walks through the vulnerability, the exploitation steps (with screenshots), why the attack works, and how to remediate it.

> **Disclaimer:** These materials are for educational purposes and authorized security testing only. Only test systems you own or have explicit permission to assess.

---

## What is a JWT?

A JSON Web Token is a compact, URL-safe token made of three base64url-encoded parts separated by dots:

```text
header.payload.signature
```

- **Header** - declares the token type and the signing algorithm (`alg`).
- **Payload** - the claims, such as `sub` (subject/user), `iss` (issuer), and `exp` (expiry).
- **Signature** - protects the header and payload against tampering.

JWTs are only as secure as the server's verification logic. If the server fails to check the signature, or lets the token dictate how it is verified, an attacker can forge tokens and impersonate other users.

---

## Labs

| # | Lab | Level | Vulnerability |
|---|-----|-------|---------------|
| 1 | [JWT authentication bypass via unverified signature](./JWT%20authentication%20bypass%20via%20unverified%20signature/) | Apprentice | The server does not verify the signature, so the payload can be modified freely. |
| 2 | [JWT authentication bypass via flawed signature verification](./JWT%20authentication%20bypass%20via%20flawed%20signature%20verification/) | Apprentice | The server accepts unsigned tokens (`alg: none`), allowing forged claims. |

---

## Key Takeaways

- **Always verify the signature** before trusting any claim in a token.
- **Pin the expected algorithm** server-side; never read `alg` from the token to decide how to verify it.
- **Reject the `none` algorithm** unconditionally for authenticated sessions.
- **Use short-lived tokens** with `exp`, and validate `iss` and `aud` where appropriate.

---

## References

- [PortSwigger - JWT attacks](https://portswigger.net/web-security/jwt)
- [RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
