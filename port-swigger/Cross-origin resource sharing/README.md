# Cross-Origin Resource Sharing (CORS) - Lab Write-ups

A collection of my solutions to the **Cross-Origin Resource Sharing (CORS)** labs from the
[PortSwigger Web Security Academy](https://portswigger.net/web-security/cors).

Each write-up documents the vulnerability, a step-by-step exploit, an explanation of *why*
the attack works, and **how to remediate it**.

Tools used: **Burp Suite** (Repeater, exploit server) and the browser developer tools.

---

## Labs

| # | Lab | Level | Write-up |
|---|-----|-------|----------|
| 1 | CORS vulnerability with basic origin reflection | Apprentice | [Read](./CORS%20vulnerability%20with%20basic%20origin%20reflection/README.md) |
| 2 | CORS vulnerability with trusted null origin | Apprentice | [Read](./CORS%20vulnerability%20with%20trusted%20null%20origin/README.md) |

---

## What is CORS?

CORS is the browser mechanism that controls whether JavaScript running on one origin is
allowed to read responses from another origin. By default the same-origin policy blocks
cross-origin reads; CORS response headers (`Access-Control-Allow-Origin` and
`Access-Control-Allow-Credentials`) are the server's way of opting in to relax that
restriction.

When these headers are configured carelessly - by reflecting the request `Origin`, trusting
`null`, or using overly broad patterns - an attacker's site can read authenticated responses
from the victim's session and steal sensitive data such as API keys.

---

## Recognizing CORS misconfiguration

Signals that indicate a CORS policy is exploitable, worth checking for during testing or
code review:

- A response's `Access-Control-Allow-Origin` header exactly mirrors whatever `Origin` was
  sent in the request, rather than a fixed value from a server-side allowlist.
- `Access-Control-Allow-Origin: null` is present, or the server accepts `Origin: null`.
- `Access-Control-Allow-Credentials: true` is combined with either of the above - this is
  the combination that actually allows an attacker to read authenticated responses.

---

## Remediation summary

- Validate `Origin` against an explicit, static **allowlist** - never reflect it.
- Never trust the `null` origin, wildcards, or loose regex patterns.
- Only enable credentialed CORS where a legitimate cross-origin use case exists.

---

> ⚠️ All labs run on disposable PortSwigger instances. The lab IDs, exploit-server URLs, and
> API keys visible in the screenshots are ephemeral and expire after the session ends.
