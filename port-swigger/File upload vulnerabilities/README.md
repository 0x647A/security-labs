# File Upload Vulnerabilities

Hands-on write-ups for the **File upload vulnerabilities** topic from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/file-upload). Each lab documents the vulnerability, a step-by-step exploitation walkthrough with screenshots, an explanation of the root cause, and concrete remediation guidance.

These write-ups focus not only on *how* to solve each lab, but on *why* the vulnerability exists and how to fix it. That is the perspective a security engineer brings to a finding.

---

## Labs

| Lab | Level | Vulnerability class |
| --- | --- | --- |
| [Remote code execution via web shell upload](./Remote%20code%20execution%20via%20web%20shell%20upload/) | Apprentice | Unrestricted file upload leading to RCE |
| [Web shell upload via Content-Type restriction bypass](./Web%20shell%20upload%20via%20Content-Type%20restriction%20bypass/) | Apprentice | Client-controlled Content-Type validation bypass |

---

## What these labs cover

- **Web shells and Remote Code Execution (RCE)** - uploading a server-side script that executes OS commands.
- **Weak upload validation** - what happens when a server trusts a file extension, MIME type, or the client-supplied `Content-Type` header.
- **Bypassing client-side controls** - using an intercepting proxy (Burp Suite) to modify a request after the browser has sent it.
- **Defense in depth** - why no single control is enough, and how content inspection, extension allowlists, storage location, and execution policy combine to prevent these attacks.

## Tools

- **Burp Suite** (Proxy, Repeater) for intercepting and modifying HTTP requests.
- Browser developer tools.
- A PHP web shell payload.

---

## Legal and ethical note

All testing was performed against intentionally vulnerable, disposable lab environments provided by PortSwigger for training purposes. These techniques must only ever be used against systems you own or have explicit written authorization to test.

---
