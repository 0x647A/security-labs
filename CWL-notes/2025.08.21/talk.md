# CyberWomen Leaders – Training 8: Application Security – OWASP TOP 10

## OWASP TOP 10 – Introduction and Applications

OWASP TOP 10 presents 10 most serious security risks concerning web applications, updated based on reports from companies specializing in penetration testing and observations of evolving threats.

## OWASP TOP 10 – Detailed Applications and Use Cases

### **Reference Point for Security Classification**
- **Testing Tools Integration:** Many automated security scanning tools like Sonarqube, Checkmarx, and Veracode classify discovered vulnerabilities according to OWASP TOP 10 categories. This standardized classification helps development teams quickly understand the severity and type of security issues.
- **Penetration Testing Reports:** Security firms like Securitum include OWASP TOP 10 references in their pentest reports. When a vulnerability is found, it's mapped to the relevant OWASP category (e.g., "This SQL injection vulnerability falls under A03:2021 - Injection"). This mapping helps clients:
  - Find additional technical documentation and remediation guides
  - Understand the broader context of the vulnerability
  - Prioritize fixes based on industry-recognized risk levels
  - Communicate security issues to stakeholders using common terminology

### **Security Implementation Starting Point**
- **For Organizations Without Security Processes:** Companies that have never implemented formal security practices can use OWASP TOP 10 as their initial roadmap. While it only covers 10 major risks (not comprehensive security), it provides:
  - **Immediate Impact:** Focus on the most critical and common vulnerabilities first
  - **Resource Allocation:** Helps prioritize limited security budgets and developer time
  - **Team Training:** Provides structured learning path for development teams new to security
  - **Quick Wins:** Addressing these 10 areas can significantly improve overall security posture
- **Gradual Implementation:** Teams can tackle one category at a time, building security capabilities incrementally rather than being overwhelmed by comprehensive security frameworks.

### **Penetration Testing Inspiration and Methodology**
- **Systematic Testing Approach:** Pentesters use OWASP TOP 10 as a structured checklist to ensure comprehensive coverage during security assessments. Each category provides:
  - **Attack Vectors:** Multiple techniques to test for each vulnerability type
  - **Testing Methodologies:** Specific approaches for discovering each category of flaw
  - **External References:** Links to detailed testing guides and tools
  - **Real-world Scenarios:** Practical examples of how vulnerabilities manifest
- **Knowledge Transfer:** Helps junior pentesters learn systematic vulnerability assessment approaches
- **Client Communication:** Provides common vocabulary for explaining findings to technical and business stakeholders

### **Compliance and Certification Framework**
- **Business Requirements:** Many organizations require security attestation before:
  - Processing employee personal data
  - Handling customer financial information  
  - Integrating with enterprise systems
  - Meeting vendor security requirements
- **Market Recognition:** OWASP TOP 10 has become a de facto industry standard because:
  - **Universal Acceptance:** Recognized by security professionals worldwide
  - **Regular Updates:** Maintained and updated based on current threat landscape
  - **Practical Focus:** Covers real-world, commonly exploited vulnerabilities
- **Alternative to Complex Standards:** When clients don't specify detailed requirements like PCI DSS or ISO 27001, OWASP TOP 10 compliance provides:
  - **Baseline Security:** Demonstrates commitment to fundamental security practices
  - **Cost-Effective Assessment:** Less expensive than comprehensive security audits
  - **Time-Efficient Implementation:** Can be addressed relatively quickly compared to full security frameworks

### **Important Limitations and Considerations**
- **OWASP's Official Position:** The organization explicitly discourages claims of "full OWASP TOP 10 compliance" because:
  - **Tool Limitations:** No single tool or assessment can comprehensively detect all variants of these vulnerabilities
  - **Design Issues:** Some categories like A04:2021-Insecure Design require architectural review, not just technical testing
  - **Contextual Nature:** Security effectiveness depends heavily on implementation context and business requirements
