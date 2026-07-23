# Insecure Deserialization

Notes and hands-on write-ups for the **Insecure deserialization** topic from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/deserialization).

---

## What Is Insecure Deserialization?

Serialization converts an in-memory object into a byte stream (for storage or transmission); deserialization reconstructs the object from that stream. **Insecure deserialization** happens when an application deserializes attacker-controllable data without validating it.

The impact ranges from tampering with application logic (for example, privilege escalation by flipping an `admin` flag) to remote code execution through gadget chains, depending on the language and the classes available at deserialization time.

Common warning signs:

- Session state, tokens, or other data are serialized and sent to the client (often base64-encoded).
- The serialized data is not signed or otherwise integrity-protected.
- The application calls a native deserialization routine (for example, PHP's `unserialize()`, Java's `ObjectInputStream.readObject()`, Python's `pickle.loads()`) on untrusted input.

---

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| Modifying serialized objects | Apprentice | [View](./Modifying%20serialized%20objects/README.md) |

---

## General Remediation

- Avoid deserializing data from untrusted sources whenever possible.
- If serialized data must cross a trust boundary, protect it with a cryptographic signature (for example, HMAC) and verify the signature before deserializing.
- Prefer simple, data-only formats such as JSON over native object serialization.
- Keep session state on the server and expose only an opaque, random token to the client.

---

## Reference

- [Insecure deserialization](https://portswigger.net/web-security/deserialization) - PortSwigger Web Security Academy
