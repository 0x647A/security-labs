# Information Disclosure

Write-ups for the **Information Disclosure** labs from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/information-disclosure).

Information disclosure (also known as information leakage) occurs when an application unintentionally reveals sensitive data to its users. Depending on the context, this can include data about other users, internal business data, or technical details about the application and its infrastructure. Attackers often use the leaked information to refine and escalate more serious attacks.

Each folder contains a step-by-step solution with annotated screenshots.

## Labs

| # | Lab | Difficulty | Write-up |
|---|-----|------------|----------|
| 1 | Information disclosure in error messages | Apprentice | [Read](./Information%20disclosure%20in%20error%20messages/) |
| 2 | Information disclosure on debug page | Apprentice | [Read](./Information%20disclosure%20on%20debug%20page/) |
| 3 | Source code disclosure via backup files | Apprentice | [Read](./Source%20code%20disclosure%20via%20backup%20files/) |
| 4 | Authentication bypass via information disclosure | Apprentice | [Read](./Authentication%20bypass%20via%20information%20disclosure/) |

## Common Sources of Information Disclosure

- Verbose error messages and unhandled exceptions (stack traces, framework versions).
- Debugging pages left enabled in production (`phpinfo`, actuator endpoints, debug toolbars).
- Backup and temporary files served as static content (`.bak`, `.swp`, `~`, `.old`).
- Files intended for the web crawlers, such as `robots.txt` and `sitemap.xml`, that inadvertently advertise hidden paths.
- Insecure configuration, including directory listing and default credentials.
- Version control history (`.git`) exposed in the web root.

## General Remediation Principles

- Return generic error messages to users and log technical details internally.
- Disable debugging features and remove debug endpoints before deploying to production.
- Never serve backup, temporary, or version control files from the web root.
- Do not treat `robots.txt` or path obscurity as a security control - it is public and advertises the paths it lists.
- Audit exactly what data each response and page exposes, and apply the principle of least privilege to it.

## Tools Used

- [Burp Suite](https://portswigger.net/burp) (Community Edition) - intercepting proxy and Repeater.
- A web browser configured to proxy traffic through Burp.

## Reference

- [PortSwigger - Information disclosure vulnerabilities](https://portswigger.net/web-security/information-disclosure)

---

> **Disclaimer:** These write-ups are intended for educational purposes only. All testing was performed against the deliberately vulnerable labs provided by the PortSwigger Web Security Academy. Never test techniques against systems you do not have explicit permission to assess.
