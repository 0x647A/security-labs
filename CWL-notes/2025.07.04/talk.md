# CyberWomen Leaders – Training 3: Threats, Vulnerabilities & Attacks

## 📋 AGENDA  
1. Attackers’ Arsenal & Methods  
2. Vulnerabilities & Exploits (CVSS)  
3. Active Defense & Analysis (Indicators of Compromise, CTI, SOC Tools)  

## MODULE 1: ATTACKERS’ ARSENAL & METHODS

### Threat Actors  
**Definition:** A threat actor is an individual or group executing attacks. Understanding motivations—financial gain, espionage, ideology, revenge—helps anticipate techniques and choose defenses.  
- **Nation-state APTs** leverage vast resources, zero-day exploits, and stealthy lateral movement to steal intellectual property or disrupt critical infrastructure.  
- **Organized crime syndicates** operate like businesses, deploying ransomware affiliates, encrypting victims’ data, and demanding cryptocurrency ransoms, then laundering proceeds via money mules or mixers.  
- **Hacktivists** pursue political or social agendas, often using DDoS campaigns to shut down websites or leaking sensitive information to embarrass targets.  
- **Insider threats** arise when employees or contractors abuse legitimate access—maliciously or accidentally—through data exfiltration, sabotage, or falling victim to phishing.

### Malware Families  
Malware encompasses any software designed to harm or exploit. Precise classification enables tailored detection and response.  
- **Viruses** attach to host files and require user execution; they corrupt data, disable security, or propagate via email attachments.  
- **Worms** self-propagate across networks by exploiting remote code-execution flaws; they can spawn global botnets or deliver payloads like ransomware.  
- **Trojans & RATs** masquerade as benign applications; once installed, Remote Access Trojans grant full attacker control—keylogging, screen capture, file manipulation, and pivoting to other systems.  
- **Ransomware** typically employs phishing or RDP exploits to install encryption payloads. In “double extortion,” attackers first exfiltrate sensitive data, then encrypt files and threaten data publication if the ransom is not paid.  
- **Spyware & Keyloggers** stealthily record keystrokes, screenshots, and browser history, then transmit credentials and personal data to command servers.  
- **Rootkits** hide in user-mode or kernel-mode, intercepting system calls to cloak malicious processes and files, making detection difficult.  
- **Fileless malware** lives entirely in memory, abusing built-in tools like PowerShell or WMI; no disk artifacts complicate forensic analysis, so behavioral EDR solutions are essential.  
- **Cryptominers** covertly harness CPU/GPU cycles for cryptocurrency mining; sudden CPU spikes, system slowdowns, and overheating fans are tell-tale indicators.

### Cyber Kill Chain  
Lockheed Martin’s model breaks an advanced attack into seven sequential phases. Each phase offers defenders a chance to detect and disrupt adversary operations:  
1. **Reconnaissance:** Passive or active information gathering.  
2. **Weaponization:** Pairing exploit code with a backdoor payload.  
3. **Delivery:** Transmitting the payload via email, web, removable media, or network.  
4. **Exploitation:** Triggering the exploit to execute code.  
5. **Installation:** Dropping and persisting malware on the host.  
6. **Command & Control:** Establishing channels for remote commands.  
7. **Actions on Objectives:** Data theft, sabotage, or lateral movement.  

By mapping alerts, logs, and endpoint telemetry against this chain, security teams can identify activity at each stage and tailor controls accordingly.

#### Attack Types & Descriptions  
- **DDoS (Distributed Denial-of-Service)**  
  Floods target with traffic to disrupt service.  

- **Man-in-the-Middle (MITM)**  
  Intercepts and optionally alters communications between two parties.  

- **SQL Injection (SQLi)**  
  Injects malicious SQL into web forms to read or modify database.  

- **Cross-Site Scripting (XSS)**  
  Injects malicious scripts into web pages viewed by other users.  

- **Directory Traversal**  
  Accesses files/directories outside intended web root.  

- **Brute-Force & Dictionary Attacks**  
  Attempts many password guesses or a list of common passwords.  

- **Password Spraying**  
  Tries one common password against many accounts to avoid lockout.  

- **Credential Stuffing**  
  Uses breached username/password pairs against multiple sites.  

#### Rootkits – Definition & Types  
- **Rootkit**: malware designed to hide itself or other malware, maintain highest privileges.  
- **User-Mode Rootkits**  
  - Operate at application level, hook API calls, easier detection by kernel-level monitoring.  
- **Kernel-Mode Rootkits**  
  - Run in OS kernel, modify core OS structures, extremely difficult to detect or remove. 

---

## MODULE 2: VULNERABILITIES & EXPLOITS

### Technical vs. Human Vulnerabilities  
- **Technical Vulnerabilities** arise from coding errors, misconfigurations, unpatched libraries, or flawed network protocols. Automated vulnerability scanners and patch-management processes help identify and remediate these weaknesses before attackers exploit them.  
- **Human Vulnerabilities** stem from cognitive biases and lack of security awareness—phishing emails, social engineering calls, or misplaced trust. Regular security awareness training and phishing simulations reduce the likelihood of employees clicking malicious links or divulging credentials.

