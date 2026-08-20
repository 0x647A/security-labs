# Cross-Site Request Forgery (CSRF)

Hands-on write-ups of CSRF labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/csrf).
Each folder documents a single lab: the underlying vulnerability, the steps taken to exploit it, screenshots of the attack, and remediation guidance.

---

## What is CSRF?

Cross-Site Request Forgery is an attack that forces an authenticated victim's browser to send an unintended, state-changing request to a web application. It works because browsers automatically attach a site's cookies to every request to that site - regardless of which page initiated the request. If the application relies on cookies alone to authenticate a request and has no additional defense, an attacker-controlled page can trigger actions on the victim's behalf.

A CSRF attack typically requires:

- **A relevant action** - something worth doing (changing an email, password, or transferring funds).
- **Cookie-based session handling** - the request is authenticated only by cookies the browser sends automatically.
- **No unpredictable request parameters** - the attacker can determine or guess every value needed (e.g. there is no CSRF token).

---

## Labs

| # | Lab | Level | Write-up |
|---|-----|-------|----------|
| 1 | CSRF vulnerability with no defenses | Apprentice | [View](./CSRF%20vulnerability%20with%20no%20defenses/README.md) |

> More labs will be added as they are completed.

---

## Common Defenses

- **CSRF tokens** - a unique, unpredictable, per-session (or per-request) value embedded in the form and validated server-side on every state-changing request.
- **`SameSite` cookies** - `SameSite=Strict` or `SameSite=Lax` instructs the browser not to send cookies with cross-site requests, breaking the core requirement of the attack.
- **Origin / Referer validation** - server-side checks that a state-changing request was initiated by the application's own domain.
- **Note:** CORS does *not* protect against CSRF - it controls whether JavaScript can *read* a cross-origin response, not whether the browser *sends* the request.

---

## Disclaimer

All testing was performed against intentionally vulnerable lab environments provided by PortSwigger's Web Security Academy. These techniques are documented for educational and defensive purposes only. Do not use them against systems you do not own or have explicit permission to test.
