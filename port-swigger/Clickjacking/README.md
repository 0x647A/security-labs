# Clickjacking - PortSwigger Web Security Academy

Write-ups and exploit walkthroughs for the **Clickjacking** labs from the
[PortSwigger Web Security Academy](https://portswigger.net/web-security/clickjacking).

Clickjacking (UI redressing) is an attack where a malicious page overlays a
nearly invisible iframe of a target site on top of decoy content. The victim
believes they are interacting with the attacker's page, but their clicks land
on actions inside the framed target site - executed in the victim's own
authenticated session.

Each folder contains a step-by-step write-up, the exploit code, and annotated
screenshots.

---

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| Basic clickjacking with CSRF token protection | Apprentice | [Read](./Basic%20clickjacking%20with%20CSRF%20token%20protection/README.md) |
| Clickjacking with a frame buster script | Apprentice | [Read](./Clickjacking%20with%20a%20frame%20buster%20script/README.md) |
| Clickjacking with form input data prefilled from a URL parameter | Apprentice | [Read](./Clickjacking%20with%20form%20input%20data%20prefilled%20from%20a%20URL%20parameter/README.md) |

---

## Key Takeaways

- **CSRF tokens do not prevent clickjacking** - the framed request comes from
  the real form, so the token is valid.
- **JavaScript frame busters are unreliable** - they can be neutralised with the
  iframe `sandbox` attribute.
- **The correct defense is HTTP headers**, enforced by the browser before any
  page content loads:
  - `X-Frame-Options: DENY` (or `SAMEORIGIN`)
  - `Content-Security-Policy: frame-ancestors 'none'`

---

> ⚠️ For educational and authorized testing only. These techniques target
> deliberately vulnerable PortSwigger lab environments.