### CVE & CVSS Standards  
The Common Vulnerabilities and Exposures (CVE) system assigns unique identifiers to public vulnerabilities (e.g., CVE-2025-53770), ensuring consistent communication across vendors and researchers. The Common Vulnerability Scoring System (CVSS) then quantifies severity on a 0.0–10.0 scale using base metrics:  
- **Attack Vector (AV):** Network, adjacent network, local, physical  
- **Attack Complexity (AC):** Low or High  
- **Privileges Required (PR):** None, Low, High  
- **User Interaction (UI):** None or Required  
- **Scope (S):** Unchanged or Changed  
- **Impact (C/I/A):** None, Low, High  

Temporal metrics adjust for exploit maturity and remediation availability; environmental metrics further refine scores based on asset criticality and existing compensating controls, allowing tailored prioritization of patching efforts.

---

## MODULE 3: ACTIVE DEFENSE & ANALYSIS

### Incident Response Lifecycle  
1. **Preparation:** Establish IR team, define policies, deploy detection tools, and conduct tabletop exercises.  
2. **Detection & Analysis:** Correlate SIEM alerts with endpoint telemetry; classify incidents by severity and scope.  
3. **Containment:** Segment or block compromised hosts to prevent lateral spread; apply network ACLs or quarantine endpoints.  
4. **Eradication:** Remove malware, disable backdoors, apply patches, and close exploited vulnerabilities.  
5. **Recovery:** Restore systems from clean backups, validate integrity, and return to business operations.  
6. **Lessons Learned:** Conduct post-incident reviews to refine detection rules, update playbooks, and strengthen defenses.

### IoCs vs. TTPs  
- **Indicators of Compromise (IoCs):** Retrospective artifacts—malicious file hashes, C2 server IPs, registry keys—used to detect known threats in logs and endpoints. IoCs must be updated continuously as adversaries rotate their infrastructure.  
- **Tactics, Techniques & Procedures (TTPs):** Proactive patterns—such as spear-phishing to gain initial access or living-off-the-land usage of PowerShell—to anticipate attacker behavior. Mapping observed activity to MITRE ATT&CK® tactics and techniques enables threat hunting and control hardening.

### Cyber Threat Intelligence (CTI)  
CTI transforms raw IoCs and threat feeds into three actionable levels:  
- **Strategic CTI** for executives: market-wide threat trends, threat actor targeting patterns, industry-specific risks.  
- **Operational CTI** for managers: active campaigns, specific TTPs in play, and resource allocation for threat mitigation.  
- **Tactical CTI** for analysts: curated IoC lists, playbooks for incident response, and automated ingestion via STIX/TAXII.

### SOC Tools & Capabilities  
- **SIEM** aggregates and normalizes logs from firewalls, servers, applications, and cloud platforms; applies correlation rules (e.g., impossible travel: login from two distant locations within minutes) to generate prioritized alerts and dashboards.  
- **SOAR** integrates with SIEM and endpoint tools to orchestrate automated workflows (playbooks) that triage alerts, query threat intelligence, isolate infected hosts, and notify analysts—all with audit trails.  
- **EDR/XDR** continuously monitors endpoint processes, network connections, and file changes; allows remote investigation, live response actions, and retrospective threat hunting. XDR extends detection across email, network, and cloud workloads for holistic visibility.  
- **Sandboxing** runs suspect files in isolated virtual environments, observing behaviors—network calls to malicious domains, suspicious registry writes, process injection—to classify samples without risking production assets.  
- **NGFW & WAF** enforce next-generation firewall policies at layers 4–7, understanding application context, decrypting SSL/TLS, blocking known bad IPs and signatures, and shielding web applications from injection and scripting attacks.

---

## 🔑 EXAM FOCUS AREAS  
- **Threat Actors & Motivations** (Domain 2.1): Compare nation-state APTs, organized crime, hacktivists, insider threat.  
- **Malware Types & Delivery** (Domain 2.4): Define and contrast viruses, worms, trojans, ransomware, spyware, keyloggers, rootkits, fileless malware, cryptominers.  
- **Vulnerability Management** (Domain 4.3): Explain CVE enumeration, CVSS scoring, and patch prioritization.  
- **Social Engineering Vectors** (Domain 2.2): Distinguish phishing, spear phishing, whaling, vishing, smishing, business email compromise, homograph attacks, typosquatting.  
- **Attack Vectors & Web Flaws** (Domain 2.3): Identify unsecure networks, open ports, removable media, SQLi, XSS, directory traversal.  
- **Indicators vs. Behaviors** (Domain 2.4): Use IoCs for detection and TTP mapping for threat hunting with MITRE ATT&CK.  
- **Incident Response & CTI** (Domains 4.8–4.9): Know IR phases, data sources (firewall, application, endpoint, network logs), CTI levels, STIX/TAXII fundamentals.  
- **SOC Technologies** (Domains 4.4–4.7, 3.2, 4.5): Understand SIEM, SOAR playbooks, EDR/XDR capabilities, sandbox analysis, NGFW vs. WAF roles.
