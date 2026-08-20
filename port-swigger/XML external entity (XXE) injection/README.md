# XML External Entity (XXE) Injection

Write-ups for the PortSwigger Web Security Academy labs on XML External Entity (XXE) injection. Each lab folder contains a step-by-step walkthrough, request/response screenshots, an explanation of why the vulnerability works, and remediation guidance.

---

## What is XXE?

XML External Entity (XXE) injection is a vulnerability that arises when an XML parser processes a `DOCTYPE` declaration containing an externally defined entity, and the application allows that entity to be resolved. If external entity resolution is enabled (as it is by default in many XML parsers), an attacker can define an entity that points to a local file, an internal network resource, or another external system, and have its content returned inside the application's response.

Depending on the application's configuration and network placement, XXE can be leveraged to:

- Read arbitrary files from the server's filesystem.
- Perform server-side request forgery (SSRF) against internal or cloud services.
- Enumerate internal networks by probing hosts and ports.
- Cause denial of service (for example, via the "billion laughs" entity expansion attack).
- In some cases, achieve remote code execution, depending on the parser and available modules.

## Labs in This Repository

| Lab | Technique | Level |
|---|---|---|
| [Exploiting XXE using external entities to retrieve files](./Exploiting%20XXE%20using%20external%20entities%20to%20retrieve%20files/README.md) | Local file disclosure via a `SYSTEM` entity pointing to `file:///etc/passwd` | Apprentice |
| [Exploiting XXE to perform SSRF attacks](./Exploiting%20XXE%20to%20perform%20SSRF%20attacks/README.md) | SSRF against the AWS EC2 instance metadata service to steal IAM credentials | Apprentice |

## General Remediation

Regardless of the specific attack vector, the most effective fix is to disable dangerous XML features at the parser level:

- Disable resolution of external general and parameter entities.
- Disable DTD (Document Type Definition) processing entirely if it is not required.
- Prefer a data format that does not support entities (such as JSON) when XML is not a hard requirement.
- Keep the XML parsing library up to date, since safe defaults have improved over time but vary by language and library.

See each lab's `Remediation` section for language-specific configuration examples.

---

Source: [PortSwigger Web Security Academy - XXE injection](https://portswigger.net/web-security/xxe)
