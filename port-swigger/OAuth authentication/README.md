# OAuth Authentication

Write-ups and proof-of-concept notes for the **OAuth authentication** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/oauth).

OAuth 2.0 is an authorization framework that lets applications access a user's data on another service without handling their credentials. It is widely used both for delegated authorization and, through social-login patterns, for authentication. Misconfigurations in the OAuth flow - or in how the client application consumes the returned tokens and identity data - can lead to authentication bypass and full account takeover.

## Labs

| Lab | Level | Vulnerability |
|-----|-------|---------------|
| [Authentication bypass via OAuth implicit flow](Authentication%20bypass%20via%20OAuth%20implicit%20flow/) | Apprentice | The backend trusts client-supplied identity data (`email`) instead of validating it against the OAuth token, allowing account takeover. |

## Reference

- [PortSwigger - OAuth authentication](https://portswigger.net/web-security/oauth)
- [OAuth 2.0 (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)
