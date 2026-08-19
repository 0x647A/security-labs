# Cross-Site Scripting (XSS) - Lab Write-ups

Hands-on write-ups for the **Cross-Site Scripting** labs from the
[PortSwigger Web Security Academy](https://portswigger.net/web-security/cross-site-scripting).
Each lab has its own folder containing a detailed write-up (`README.md`) and screenshots
documenting the exploitation and the solved state.

This repository is part of my security learning portfolio as I work toward a
**Junior AppSec / Penetration Testing** role. For every lab I document not only *how* the
vulnerability is exploited, but also *why* it works and - most importantly - *how to remediate
it*, since understanding root cause is what separates running a payload from actually
understanding the vulnerability.

---

## What is Cross-Site Scripting?

Cross-Site Scripting (XSS) is a web vulnerability that lets an attacker inject and execute
malicious JavaScript in another user's browser, in the context of a vulnerable site. It can be
used to steal session cookies, perform actions on behalf of the victim, capture keystrokes, or
deface content. XSS is commonly split into three categories:

- **Reflected XSS** - the payload is echoed back immediately in the HTTP response.
- **Stored XSS** - the payload is saved server-side and served to every future visitor.
- **DOM-based XSS** - the vulnerability lives entirely in client-side JavaScript, which reads a
  *source* (e.g. `location.search`) and writes it into a dangerous *sink* (e.g. `innerHTML`).

A recurring theme across these labs is **context-aware output encoding**: the correct defense
depends on *where* untrusted data is placed (HTML body, HTML attribute, JavaScript string, or a
URL scheme).

---

## Labs

| # | Lab | Type | Level |
|---|-----|------|-------|
| 1 | [Reflected XSS into HTML context with nothing encoded](Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/) | Reflected | Apprentice |
| 2 | [Stored XSS into HTML context with nothing encoded](Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded/) | Stored | Apprentice |
| 3 | [DOM XSS in document.write sink using source location.search](DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search/) | DOM-based | Apprentice |
| 4 | [DOM XSS in innerHTML sink using source location.search](DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search/) | DOM-based | Apprentice |
| 5 | [DOM XSS in jQuery anchor href attribute sink using location.search source](DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source/) | DOM-based | Apprentice |
| 6 | [DOM XSS in jQuery selector sink using a hashchange event](DOM%20XSS%20in%20jQuery%20selector%20sink%20using%20a%20hashchange%20event/) | DOM-based | Apprentice |
| 7 | [Reflected XSS into attribute with angle brackets HTML-encoded](Reflected%20XSS%20into%20attribute%20with%20angle%20brackets%20HTML-encoded/) | Reflected | Apprentice |
| 8 | [Reflected XSS into a JavaScript string with angle brackets HTML-encoded](Reflected%20XSS%20into%20a%20JavaScript%20string%20with%20angle%20brackets%20HTML%20encoded/) | Reflected | Apprentice |
| 9 | [Stored XSS into anchor href attribute with double quotes HTML-encoded](Stored%20XSS%20into%20anchor%20href%20attribute%20with%20double%20quotes%20HTML-encoded/) | Stored | Apprentice |

---

## Write-up structure

Every lab folder follows the same template:

1. **Vulnerability Overview** - what the flaw is, plus the *source* and *sink* for DOM-based labs.
2. **Steps to Solve the Lab** - reproducible, step-by-step exploitation, with screenshots evidencing each step and the solved lab.
3. **Why This Works** - the underlying mechanism.
4. **Remediation** - how to fix and defend against it.

---

## Disclaimer

All testing was performed exclusively against the intentionally vulnerable, sandboxed labs
provided by the PortSwigger Web Security Academy. These techniques must only be used on systems
you own or are explicitly authorized to test.
