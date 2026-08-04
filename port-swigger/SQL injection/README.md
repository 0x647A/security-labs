# SQL Injection

Write-ups for the **SQL injection** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/sql-injection).

Each lab folder contains a `README.md` with a vulnerability overview, the steps used to solve the lab, an explanation of why the attack works, and remediation guidance, along with screenshots of the exploitation.

---

## What Is SQL Injection?

SQL injection (SQLi) is a vulnerability that occurs when an application builds SQL queries by concatenating untrusted input directly into the query string. Because the database cannot distinguish between the developer's intended query structure and attacker-supplied input, the attacker can alter the meaning of the query.

Depending on the query and the database permissions, this can allow an attacker to:

- Read data they are not authorised to see, including other users' records.
- Bypass authentication and application logic.
- Modify or delete data.
- In some configurations, read or write local files or execute operating system commands.

SQL injection is tracked as [CWE-89](https://cwe.mitre.org/data/definitions/89.html) and falls under **A03:2021 - Injection** in the [OWASP Top 10](https://owasp.org/Top10/A03_2021-Injection/).

---

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| SQL injection vulnerability in WHERE clause allowing retrieval of hidden data | Apprentice | [Write-up](./SQL%20injection%20vulnerability%20in%20WHERE%20clause%20allowing%20retrieval%20of%20hidden%20data/README.md) |
| SQL injection vulnerability allowing login bypass | Apprentice | [Write-up](./SQL%20injection%20vulnerability%20allowing%20login%20bypass/README.md) |

---

## Core Defence

The single most effective defence against SQL injection is to **use parameterised queries (prepared statements)** for every query that includes untrusted input. Parameterisation sends the query structure and the data to the database separately, so input can never be interpreted as SQL syntax:

```python
# Safe - the query structure is fixed; `category` is only ever data.
cursor.execute(
    "SELECT * FROM products WHERE category = %s AND released = 1",
    (category,),
)
```

Supporting controls that reduce the impact of a vulnerability but do **not** replace parameterisation:

- **Allow-listing** for values that come from a fixed set, and for query parts that cannot be parameterised (table names, column names, `ORDER BY` clauses, sort direction).
- **Least privilege** - the application's database account should hold only the permissions it actually needs.
- **Generic error messages** - detailed database errors returned to the client make exploitation significantly easier.

Escaping input by hand and blocklisting keywords are unreliable and should not be relied upon as primary defences.

---

## Tools

- [Burp Suite](https://portswigger.net/burp) (Community Edition is sufficient for these labs) - intercepting proxy used to capture and modify requests.
- A browser configured to proxy traffic through Burp.

---

## Disclaimer

These write-ups are for educational purposes and document work on the PortSwigger Web Security Academy's intentionally vulnerable labs. Only test systems you own or have explicit written permission to test. Unauthorised testing is illegal.

---

Reference: https://portswigger.net/web-security/sql-injection