- **Complementary Approach:** OWASP TOP 10 should be used alongside, not instead of, comprehensive security programs including secure development lifecycle, threat modeling, and regular security assessments.

> **Note:** OWASP discourages unequivocal assurances about "full compliance with OWASP TOP 10" – due to the complexity and nature of some risks, tools don't detect everything, and the list doesn't cover all types of threats.

## How to analyze each OWASP TOP 10 point?
Each point contains:
- Risk description and example attacks and scenarios,
- Protection methods (often linked to OWASP Cheat Sheet Series),
- Detailed attack scenarios,
- References and CWE (Common Weakness Enumeration) examples.

## Detailed description of OWASP TOP 10 (2021)

### 1. **A01:2021 – Broken Access Control**

**Description:**  
Broken Access Control occurs when an application fails to enforce what authenticated users are allowed to do. Attackers can exploit these weaknesses to access or modify data and functionality beyond their privileges. This risk covers any scenario where users can read, write, update or delete resources they shouldn’t, including unauthorized API endpoints, hidden functionalities, or direct object references.

**Key Examples:**  
- **IDOR (Insecure Direct Object Reference):**  
  An attacker manipulates a parameter (e.g., `GET /user/profile?id=123`) to access another user’s data (`id=124`) without proper permission checks.  
- **Vertical Privilege Escalation:**  
  A standard user escalates to an administrator role by guessing or tampering with role identifiers in requests (e.g., changing `role=user` to `role=admin`).

**Common Attack Vectors:**  
- Missing server-side authorization checks on endpoints  
- Unprotected direct object references in URLs, forms, or API calls  
- Forced browsing of administrative or developer resources  
- Bypassing UI controls by sending crafted requests directly to the backend

**Recommendations:**  
- Enforce authorization logic on the server for every request, even when controlled via the UI  
- Avoid exposing raw identifiers; use indirect references or mapping layers  
- Implement a centralized access control mechanism (e.g., middleware or policy engine) so that checks are consistent across the application  
- Regularly test endpoints with automated tools and manual reviews to ensure no unintended access paths exist  
- Log denied access attempts and monitor for suspicious activity patterns  

### 2. **A02:2021 – Cryptographic Failures**

**Description:**  
Cryptographic Failures occur when applications improperly implement or entirely omit cryptography, leaving sensitive data exposed in transit or at rest. This category covers failures in encryption, key management, randomness, and integrity verification that attackers can exploit to intercept, modify, or forge data.

**Includes among others:**  
- **Weak or missing encryption in transit:** HTTP connections without TLS or misconfigured TLS versions/ciphers allow eavesdropping and manipulation.  
- **Weak or missing encryption at rest:** Unencrypted databases, logs, or backups expose sensitive information if storage is compromised.  
- **Errors in key management:** Hard-coded keys, weak key rotation policies, or insecure storage of keys enable attackers to decrypt or sign data.  
- **Weak randomness sources:** Non-cryptographic random generators (e.g., `Math.random()`) used for tokens, IVs, or salts can be predicted, undermining encryption and authentication.  
- **Improper password storage:** Storing plaintext or using fast hash functions (e.g., MD5, SHA1) without salting makes passwords vulnerable to brute-force and rainbow-table attacks.  
- **Lack of certificate verification:** Skipping full chain validation or ignoring hostname mismatches leads to man-in-the-middle attacks.

**Common Attack Scenarios:**  
- Downgrade to TLS 1.0/1.1 or use of weak cipher suites  
- Reuse of the same IV/nonce in symmetric encryption  
- Extraction of static keys from binaries or configuration files  
- Successful offline password cracking due to fast hashes  
- Impersonation by trusting self-signed or expired certificates

