# Path Traversal

Notes and lab write-ups for the **Path traversal** (directory traversal) topic from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/file-path-traversal).

Path traversal occurs when an application builds a filesystem path from user-controlled input without adequate validation, allowing an attacker to use `../` sequences to escape the intended directory and read (or sometimes write) arbitrary files on the server.

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| File path traversal, simple case | Apprentice | [Read](./File%20path%20traversal%2C%20simple%20case/README.md) |

## References

- Web Security Academy - Path traversal: <https://portswigger.net/web-security/file-path-traversal>
- OWASP - Path Traversal: <https://owasp.org/www-community/attacks/Path_Traversal>
