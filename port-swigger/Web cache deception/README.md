# Web Cache Deception

Write-ups and walkthroughs for the **Web Cache Deception** topic from the [PortSwigger Web Security Academy](https://portswigger.net/web-security/web-cache-deception).

Web cache deception is an attack in which an attacker tricks a caching layer (a CDN or reverse proxy) into storing a response that contains sensitive, user-specific data, and then retrieves that cached response as an unauthenticated user. It typically relies on a discrepancy between how the cache and the origin server interpret a URL.

---

## Labs

| Lab | Level | Write-up |
| --- | --- | --- |
| Exploiting path mapping for web cache deception | Apprentice | [Write-up](Exploiting%20path%20mapping%20for%20web%20cache%20deception/README.md) |

---

## Reference

- [Web cache deception (PortSwigger Web Security Academy)](https://portswigger.net/web-security/web-cache-deception)

---

> **Disclaimer:** This material is for educational purposes and authorized security testing only. All techniques are demonstrated against PortSwigger's intentionally vulnerable lab environment. Do not use them against systems you do not have explicit permission to test.