**Recommendations:**  
- **Enforce strong protocols and ciphers:** Use TLS v1.2+ or TLS v1.3, disable legacy protocols, and prefer AEAD ciphers (AES-GCM, ChaCha20-Poly1305).  
- **Use approved asymmetric standards:** RSA 2048+ or elliptic-curve algorithms (e.g., ECDSA with P-256) with appropriate padding.  
- **Secure key management:** Store keys in hardware security modules (HSMs), KMS services, or dedicated secret volumes; never hard-code in source.  
- **Generate cryptographic randomness:** Use cryptographically secure generators (e.g., `/dev/urandom`, `java.security.SecureRandom`) for salts, IVs, and tokens.  
- **Hash passwords securely:** Employ adaptive, memory-hard functions—bcrypt, scrypt, or Argon2—with per-user salts and sufficient work factors.  
- **Validate certificates:** Always perform full certificate chain validation, verify hostnames, and monitor for certificate expiry or revocation.  
- **Perform regular audits:** Scan for use of deprecated functions, misconfigurations, and ensure all components adhere to current cryptographic best practices.

### 3. **A03:2021 – Injection**

**Description:**  
Injection vulnerabilities occur when untrusted input is included in commands or queries, allowing attackers to manipulate an application’s logic or execute unintended commands. By injecting malicious payloads, attackers can read, modify, or delete data, execute system commands, or bypass authentication.

**Examples:**  
- **SQL Injection:**  
  - **UNION-based:** Attacker appends `UNION SELECT` to combine results from another table.  
  - **Error-based:** Leverages database error messages to extract data.  
  - **Content-based blind:** Infers data by observing differences in responses.  
  - **Time-based blind:** Uses delays (e.g., `SLEEP()`) in SQL to deduce data bit by bit.  
- **OS Command Injection:** Invokes system commands via unsanitized input, e.g., `exec("ping " + host)` leading to `; rm -rf /`.  
- **LDAP Injection:** Manipulates LDAP queries, e.g., `ldap_search("cn=" + user + ")")`.  
- **XSS (Cross-site Scripting):**  
  - **Reflected:** Malicious script in URL is executed when reflected in response.  
  - **Stored:** Persistent script saved in database and executed by all visitors.  
  - **DOM-Based:** Client-side JavaScript writes untrusted input into the DOM.  
- **XML Injection/XXE:** Injects malicious XML entities to read local files or perform SSRF.  
- **Server-Side Template Injection:** Injects template directives, e.g., `${system.exit()}` in a templating engine.  
- **HQL/ORM Injection:** Alters ORM queries by concatenating untrusted input, e.g., `from User where name = '` + name + `'`.

**Key Characteristic:**  
All injection flaws involve string concatenation or interpolation of untrusted input into commands or queries:

```bash
data = "user: " + username
// or
data = "user:${username}"
```
**Tools:**  
- **SQLmap:** Automates detection and exploitation of SQL injection.  
- **Burp Suite Intruder:** Automates payload injection and response analysis.  
- **OWASP ZAP:** Scans for injection flaws across protocols.

**Recommendations:**  
- **Validate Input:** Use a whitelist of allowed characters/values; reject or sanitize everything else.  
- **Server-Side Enforcement:** Perform validation and sanitization on the server, not solely in the browser.  
- **Parameterized Queries:** Always use prepared statements or ORM parameter binding; never concatenate user input into queries.  
- **Escaping and Encoding:** Properly escape data in contexts where parameterization isn’t possible (e.g., HTML or XML).  
- **Least Privilege:** Limit database user permissions to only necessary operations to reduce damage if injection succeeds.  
- **Regular Testing:** Include automated injection tests in CI/CD and perform manual reviews of query-building code.

### 4. **A04:2021 – Insecure Design**

**Description:**  
Insecure Design refers to flaws introduced during the architectural or design phases that cannot be mitigated by perfect implementation alone. These issues stem from missing or inadequate security controls in the system’s blueprint and require revisiting design decisions to resolve.

**Real-world Examples:**  
- **Detailed Error Messages in Logs:**  
  An application logs full session identifiers and request details. When combined with a path traversal vulnerability, an attacker reads logs to hijack user sessions.  
- **Client-Side Only Validation:**  
  A Cisco router’s web UI validates input (e.g., ping hostnames) in JavaScript but does not enforce it on the server. By bypassing client checks via a proxy, attackers executed arbitrary OS commands.  
