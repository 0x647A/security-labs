# WebSockets

Write-ups of PortSwigger Web Security Academy labs covering WebSocket security - a persistent, bidirectional communication channel that is frequently overlooked during security testing because it operates outside the traditional request/response HTTP model.

## Why WebSockets Matter for Security

WebSocket connections are established via an HTTP handshake (`Upgrade: websocket`) and then switch to a full-duplex TCP channel. Once upgraded, messages are no longer standard HTTP requests, which means:

- Traditional HTTP-layer defenses (some WAFs, CSRF tokens tied to HTTP forms) may not cover WebSocket traffic.
- Developers often apply less input validation and output encoding to WebSocket messages than to HTTP parameters.
- The initial handshake can itself be vulnerable to Cross-Site WebSocket Hijacking (CSWSH) if the server relies solely on ambient authentication (cookies) without validating the `Origin` header.

Burp Suite supports intercepting and modifying WebSocket messages via **Proxy > WebSockets history** and the **WebSockets** interception toggle, making it possible to manipulate frames in transit just like HTTP requests.

## Labs

| Lab | Vulnerability | Level |
|---|---|---|
| [Manipulating WebSocket messages to exploit vulnerabilities](<Manipulating WebSocket messages to exploit vulnerabilities/README.md>) | Stored XSS via unencoded WebSocket message content | Apprentice |

## Key Takeaways

- Treat every WebSocket message as untrusted input, exactly like an HTTP parameter.
- Always HTML-encode data before inserting it into the DOM, regardless of the transport (HTTP or WebSocket).
- Validate the `Origin` header on the server during the WebSocket handshake to prevent cross-site hijacking.
- Use Burp's WebSockets history and interception features to audit real-time applications (chat, notifications, live dashboards) for the same classes of vulnerabilities found in traditional HTTP endpoints.

---

Reference: https://portswigger.net/web-security/websockets
