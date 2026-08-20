# NoSQL Injection

Walkthroughs and notes for the **NoSQL injection** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/nosql-injection).

NoSQL injection occurs when user-controlled input is passed into a NoSQL query (for example, a MongoDB query) without proper validation or sanitization. Depending on how the query is built, an attacker can inject query operators or, in some cases, JavaScript expressions to alter the query's logic - extracting data, bypassing filters, or bypassing authentication entirely.

There are two broad categories:

- **Syntax injection** - breaking out of a query by injecting characters or expressions (analogous to classic SQL injection).
- **Operator injection** - injecting NoSQL query operators (such as `$ne`, `$regex`, or `$gt`) to change the query's behavior.

---

## Labs

| # | Lab | Type | Level |
|---|-----|------|-------|
| 1 | [Detecting NoSQL injection](./Detecting%20NoSQL%20injection/) | Syntax injection | Apprentice |
| 2 | [Exploiting NoSQL operator injection to bypass authentication](./Exploiting%20NoSQL%20operator%20injection%20to%20bypass%20authentication/) | Operator injection | Apprentice |

---

## Prerequisites

- A [PortSwigger Web Security Academy](https://portswigger.net/web-security) account (free).
- [Burp Suite](https://portswigger.net/burp) (Community Edition is sufficient) configured as an intercepting proxy for your browser.

---

## Remediation Summary

The same defensive principles apply across both labs:

- **Validate input types.** Reject non-string values where a string is expected, so an attacker cannot smuggle in an operator object such as `{"$ne": null}`.
- **Sanitize special characters and operators.** Strip or reject query operators and characters (for example, keys beginning with `$`, and characters such as `'`, `"`, `\`, `;`, `||`) from user-supplied input.
- **Use an ODM/ODL with a strict schema.** Libraries such as [Mongoose](https://mongoosejs.com/) enforce expected field types and reject unexpected object structures.
- **Apply the principle of least privilege.** Grant the application's database account only the permissions it needs.

---

## Disclaimer

This material is provided for educational purposes only. All testing was performed against the intentionally vulnerable labs hosted by PortSwigger. Never test these techniques against systems you do not own or do not have explicit written permission to test.
