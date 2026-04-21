# CyberWomen Leaders – Training 11: Penetration Testing and Security Audits

## 1. What is an Audit

### Security Audit
**What is it?**
- Checking compliance with **policies, standards** (e.g., ISO 27001, NIST, GDPR) and best practices  
- Assessment of the organization’s security level from both **process** and **technical** perspectives  

A security audit typically involves a systematic review of policies, procedures, network configurations, access controls and system settings. Auditors collect evidence through interviews, documentation review and technical testing to ensure that controls are implemented correctly and operating effectively. The audit process often produces a gap analysis that highlights areas of non-compliance and recommendations for remediation.  

**Why?**
- **Compliance, regulations**, verification of meeting selected standards  
- Ensures that legal, contractual and industry requirements are fulfilled before they lead to penalties or reputational damage  
- *"Are we operating according to requirements and are our processes compliant with standards and best practices?"*  

## 2. What is a Pentest

### Penetration Test
**What is it?**
- **Attack simulation** involving controlled attempts to detect security vulnerabilities in a target application, system or network  
- Ethical hackers mimic real-world adversaries to identify weaknesses before malicious actors can exploit them  

**Methodology:**
- **Practical approach** focused on exploiting discovered issues rather than just listing them  
- Typically involves:
  - **Active scanning** with specialized tools to detect open ports, services and known vulnerabilities  
  - **Manual attacks** such as crafting custom payloads, exploiting business logic flaws and testing authentication mechanisms  
  - **Software analysis** including source code review (in whitebox or graybox scenarios) to uncover hidden flaws in logic, input validation and error handling  

**Why?**
- Reveals **threats (vulnerabilities)** that automated scans or code reviews alone may miss  
- Provides a real-world perspective on the severity and exploitability of security gaps  
- Helps organizations prioritize remediation based on practical impact  
- *"Can someone realistically attack us and what would be the consequences?"*  

## 3. "I'll run a scanner and it's done"

### Limitations of Automated Scanners
- **"I'll run a scanner and it's done"** is a flawed approach
- **Automated network scanning**, even with expensive tools, does not replace manual penetration testing
- **Automated tools support** pentesting (e.g., Nessus, OpenVAS, Nuclei, SonarQube)

## 4. Example Vulnerability Scanners

### Free Vulnerability Scanners

**Network scanners:**
- **Nessus Essential** — Entry-level edition of Nessus for host and service vulnerability assessment, using a large plug‑in feed to detect missing patches, CVEs, and common misconfigurations; suitable for small scopes with basic compliance templates and IP limits.
- **OpenVAS** — Open-source scanner (Greenbone) providing broad vulnerability coverage with authenticated scans and compliance policies; relies on regularly updated community feeds and is well-suited for on‑prem deployments.
- **Nuclei** — High-speed, template-driven scanner (YAML) focusing on web assets and common exposures; excels at mass recon and CI/CD automation by running community or custom templates against large target inventories.

**Application code scanners:**
- **OWASP Dependency-Check** — Software composition analysis (SCA) that identifies vulnerable third‑party libraries by correlating project dependencies with known CVEs; supports multiple ecosystems and produces standardizable reports.
- **GitLeaks** — Secrets scanner for Git repositories that detects hardcoded credentials, API keys, and tokens across history and new commits; supports policies, allowlists, and CI integration to block sensitive leaks.
- **SonarQube Free** — Community static analysis for code quality and security hotspots across many languages; flags bugs and maintainability issues, with limited security/taint analysis compared to paid editions, and integrates with developer workflows.

## 5. Types of Pentests

### Based on Knowledge Scope

**Whitebox**
- Code and configuration analysis
- **Full access** to client documentation and solutions
- Manual and automated testing

**Graybox**
- Partial knowledge, such as **access to user accounts**
- Optional documentation access
- Manual and automated testing

**Blackbox**
- **Only publicly available information**
- No client-provided credentials
- Manual and automated testing

### By Team Perspective

**Red Team** - attacker role  
**Blue Team** - defender role  
**Purple Team** - collaborative Red and Blue roles  

## 6. Security of IT Systems

### Testing Areas

**Applications:**
- **Web**: Frontend, backend, APIs, web servers  
- **Mobile**: Mobile applications  
- **Desktop**: Desktop applications  

