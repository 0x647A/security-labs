# flaws.cloud — AWS Security Challenges

Six-level AWS security challenge covering real-world cloud misconfigurations. Each level requires exploiting a progressively more complex flaw to advance — from public S3 buckets to SSRF against the instance metadata service.

**[flaws.cloud](http://flaws.cloud/)**

---

## Levels

| Level | Vulnerability | Technique |
|---|---|---|
| [1](level1/) | Public S3 bucket | Bucket enumeration via DNS + directory listing |
| [2](level2/) | S3 ACL: All Authenticated Users | AWS CLI access with any valid account |
| [3](level3/) | `.git` directory exposed in S3 | Credential recovery from Git commit history |
| [4](level4/) | Public EBS snapshot | Volume restore + filesystem mount |
| [5](level5/) | SSRF → IMDSv1 | Metadata service pivot to extract IAM credentials |
| [6](level6/) | SecurityAudit policy abuse | Full account enumeration + API Gateway discovery |

---

## Tools Used

- AWS CLI
- nslookup
- git
- curl

---

## Disclaimer

All challenges are solved in the intentionally vulnerable flaws.cloud environment. Credentials appearing in writeups are expired CTF keys provided by the platform.