- **Reversible Password Storage:**  
  A desktop application uses a homegrown encryption algorithm to store user passwords. Attackers reverse-engineered the algorithm, exposing plaintext credentials for all users.  
- **Sensitive Data in GET Parameters:**  
  An e-commerce site includes user credentials in query strings (`?user=alice&token=abc123`). These appear in browser history, referer headers, and server logs, leaking sensitive data.

**Recommendations:**  
- **Integrate Security into SDLC (S-SDLC):**  
  Embed security requirements, design reviews, and code reviews at each development phase. Treat design artifacts (UML, data flows) as security checkpoints.  
- **Perform Threat Modeling Continuously:**  
  Re-evaluate attack surfaces and data flows whenever features are added or modified. Use techniques like STRIDE or PASTA to identify design-level threats.  
- **Enforce Secure Defaults:**  
  Design configurations that default to safe behavior (e.g., deny-by-default access control, input validation on server).  
- **Use Standardized Patterns:**  
  Adopt proven security patterns (e.g., Proxy pattern for SSRF, Interceptor pattern for centralized input validation) rather than ad hoc controls.  
- **Document Security Decisions:**  
  Maintain design documentation detailing chosen controls, trust boundaries, and data sensitivity classifications to guide future audits and updates.  

### 5. **A05:2021 – Security Misconfiguration**

**Description:**  
Security Misconfiguration arises when security settings are left at insecure defaults or are improperly configured in servers, frameworks, or applications. These lapses create easy entry points for attackers.

**Examples:**  
- **Lack of Hardened Services:** Unnecessary features or services enabled (e.g., open management interfaces, sample/demo pages) increase attack surface.  
- **Default Credentials & Stack Traces:** Use of default admin accounts/passwords and unfiltered error messages reveal internal paths, versions, and code snippets.  
- **Framework Misconfiguration:** Outdated or insecure framework settings (e.g., Struts, Spring Boot actuator endpoints left open, exposed debugging modules).  
- **Missing or Incorrect Security Headers:** Absence of headers like `X-Frame-Options`, `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options` allows clickjacking, XSS, and downgrade attacks.  
- **XXE (XML External Entity) Vulnerability:** XML parsers that process external entities enable SSRF or disclosure of local files.  
- **Cookie Flags Misconfigured:** Missing `HttpOnly` allows JavaScript access; missing `Secure` permits transmission over HTTP; missing `SameSite` enables CSRF via cross-site requests.

**Recommendations:**  
- **Directory & Version Disclosure Control:** Disable directory listings; hide or restrict endpoints revealing server or framework versions.  
- **Cookie Security Flags:**  
  - `HttpOnly` to prevent JavaScript access  
  - `Secure` to enforce HTTPS-only transmission  
  - `SameSite` (Lax or Strict) to mitigate CSRF  
- **Security Headers Configuration:**  
  - `Strict-Transport-Security` to enforce HTTPS  
  - `Content-Security-Policy` to restrict allowed sources  
  - `X-Frame-Options: DENY|SAMEORIGIN` to prevent clickjacking  
  - `X-Content-Type-Options: nosniff` to block MIME sniffing  
- **Disable External Entity Processing:** Configure all XML parsers to disallow DTDs and external entities (`XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES=false`).  
- **Continuous Configuration Audits:** Regularly scan environments with automated tools (e.g., CIS-CAT, security linters) and perform manual reviews of server, container, and application settings to enforce hardened, up-to-date configurations.  

### 6. **A06:2021 – Vulnerable and Outdated Components**

**Description:**  
Using outdated or vulnerable components exposes applications to known security flaws that attackers can exploit. This includes any software dependency, platform, or service not kept up to date with patches for discovered vulnerabilities.

