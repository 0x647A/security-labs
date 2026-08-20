# GraphQL API Vulnerabilities

Write-ups for the **GraphQL API vulnerabilities** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/graphql).

Each write-up walks through the vulnerability, the exploitation steps (with screenshots), why the attack works, and how to remediate it.

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| Accessing private GraphQL posts | Apprentice | [Read](./Accessing%20private%20GraphQL%20posts/README.md) |

## Topics Covered

- GraphQL introspection and schema discovery
- Accessing fields the frontend never requests
- Broken field-level and object-level authorization
- Remediation: disabling introspection, enforcing authorization, query depth and complexity limits

## Disclaimer

These notes are for educational purposes and were produced against PortSwigger's intentionally vulnerable lab environments. Only test systems you are authorized to test.
