# Business Logic Vulnerabilities - PortSwigger Web Security Academy

Write-ups for the **Business Logic Vulnerabilities** track from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/logic-flaws). Each lab was solved hands-on; every write-up documents the root cause, the exploitation steps (with screenshots), why the flaw works, and how to remediate it.

**Tooling:** Burp Suite (Proxy, Repeater), browser.

---

## Labs

| # | Lab | Level | Core flaw | Impact |
|---|-----|-------|-----------|--------|
| 1 | [Excessive trust in client-side controls](./Excessive%20trust%20in%20client-side%20controls/README.md) | Apprentice | Server trusts a client-supplied price | Financial - buy a $1337 item for $0.50 |
| 2 | [High-level logic vulnerability](./High-level%20logic%20vulnerability/README.md) | Apprentice | No validation that quantity must be positive | Financial - negative quantity drives the total down |
| 3 | [Inconsistent security controls](./Inconsistent%20security%20controls/README.md) | Apprentice | Privilege check on a mutable, unverified attribute (email) | Privilege escalation - unauthorized admin access |
| 4 | [Flawed enforcement of business rules](./Flawed%20enforcement%20of%20business%20rules/README.md) | Apprentice | Coupon "one use" check only compares the last code | Financial - stack coupons to reach $0.00 |

---

## What these labs have in common

All four are **business logic flaws**: the application's individual operations are implemented correctly, but the rules that connect them are either missing, enforced in the wrong place, or enforced only once. None of them is a memory-safety or injection bug - they are failures of *intent*, which makes them invisible to most automated scanners and a good demonstration of manual review.

The recurring lesson: **never trust the client, and enforce every business rule on the server, at every point in the lifecycle where it matters.**