**Components include:**  
- **Development Dependencies:** Frameworks, libraries, and SDKs used in builds (e.g., npm, Maven, NuGet packages).  
- **Operating System:** Unpatched OS kernels or system libraries on servers, containers, or endpoints.  
- **Used Libraries:** Third-party client-side or server-side libraries (e.g., jQuery, OpenSSL, Log4j).  
- **Servers and Services:** Orchestrators and infrastructure components such as Kubernetes, queue/broker systems (RabbitMQ, Kafka), databases (MySQL, MongoDB).

**Tools:**  
- **Snyk:** Automates scanning of project dependencies, container images, and infrastructure as code for known CVEs.  
- **OWASP Dependency-Check:** Identifies publicly disclosed vulnerabilities in project dependencies.  
- **Trivy:** Scans container images and filesystems for OS and application vulnerabilities.

**Recommendations:**  
- **Continuous Dependency Verification:** Integrate automated vulnerability scanning into CI/CD pipelines to detect outdated or vulnerable packages before deployment.  
- **Version Documentation:** Maintain a bill of materials (BOM) listing all dependencies and their versions; track updates and patches over time.  
- **Regular Vulnerability Monitoring:** Subscribe to CVE feeds and security advisories for all used components; prioritize patching based on severity and exploitability.  
- **Enforce Minimal Versions Policy:** Require dependencies meet a minimum secure version; fail builds if versions fall below thresholds.  
- **Isolate and Patch Host Environments:** Apply OS and container runtime updates regularly; use configuration management tools (Ansible, Puppet) to enforce baseline configurations.  

### 7. **A07:2021 – Identification and Authentication Failures**

**Description:**  
Failures in identification and authentication allow attackers to assume other users’ identities or bypass authentication mechanisms entirely. These flaws occur when applications do not properly verify user credentials or session tokens.

**Examples:**  
- **Incorrect 2FA Implementation:** Failing to enforce second factor before granting access, or reusing one-time codes.  
- **Username Enumeration:** Detailed error messages reveal whether a username exists (`"User not found"` vs. `"Incorrect password"`).  
- **Weak Password Reset:** Reset links or codes without expiration, insufficient verification, or predictable tokens allow unauthorized resets.

**Recommendations:**  
- **Strong Password Policy:** Enforce minimum length (e.g., 12+ characters), complexity rules, and ban common passwords.  
- **Generic Authentication Errors:** Use messages like `"Invalid username or password"` without specifying which field was incorrect.  
- **Secure Password Reset:** Require multi-channel verification (email link + security question or SMS code), ensure links/codes expire quickly, and invalidate on first use.  
- **Cryptographically Secure Tokens:** Generate session tokens, one-time codes, and reset tokens using CSPRNG.  
- **Secure JWT Handling:**  
  - Reject tokens with `alg: none`  
  - Use sufficiently long, high-entropy signing keys  
  - Set a reasonable token expiration time and enforce refresh policies  
- **Account Lockout & Monitoring:** Temporarily lock accounts after repeated failures and alert on suspicious login patterns.  

### 8. **A08:2021 – Software and Data Integrity Failures**

**Description:**  
Software and Data Integrity Failures occur when applications do not verify the integrity and authenticity of code, dependencies, or data. Attackers can introduce malicious artifacts at build time, run-time, or via external resources.

**Scenarios:**  
- **Unsigned Automatic Updates:** Applications auto-update executables or libraries from a server without validating digital signatures, risking supply-chain compromise.  
- **CI/CD Integrity Gaps:** Build pipelines pull dependencies or code without checksum or signature verification, allowing injection of malicious packages.  
- **Serialized Data in Cookies:** Cookies store serialized objects (e.g., Java `Serializable`) that aren’t integrity-checked, enabling arbitrary code execution when deserialized.  
- **Compromised External JS:** Loading third-party scripts (e.g., analytics) without SubResource Integrity (SRI) allows attackers controlling the host to serve malicious code (TicketMaster breach).

