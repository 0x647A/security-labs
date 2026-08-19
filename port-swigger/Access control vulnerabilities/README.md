# Access Control Vulnerabilities

9 Apprentice-level labs from [PortSwigger Web Security Academy](https://portswigger.net/web-security/access-control).

Access control vulnerabilities arise when an application fails to enforce restrictions on what authenticated (or unauthenticated) users are permitted to do or see. The labs below cover vertical privilege escalation, horizontal privilege escalation, and IDOR.

---

## Labs

| Lab | Vulnerability Type |
|---|---|
| [Unprotected admin functionality](Unprotected%20admin%20functionality/README.md) | Missing access control - admin panel with no auth check |
| [Unprotected admin functionality with unpredictable URL](Unprotected%20admin%20functionality%20with%20unpredictable%20URL/README.md) | Security through obscurity - admin URL leaked in client-side JS |
| [User role controlled by request parameter](User%20role%20controlled%20by%20request%20parameter/README.md) | Client-side authorization - role stored in editable cookie |
| [User role can be modified in user profile](User%20role%20can%20be%20modified%20in%20user%20profile/README.md) | Mass assignment - `roleid` accepted in profile update request |
| [User ID controlled by request parameter](User%20ID%20controlled%20by%20request%20parameter/README.md) | IDOR - predictable username in `id` parameter, no ownership check |
| [User ID controlled by request parameter, with unpredictable user IDs](User%20ID%20controlled%20by%20request%20parameter%2C%20with%20unpredictable%20user%20IDs/README.md) | IDOR - GUID-based `id`, GUID leaked via public author profile |
| [User ID controlled by request parameter with data leakage in redirect](User%20ID%20controlled%20by%20request%20parameter%20with%20data%20leakage%20in%20redirect/README.md) | IDOR - sensitive data included in 302 redirect response body |
| [User ID controlled by request parameter with password disclosure](User%20ID%20controlled%20by%20request%20parameter%20with%20password%20disclosure/README.md) | IDOR + sensitive data exposure - password pre-filled in HTML input |
| [Insecure direct object references](Insecure%20direct%20object%20references/README.md) | IDOR - sequential file IDs for chat transcripts, no auth check |