**Infrastructure:**
- **Network**: WAN, VPN, LAN, segmentation, Wi-Fi  
- **Servers**: Workstations, servers  
- **Active Directory**  

**Cloud:**
- **AWS/GCP/Azure** (whitebox reviews)  
- **Kubernetes**  
- **Office 365**, **G Suite**  
- **Docker**  

**Other areas:**
- **IoT**  
- **Social engineering** (phishing, vishing, on-site)  
- **Source code review**  
- **OSINT/recon**  
- **DDoS**  
- **Incident analysis**  
- **Red teaming**  
- **Insider threat**  
- **Threat modeling**  
- **Architecture review**  
- **Security consulting**  
- **Documentation review**  
- **Secure SDLC**  
- **E-commerce**  
- **Banking & finance**  
- **CMS**  
- **PII protection**  

## 7. Key Concepts

### Vulnerability Databases
**CVE (Common Vulnerabilities and Exposure)**
- Database of known reported vulnerabilities: https://www.cvedetails.com/  
- Maintained by various organizations, including **Polish CERT**: https://cert.pl/cvd/

### Disclosure Policies

**Responsible Disclosure**
- Inform the service owner about the vulnerability  
- Provide time (typically 90 days) to fix it before public release  

**Full Disclosure**
- Publish vulnerability details without waiting for a fix  

**Notes:**
- CVE assignments may lack thorough verification  
- Not all vulnerabilities are reported to vendors  

## 8. Vulnerability Assessment

### CVSS Calculator
**Common Vulnerability Scoring System (CVSS) version 3.0**  
- https://www.first.org/cvss/calculator/3-0  
- Standard method for assessing vulnerability severity  

## 9. Pegasus

### 0-day Vulnerabilities
**Business model:**
1. Purchase 0-days from researchers for high sums  
2. Vendor patches the exploited vulnerability  
3. Offer the exploit as a turnkey solution to nontechnical users  
4. Sell expensive licenses to recoup costs and profit  

**Example tool:** Pegasus  

## 10. Bug Bounty

### Bug Bounty Programs
- Companies invite external researchers to test their systems  
- Payment for each valid vulnerability report  
- **Example:** Apple offers up to \$100,000 for bypassing iPhone lock screen  
- https://security.apple.com/bounty/categories/  

## 11. Rules of Engagement

### Scope and Boundary Setting
**Key considerations:**
- Scope of testing (application, network, cloud)  
- Asset inventory and technology stack  
- Credentials and access levels provided  
- Testing methods (manual, automated, hybrid)  
- WAF status (enabled/disabled)  
- Privilege escalation policy  
- Infrastructure environment (on-premises vs. cloud)  
- Test environment (production vs. staging)  
- Vulnerability severity assessment (CVSS)  

## 12. Pentest Methodology

### Web Application Pentest Process
1. **Initial reconnaissance**  
2. **Application mapping**  
3. **Exploitation**  
4. **Reporting**  
5. **Retest (optional)**  

**Security considerations:**
- Plan tests to minimize impact  
- Be aware of exploit risks (system crashes, data loss)  
- Pay special attention to buffer and integer overflows  

## 13. Passive vs Active Reconnaissance

### Passive Reconnaissance
Passive recon collects information without directly touching the target’s systems, minimizing detection risk and legal exposure. Typical sources include public records, search engines, and third‑party datasets that describe the target’s assets and behaviors. The goal is to build an initial asset inventory and threat model before any active probing.
- Open-source intelligence (OSINT): search engines, site operators (dorking), Wayback Machine, news, job postings, social media.
- Internet datasets: Shodan/Censys, Certificate Transparency (crt.sh), DNSDB, paste sites, breach corpuses.
- Public registries: WHOIS/RDAP, ASN/IP allocations, company filings, SSL/TLS cert metadata.
- Code and artifacts: public Git repositories, packages, container registries, exposed docs with metadata (PDF/DOCX exif).
- Third-party footprint: vendors, CDNs, marketing platforms, analytics IDs that correlate to subdomains and apps.

