# OS Command Injection

Notes and walkthroughs for the **OS command injection** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/os-command-injection).

## What is OS command injection?

OS command injection (also known as shell injection) is a vulnerability that allows an attacker to execute arbitrary operating-system commands on the server that runs an application. It happens when an application passes unsafe, user-supplied data (such as form fields, cookies, or HTTP headers) to a system shell. The injected commands run with the privileges of the application, which frequently leads to full compromise of the server and any data it can reach.

## Labs

| Lab | Level | Notes |
|---|---|---|
| [OS command injection, simple case](./OS%20command%20injection%2C%20simple%20case/) | Apprentice | Inject a second command through the stock-checker to run `whoami`. |

## Impact

A successful attacker can typically:

- Read, modify, or delete files the application can access.
- Exfiltrate sensitive data (credentials, configuration, customer records).
- Pivot to other systems on the internal network.
- Achieve full remote code execution and take over the host.

## Key defenses

- **Never call out to a shell with user input.** Use language APIs that pass arguments directly to the target program instead of building a command string.
- **Validate input against an allowlist** of permitted values or a strict format (for example, integers only).
- **Run the application with least privilege** so that a successful injection has limited reach.

## Reference

- PortSwigger Web Security Academy: https://portswigger.net/web-security/os-command-injection

---

> These materials are for educational and authorized security-testing purposes only. Only test systems you have explicit permission to assess.
