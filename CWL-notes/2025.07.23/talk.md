# CyberWomen Leaders – Training 5: Identity and Access Management (IAM)

## 1. IAM Fundamentals and the AAA Model

### 1.1 Definition of IAM  
**Identity and Access Management** (IAM) is the discipline of managing digital identities—whether they belong to human users, applications, or devices—and controlling their access to an organization’s resources. A robust IAM framework ensures that:  
- **Only trusted identities** (employees, partners, service accounts, IoT devices) are granted any access.  
- **Access rights** are precisely tailored so each identity can reach exactly the systems, applications, or data it needs—and nothing more.  
- **Access is delivered at the right moment**, for example granting temporary elevated privileges only when a specific task is underway.  

An effective IAM solution includes:  
- **Account Registration and Lifecycle**  
  - Automated onboarding: creating accounts and baseline permissions when a new identity is added (e.g., new hire, new service).  
  - Ongoing management: updating attributes like department or role as identities change over time.  
  - Deprovisioning: immediately revoking all access when an identity leaves or is retired to eliminate orphaned accounts.  
- **Authentication (Verifying Identity)**  
  - Ensuring the user or system presenting credentials is who—or what—it claims to be.  
  - Techniques range from simple passwords to multi-factor methods (SMS codes, hardware tokens, biometrics, or modern passwordless standards like FIDO2).  
- **Authorization (Assigning Permissions)**  
  - Determining “what can this identity do?” after authentication.  
  - Policies may be role-based (RBAC), attribute-based (ABAC), or policy-driven, enforcing the principle of least privilege.  
- **Auditing and Logging**  
  - Capturing every significant action: successful and failed logins, privilege elevations, resource changes.  
  - Providing a trail for troubleshooting, forensic investigation, and proving compliance with regulations (e.g., GDPR, PCI DSS).

### 1.2 The AAA Model  
The AAA model is the cornerstone of most IAM implementations, comprising three sequential steps:

1. **Authentication** – Confirming “Who are you?”  
   - Before any access is granted, the system must validate that the presented credentials genuinely belong to the claimed identity.  
   - Common methods:  
     - **Something you know**: passwords, PINs, or passphrases.  
     - **Something you have**: one-time password tokens, hardware keys (YubiKey), or mobile push notifications.  
     - **Something you are**: biometric factors like fingerprint or facial recognition.  
     - **Emerging factors**: device posture checks, geolocation constraints, or behavioral analytics.

2. **Authorization** – Deciding “What can you do?”  
   - Once the identity is authenticated, the system checks policies to determine which resources and operations the identity is permitted.  
   - Policies may leverage:  
     - **Roles and groups** (e.g., “Finance,” “HR,” “DevOps”) to assign broad permission sets.  
     - **Attributes** (e.g., job title, department, project membership) for finer-grained control.  
     - **Contextual conditions** (e.g., time of day, network location, device security posture) under zero-trust frameworks.

3. **Accounting** – Recording “What did you do?”  
   - Every authenticated and authorized action is logged for later review.  
   - Typical audit data includes: timestamps of logins/logouts, resources accessed, commands executed, and changes made.  
   - These records are essential for:  
     - **Incident analysis**: reconstructing attack paths or misuse.  
     - **Forensic investigations**: identifying insider threats or compromised accounts.  
     - **Compliance reporting**: demonstrating adherence to regulatory requirements with detailed usage logs.