**Recommendations:**  
- **Integrity Verification on Install:** Use package managers’ checksum or signature features (`npm ci --verify-signatures`, Maven PGP signatures, NuGet signed packages).  
- **Avoid Native Deserialization:** Replace insecure object serialization with safer formats like JSON or protocol buffers, and validate parsed data.  
- **Secure Key Management:** Store signing keys in HSMs, vaults, or KMS services—never embed in source or container images.  
- **Use SubResource Integrity for JS:** Add `integrity` and `crossorigin` attributes to `<script>` tags to ensure remote scripts match expected hashes.  
- **Pipeline Hardening:** Implement automated checks in CI/CD to validate artifacts’ checksums, reject altered dependencies, and perform reproducible builds.  

### 9. **A09:2021 – Security Logging and Monitoring Failures**

**Description:**  
Failures in logging and monitoring prevent detection, investigation, and response to security incidents. Without detailed, trustworthy logs and active monitoring, attackers can operate unnoticed, and post-incident forensics become impossible.

**Real-world Example:**  
A web application breach where only basic HTTP access logs were available; no user identifiers, action details, or timestamps in UTC, making it impossible to trace attacker behavior or impact.

**What to Log:**  
- **When:** Exact date and time in UTC  
- **Where From:** Client IP address  
- **Who:** Authenticated user identifier or anonymized user ID  
- **What:** Detailed action performed (e.g., record accessed, settings changed)  
- **Status:** Outcome (success, failure, error codes)  
- **Level:** Severity (info, warning, error, critical)

**What NOT to Log:**  
- Session IDs or tokens  
- Plaintext passwords  
- JWT tokens or secret keys  
- Any sensitive data that could enable account takeover

**Recommendations:**  
- **Comprehensive Logging:** Instrument application and infrastructure to record all key operations following the above schema.  
- **Active Monitoring:** Implement real-time alerting and dashboards to detect anomalies (e.g., multiple failures).  
- **Centralized Log Management:** Use a dedicated logging platform (ELK, Splunk, or cloud SIEM) to collect, index, and correlate logs across services.  
- **Immutable Storage:** Configure logs in read-only or append-only mode and restrict write access to prevent tampering.  
- **Regular Backups:** Archive logs securely and test restoration procedures to ensure availability for audits and incident response.

### 10. **A10:2021 – Server-Side Request Forgery (SSRF)**
**Description:** Vulnerability allowing execution of requests to other servers from the vulnerable server under attacker's control.

**Common uses:**
- Exploiting security flaws in services within the same network,
- Bypassing access controls,
- Reading cloud metadata in cloud environments.

**Recommendations:**
- Protect against XXE (which can also enable SSRF),
- Ensure application server doesn't have access to unnecessary local network services,
- For functionality allowing user-provided URLs, use dedicated proxy servers.

## Additional recommendations and tools

**Security tools mentioned:**
- **Sonarqube:** Code analysis with OWASP TOP 10 classification
- **SQLmap:** Automated SQL injection testing
- **Snyk:** Dependency vulnerability scanning
- **Qualys SSL Labs:** SSL configuration testing

**Key practices:**
- Regular permission verification and server-side data validation
- Apply security mechanisms at the design stage (S-SDLC, threat modeling)
- Regular component updates and verification
- Implement and automate security testing
- Centralize logs and monitoring with incident detection

**Links:**
- Burp Suite Community - https://portswigger.net/burp/releases#community
- Darmowa platforma z zadaniamiami do hakowania - https://portswigger.net/web-security
- SQLmap - https://github.com/sqlmapproject/sqlmap
- Snyk - https://docs.snyk.io/developer-tools/snyk-cli
- PHPGGC - https://github.com/ambionics/phpggc
- Słownik do wyszukiwania zasobów - https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/LinuxFileList.txt
- Feroxbuster - https://github.com/epi052/feroxbuster
- Ffuf - https://github.com/ffuf/ffuf
- Sql-Injection Cheat Sheet https://portswigger.net/web-security/sql-injection/cheat-sheet
- Cross-site scripting (XSS) cheat sheet - https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
- PayloadsAllTheThings - https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection#xss-in-svg