### Active Reconnaissance
Active recon interacts with the target and can trigger logs, alerts, or rate limits, but yields fresher and more precise technical data. It validates passive findings, maps live surfaces, and identifies reachable services, versions, and misconfigurations.
- Host discovery and port scanning to enumerate reachable services and trust boundaries.
- Service and version identification (banner grabbing, TLS fingerprinting, protocol handshakes).
- Web surface mapping: technology fingerprinting, virtual host and subdomain discovery, directory/file enumeration.
- Auth and session surface review: login flows, MFA prompts, password policies, rate limits, lockout behavior.
- Environment cues: WAF/IDS fingerprinting, caching/CDN behavior, error handling, debug headers.
- Network/service enumeration: SMB/LDAP/RDP/SSH/SNMP specifics, mail server VRFY/RCPT tests.

### Attack Phase
The attack phase moves from mapping to validation of risk via controlled exploitation and credential use, under the agreed rules of engagement. Findings here demonstrate practical impact and help prioritize remediation by evidence rather than theoretical severity.
- Use of valid or brute‑forced credentials (e.g., password spraying, credential stuffing under throttling constraints).
- Automated and manual exploitation of vulnerabilities, misconfigurations, and insecure defaults with careful impact control.

## 14. Buffer Overflow

### Explanation
1. Program allocated specific memory buffer  
2. Attacker submits oversized input  
3. Overflow overwrites adjacent memory areas  

When the overwritten data includes control structures (for example, a saved return address on the stack or a function pointer), execution flow can be hijacked to attacker‑controlled code or gadgets, leading to arbitrary code execution; otherwise, the process often crashes or leaks memory contents. Modern targets include stack and heap buffers, object fields, and protocol parsers that trust length fields, especially in native code written without strict bounds checks. Typical mitigations include rigorous bounds checking and safe APIs, compiler and platform defenses (stack canaries, ASLR, DEP/NX, PIE, Fortify), and adopting memory‑safe languages for high‑risk components.

**Impact example:** BlueKeep vulnerability  

## 15. Integer Overflow

### Explanation
1. Maximum 32-bit int value (2,147,483,647)  
2. Increment by 1 causes wrap-around to –2,147,483,648  

In signed arithmetic, overflow can wrap or trigger undefined behavior depending on language and compiler, while unsigned types wrap modulo \(2^n\), both of which can corrupt logic that relies on counts, sizes, or indices. Security impact arises when overflowed values drive memory allocations, copy lengths, or authorization checks, causing under‑allocation followed by buffer overflow, negative indexing, or bypassed limits. Mitigations include explicit range checks, using wider or checked integer types, compiler/runtime sanitizers, fuzzing with boundary cases, and defensive parsing that treats any arithmetic near limits as suspicious. 

## 16. Post-Exploitation Activities

### Steps After Gaining Access
1. **Privilege escalation** to root or admin — elevate from low-privileged footholds to maximize control and visibility, using safe, agreed techniques that minimize system impact.  
2. **Persistence** mechanisms (e.g., new user accounts, SSH keys) — maintain controlled access across reboots or security resets, favoring low-noise methods aligned with operational security.  
3. **Pivoting** to compromise additional network segments — route traffic through the compromised host to reach internal subnets and services otherwise inaccessible.  

Beyond these steps, prioritize credential harvesting (memory, LSASS/Keychain equivalents, password stores), careful data access limited to agreed samples, and lateral movement only within scope. Maintain clear evidence collection, timestamped notes, and artifacts for reproducibility, and plan for cleanup and restoration to pre-test state as part of the engagement deliverables.

## 17. Mobile Devices

### Mobile OS Security
- **Android/iOS** based on Linux kernel  
- **Sandboxing** isolates apps  
- **Digital signatures** enforce chain of trust  
- Restricts installation of untrusted apps  

Both platforms add runtime permission prompts, app entitlements, and mandatory code signing that limit inter-app data flows and API access. Security services like SELinux (Android) and hardened sandbox profiles (iOS) constrain processes, while the verified boot chain prevents unsigned system images from loading in default configurations.

### Device Preparation
**Rooting (Android) vs. Jailbreaking (iOS)**
- Android: official support for unlocking bootloaders  
- iOS: requires security exploits to break the sandbox  

In authorized testing environments, typical prep includes enabling developer modes, installing platform SDK tools (ADB/Xcode), configuring an interception proxy and custom test CA, and temporarily bypassing certificate pinning via dynamic instrumentation. Common tooling for gray/white-box workflows includes Frida/Objection, local debuggers, and file-system access utilities; all activities must respect scope, data handling rules, and agreed operational safeguards.