By combining these three pillars—Authentication, Authorization, and Accounting—organizations can build a coherent, end-to-end IAM strategy that both secures resources and provides the visibility needed for effective governance and compliance.```

#### 1.3 RADIUS vs. TACACS+
|              | RADIUS                        | TACACS+                     |
|--------------|-------------------------------|-----------------------------|
| Transport    | UDP (connectionless)          | TCP (connection-oriented)   |
| Ports        | 1812 (Auth/Authz), 1813 (Acct)| 49                          |
| Encryption   | Password only in Access-Request | Entire packet             |
| AAA Separation | Auth + Authz combined       | Auth, Authz, Acct separated |
| Use Case     | Network access (VPN, 802.1X)  | Network device administration |

## 2. User Lifecycle Management (ULM)

### 2.1 Account Lifecycle Stages  
1. **Onboarding**  
   - Triggered by HR event (new hire, contractor start).  
   - Automatically create user account in directory (e.g., Active Directory or LDAP).  
   - Populate user profile with attributes (name, department, manager).  
   - Assign baseline roles or groups based on job function (e.g., “Sales,” “IT Staff”).  
   - Send welcome email with initial credentials and login instructions.  

2. **Provisioning**  
   - Upon role assignment, automatically grant access to required systems:  
     - Create e-mail mailbox and collaboration tools license.  
     - Provision access to file shares, applications, VPN.  
     - Issue hardware tokens, certificates, or MFA enrollment.  
   - Track all grants in IAM system to ensure visibility and reversibility.  

3. **Maintenance**  
   - When an employee changes position or project:  
     - Update group memberships or role assignments in central directory.  
     - Add new privileges for new responsibilities; remove old ones no longer needed.  
   - Handle temporary access requests (e.g., emergency admin rights) via Just-In-Time workflows.  
   - Maintain accurate attribute data (location, cost center) to drive dynamic policies.  

4. **Deprovisioning**  
   - Immediately upon termination or contract end:  
     - Disable account in directory to block logins.  
     - Revoke all active sessions and tokens (MFA, SSH keys).  
     - Remove access to cloud subscriptions, SaaS applications, privileged vaults.  
   - Ensure any shared or departmental accounts are cleaned up to prevent orphans.  

5. **Retirement**  
   - After a safe retention period (for audit/compliance):  
     - Convert account to read-only or archival mode.  
     - Export and securely store audit logs, historical entitlements.  
     - Delete or anonymize personal data to comply with privacy regulations (e.g., GDPR “right to erasure”).  

### 2.2 Key Principles  
- **Automation**  
  - Integrate IAM platform with HR or ERP system as authoritative source of record.  
  - Leverage workflows and APIs to eliminate manual request tickets and reduce misconfigurations.  
  - Automate lifecycle events (onboarding, role changes, offboarding) to minimize human error and accelerate access delivery.  

- **Centralization**  
  - Maintain a single, unified directory of all identities and groups.  
  - Use Single Sign-On (SSO) to grant access to multiple applications with one set of credentials.  
  - Centralize policy definition and enforcement to maintain consistency and simplify auditing.  

- **Least Privilege**  
  - Default new accounts to minimal access required for core tasks.  
  - Require explicit approval for any elevation beyond baseline roles.  
  - Use role reviews and just-in-time privilege elevation to limit the duration of high-risk permissions.  

- **Regular Audits**  
  - Schedule quarterly or event-driven reviews of all roles, group memberships, and system accesses.  
  - Identify and remove stale or unused accounts (e.g., dormant service accounts).  
  - Validate that privilege assignments still align with current job responsibilities.  
  - Document findings and remediation actions to demonstrate compliance to auditors.  

## 3. Access Control Models

### 3.1 Discretionary Access Control (DAC)  
Under DAC, each resource—file, folder, database object—is owned by a user or application. The owner directly grants and revokes permissions (read, write, execute) to other identities, typically via Access Control Lists (ACLs).  
- **Pros:** Owners can tailor access rights quickly for collaborators; easy to implement in small or informal environments.  
- **Cons:** As the number of resources and users grows, scattered ACLs become hard to track and audit; inadvertent “open to all” grants can introduce security gaps.  

### 3.2 Mandatory Access Control (MAC)  
In MAC, the operating system or security kernel enforces access decisions based on preassigned labels (e.g., “Top Secret,” “Confidential”) attached to both subjects (users/processes) and objects (files, devices). Owners cannot override or alter these labels.  
- **Use Cases:** Government, military, and intelligence systems where strict separation of classified data is required.  
- **Benefit:** Centralized, non-bypassable enforcement ensures that no user—even with administrative privileges—can subvert the security policy.  

### 3.3 Role-Based Access Control (RBAC)  
RBAC assigns permissions to roles (e.g., “HR Manager,” “Developer,” “Auditor”) rather than to individual users. Users inherit the combined permissions of all roles they hold.  
- **Simplicity at Scale:** Onboarding or removing a user simply involves assigning or revoking roles, automatically adjusting their access everywhere.  
- **Consistency:** Roles reflect business functions, aligning IT controls with organizational structure and reducing the risk of excessive individual privileges.  

### 3.4 Attribute-Based Access Control (ABAC)  
ABAC evaluates policies in real time by examining attributes of the user (department, clearance level), the resource (data classification, owner), and the environment (time of day, device health, network location).  
- **Granularity:** Enables highly contextual rules—for example, allowing a pediatrician read-only access to records from inside the hospital network during standard clinic hours.  
- **Zero Trust Foundation:** By continuously assessing context and risk, ABAC supports dynamic, just-in-time access decisions essential for modern cloud and hybrid infrastructures.  

## 4. Authentication Techniques – Passwords, 2FA, MFA

### 4.1 Password Weaknesses  
- **Phishing:** Users can be tricked into entering credentials on fake sites, handing attackers direct access.  
- **Brute-force and credential stuffing:** Automated tools can guess common or leaked passwords, especially when reuse across services occurs.  
- **Keyloggers and malware:** Malicious software on endpoints can capture keystrokes or steal password files directly.  
- **Reuse and breaches:** When one site is compromised, reused passwords expose multiple accounts.  
- **Fundamental flaw:** No matter the complexity, any password can eventually be cracked or intercepted; passwords alone offer insufficient security.  

### 4.2 2FA vs. MFA  
- **Two-Factor Authentication (2FA):** Requires exactly two distinct factors (something you know + something you have), such as a password plus an SMS one-time code.  
- **Multi-Factor Authentication (MFA):** Extends beyond two factors; for example, password + hardware token + biometric scan, or password + fingerprint + geolocation. MFA allows more flexible, stronger combinations.  

### 4.3 Factor Categories  
1. **Something you know:** Passwords, PINs, or answers to security questions—prone to being forgotten or phished.  
2. **Something you have:** Physical devices such as hardware tokens (YubiKey), mobile authenticator apps, or smartcards—resistant to remote compromise but can be lost or stolen.  
3. **Something you are:** Biometric identifiers like fingerprints, facial recognition, or iris scans—unique but raise privacy and spoofing concerns.  
4. **Somewhere you are:** Geolocation or network-based checks (IP address, Wi-Fi SSID, GPS coordinates) used as contextual factors to detect anomalous access attempts.  
5. **Something you do:** Behavioral analytics such as typing rhythms, mouse movement patterns, or habitual login times—continually profiled by AI/ML for ongoing risk assessment.  

### 4.4 Resistance Hierarchy  
1. **Hardware security keys (FIDO2/U2F):** Gold standard—phishing-resistant cryptographic challenge-response bound to specific domains.  
2. **Push notifications with context:** Mobile app prompts displaying login details and location; more secure than simple codes but vulnerable to “push fatigue” attacks.  
3. **TOTP codes (authenticator apps):** Time-based one-time passwords generated offline; secure against interception but still susceptible to phishing if codes are entered on fake sites.  
4. **SMS codes:** Least secure; susceptible to SIM swap attacks, SMS interception, and social engineering at the carrier level.  

## 5. Passwordless Future – FIDO2 and WebAuthn

### 5.1 FIDO2 Components  
- **WebAuthn:** A W3C-standardized JavaScript API built into modern browsers. It allows web applications to register and authenticate users by performing cryptographic public-key operations instead of passwords. During registration, the browser generates a key pair and sends only the public key to the server; during login, the server issues a challenge that the browser signs with the private key.  
- **CTAP (Client To Authenticator Protocol):** Defines how browsers or operating systems communicate with external or built-in authenticators (security keys, smartphones, platform TPMs) over USB, NFC, or Bluetooth. CTAP ensures the authenticator can handle requests to create new credentials and sign authentication challenges.  

### 5.2 Advantages  
- **Phishing-resistant:** Each key pair is scoped to a specific origin (domain). A credential registered for example.com cannot be used on attacker.com.  
- **No passwords on servers:** Only public keys are stored; leaked server data cannot be used by attackers to impersonate users.  
- **Frictionless, fast login:** Users authenticate by touching a security key, scanning their fingerprint or face, or inserting a USB/NFC device—streamlining the process and removing the need to remember complex passwords.  

## 6. Identity Federation and SSO

### 6.1 Actors
- **Identity Provider (IdP):** Authenticates users and issues tokens  
- **Service Provider (SP):** Trusts IdP, does not store passwords  

### 6.2 Protocols
- **SAML 2.0:** XML assertions for enterprise SSO  
- **OAuth 2.0:** API authorization with access tokens  
- **OpenID Connect:** Authentication on top of OAuth2 with ID tokens (JWT)  

## 7. Privileged Access Management (PAM)

### 7.1 Goal
Secure access to privileged accounts (admins, service accounts)

### 7.2 PAM Pillars  
1. **Vaulting:** A centrally managed, strongly encrypted credential repository that stores all privileged credentials. The PAM system injects credentials into target systems on behalf of users or applications, and automatically rotates passwords or keys after each use to eliminate reuse risks.  
2. **Session Isolation:** All privileged sessions (RDP, SSH, database consoles) are brokered through a hardened bastion host or jump server. The PAM solution records video and command-level logs of each session, ensuring full auditability and preventing direct network access to critical systems.  
3. **Zero Standing Privileges / Just-In-Time (JIT):** Users and service accounts possess no permanent elevated rights. Privileges are granted dynamically for specific tasks or time windows based on an access request workflow, then automatically revoked when the task completes—minimizing the attack surface and enforcing least privilege at runtime.  

## 8. Zero Trust Architecture (ZTA)

### 8.1 Core Principle
“Never trust, always verify” – treat every access attempt as untrusted

### 8.2 Key Tenets of Zero Trust Architecture  
1. **Universal Resource Protection:** Apply the same strict access controls to every resource—on-premises, cloud, and IoT—without implicit trust based on network location.  
2. **Encrypted & Segmented Communications:** Encrypt all traffic end-to-end and enforce micro-segmentation to limit lateral movement; use VLANs, zero-trust network access (ZTNA), and service mesh.  
3. **Dynamic Contextual Policies:** Make access decisions per request using real-time attributes—user identity, device posture, geolocation, time of day, and risk signals—via ABAC/PBAC.  
4. **Continuous Monitoring & Analytics:** Collect telemetry from endpoints, network flows, and access logs; apply real-time behavioral analysis and anomaly detection to identify threats.  
5. **MFA Everywhere:** Require multi-factor authentication for all access—users, applications, APIs—ensuring at least two distinct factors for every session.  
6. **Automated Response & Orchestration:** Integrate security tools (SIEM, SOAR, endpoint detection) to automate threat containment, remediation workflows, and policy enforcement.  
7. **Full Visibility & Audit Trails:** Maintain comprehensive, tamper-evident logging of every access attempt, configuration change, and incident response action for forensic and compliance needs.  

## 9. Compliance

### 9.1 GDPR  
- **Data Minimization & Access Limiting:** Only collect and store identity attributes strictly necessary for each business purpose. Implement role-based or attribute-based policies to ensure users and applications access only the data they need.  
- **Right to Erasure (“Right to be Forgotten”):** When a user’s personal data must be deleted or anonymized—such as upon account closure or request—automatically deprovision their account, remove or mask personal attributes, and revoke all access.  
- **Auditable Logs:** Maintain detailed, tamper-evident logs of all IAM events (provisioning, authentication, MFA prompts, access grants/revocations). Ensure logs capture user identifiers, timestamps, actions performed, and source context to support GDPR compliance and breach investigations.  

### 9.2 PCI DSS  
- **Protect Cardholder Data:** Encrypt Primary Account Numbers (PAN), CVV2, and other sensitive data in storage and transit. Use strong cryptographic algorithms and key management practices so that stolen data remains unusable.  
- **Network Segmentation & Firewalls:** Isolate payment card environments from the rest of the corporate network using dedicated VLANs or physical separation. Deploy stateful firewalls and intrusion detection/prevention systems at all ingress and egress points.  
- **Least-Privilege Access Control:** Grant administrators and applications only the minimal rights required to process, store, or transmit cardholder data. Implement unique user IDs, multi-factor authentication, and time-limited service accounts.  
- **Continuous Monitoring & Penetration Testing:** Collect and review logs of all access to cardholder data and critical systems. Perform quarterly vulnerability scans by an Approved Scanning Vendor (ASV) and annual penetration tests to identify and remediate security gaps.  
- **Security Policies & Staff Training:** Maintain documented security policies covering data handling, incident response, and change management. Provide regular PCI-specific training for all personnel with access to cardholder data to ensure awareness of threats and best practices.  
