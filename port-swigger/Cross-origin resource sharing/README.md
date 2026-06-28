# Cross-Origin Resource Sharing (CORS) - Lab Write-ups

A collection of my solutions to the **Cross-Origin Resource Sharing (CORS)** labs from the
[PortSwigger Web Security Academy](https://portswigger.net/web-security/cors).

Each write-up documents the vulnerability, a step-by-step exploit, an explanation of *why*
the attack works, and - with a SOC perspective - **how to detect and remediate it**.

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

## Detection (SOC perspective)

Common signals when hunting for CORS abuse in logs:

- Requests to sensitive endpoints (e.g. `/accountDetails`) carrying an unexpected `Origin`
  header, or `Origin: null`.
- Responses where `Access-Control-Allow-Origin` matches an attacker-controlled or unknown
  origin, combined with `Access-Control-Allow-Credentials: true`.
- Exfiltration follow-ups - outbound requests to attacker infrastructure carrying
  response data in the URL (e.g. `GET /log?key=...`).

---

## Remediation summary

- Validate `Origin` against an explicit, static **allowlist** - never reflect it.
- Never trust the `null` origin, wildcards, or loose regex patterns.
- Only enable credentialed CORS where a legitimate cross-origin use case exists.

---

> ⚠️ All labs run on disposable PortSwigger instances. The lab IDs, exploit-server URLs, and
> API keys visible in the screenshots are ephemeral and expire after the session ends.
