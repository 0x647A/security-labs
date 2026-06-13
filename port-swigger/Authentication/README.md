# Authentication — PortSwigger Web Security Academy

Write-ups for the **Authentication** topic of the [PortSwigger Web Security Academy](https://portswigger.net/web-security/authentication).
Each lab includes a vulnerability overview, step-by-step solution with screenshots, an explanation of the root cause, and remediation guidance.

**Tools used:** Burp Suite (Proxy, Repeater, Intruder), browser
**OWASP Top 10:** A07:2021 – Identification and Authentication Failures

---

## Labs

| # | Lab | Level | Key vulnerability |
|---|-----|-------|-------------------|
| 1 | [Username enumeration via different responses](./Username%20enumeration%20via%20different%20responses/README.md) | Apprentice | Differential error messages leak valid usernames |
| 2 | [2FA simple bypass](./2FA%20simple%20bypass/README.md) | Apprentice | Session granted before the second factor is verified |
| 3 | [Password reset broken logic](./Password%20reset%20broken%20logic/README.md) | Apprentice | Reset token not bound to the target account |

---

## Key takeaways

- **Enforce authentication state server-side** — never trust the UI flow. A session must not be considered authenticated until *all* required factors succeed.
- **Bind security tokens to a single account and a single use** — password reset tokens should be derived back to the user, not paired with an attacker-controlled `username`.
- **Avoid information leakage** — login and recovery flows should return generic responses so they don't reveal whether an account exists.
