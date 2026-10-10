# security-labs

Cloud incident investigations, web application security labs, Python security tooling and study notes.

I focus on DFIR and SOC work: digital forensics, incident response and detection engineering. Each write-up explains the root cause, how to detect the issue and how to fix it, not just how to solve the lab.

## Projects

| Project | Area | Highlights |
|---|---|---|
| [flaws2.cloud](flaws2.cloud/) | Cloud incident response | CloudTrail investigation with `jq`, credential theft detection, MITRE ATT&CK mapping |
| [flaws.cloud](flaws.cloud/) | Cloud offensive security | 6 levels of AWS misconfigurations: S3, EBS snapshots, SSRF to IMDS, IAM enumeration |
| [port-swigger](port-swigger/) | Web application security | 59 Apprentice labs across 25 vulnerability classes, each with remediation guidance |
| [sekurak](sekurak/) | Python tooling and training | Security scripts, CTF solutions, certifications (172h Sekurak.Academy, Wazuh, OSINT) |
| [CWL-notes](CWL-notes/) | Security fundamentals | Cyber Women Leaders program notes, CompTIA Security+ preparation |

### [flaws2.cloud](flaws2.cloud/) - AWS Incident Investigation (Defender Track)

Investigation of a compromised serverless and container application, using only CloudTrail logs, AWS CLI and `jq`.

- Rebuilt the attacker's timeline. Credentials were stolen from a Lambda function and an ECS task, then used from outside AWS
- Wrote detection logic for workload credentials used from non-AWS IP space. It flagged **5 of 37 events**, which turned out to be every use of the stolen keys
- Traced stolen access keys back to the `AssumeRole` events that issued them
- Mapped the attack to MITRE ATT&CK and proposed fixes, including GuardDuty detection

### [flaws.cloud](flaws.cloud/) - AWS Security Challenges

Six AWS misconfigurations, each level harder than the previous one:

- Public and over-permissive S3 buckets, credentials recovered from an exposed `.git` history
- Public EBS snapshot restored and mounted to extract secrets
- SSRF against the EC2 instance metadata service (IMDSv1) to steal IAM credentials
- Account enumeration through an over-permissive `SecurityAudit` policy

### [port-swigger](port-swigger/) - Web Security Academy

Write-ups for **59 Apprentice-level labs** covering 25 vulnerability classes, including access control, XSS, SQL and NoSQL injection, SSRF, XXE, JWT, OAuth, CORS, race conditions and web LLM attacks.

Every lab has the same structure: vulnerability overview, steps with screenshots, why it works and remediation.

### [sekurak](sekurak/) - Python Security Tooling and Training

Scripts and exercises from Sekurak courses and CTF challenges:

- File system monitoring, scanning and change reporting
- Multiprocessing for hash cracking and CRC32 collision search
- A rate-limited web crawler for finding CTF flags, small APIs built with FastAPI

The [certification folder](sekurak/certification/) lists completed training: Sekurak.Academy (4 semesters, 172h), Wazuh Expert, OSINT Toolbox and others.

### [CWL-notes](CWL-notes/) - Cyber Women Leaders

Study notes from the Cyber Women Leaders program (Mamo Pracuj Foundation), a free cybersecurity development program for women in Poland. Lecture notes, glossaries, commands and exercises, written in technical English as preparation for CompTIA Security+.

## Tools and Technologies

- **Cloud:** AWS CLI, CloudTrail, IAM, S3, EC2, ECS, ECR, Lambda
- **Log analysis and detection:** `jq`, Wazuh (SIEM), MITRE ATT&CK
- **Web security:** Burp Suite, JWT Editor, browser DevTools
- **Programming and tooling:** Python, FastAPI, Linux command line, Git

## Disclaimer

All work was done for educational purposes, in intentionally vulnerable lab environments (flaws.cloud, flaws2.cloud, PortSwigger Web Security Academy, CTF platforms). Credentials that appear in write-ups are expired or redacted. Do not use these techniques against systems without explicit permission.
