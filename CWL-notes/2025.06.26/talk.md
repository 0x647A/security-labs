# CyberWomen Leaders – Training 1: Introduction to Information Security

## Fundamental Truth of Cybersecurity

**IT systems are much easier to attack than to defend** - this is the basic assumption that drives the entire cybersecurity industry. According to the latest statistics for 2025:

- **72%** of organizations noted increased cyber risk
- **10.5 trillion USD** - predicted cost of cybercrime by 2025
- **Over 2,200** cyberattacks daily worldwide
- **258 days** - average time to detect and contain a data breach

## Definitions and Differences of Key Concepts

### Information Security
A comprehensive set of practices aimed at protecting data, systems and resources from:
- Unauthorized access
- Exploitation  
- Disclosure
- Disruption
- Modification
- Destruction

It includes strategies, processes and technological tools at **all stages of information existence** - from creation, through processing and storage, to secure disposal.

### Cybersecurity vs Information Security

| Aspect | Information Security | Cybersecurity |
|--------|---------------------|---------------|
| **Scope** | All information (digital + paper) | Digital systems only |
| **Focus** | Data protection regardless of medium | Protection of networks and IT systems |
| **Approach** | Holistic | Technological |

## Regulatory Frameworks and Standards

### Key frameworks:
- **NIST Cybersecurity Framework (CSF)** - https://www.nist.gov/cyberframework
  - Identify (IDENTIFY)
  - Protect (PROTECT) 
  - Detect (DETECT)
  - Respond (RESPOND)
  - Recover (RECOVER)

- **ISO27001:2022** - international information security management standard
- **GDPR** - General Data Protection Regulation in the EU

### Regulatory Trends for 2025
According to the World Economic Forum, cybersecurity will remain a persistent problem in 2025, with continuous threats to technological systems, especially in financial sectors and communication infrastructure.

## Information Security Goals - Extended Triad

### Classic CIA Triad:
1. **Confidentiality** - ensuring information is available only to authorized persons
2. **Integrity** - protection against unauthorized data modification  
3. **Availability** - ensuring access to information when needed

### Extended Goals:
4. **Authenticity** - verification of user and data source identity
5. **Non-repudiation** - inability to deny performing an action

### Contemporary Challenges to CIA Triad
In 2025, the biggest threats are:
- **47%** of organizations indicate threats related to generative AI
- **66%** of organizations expect the greatest AI impact on cybersecurity
- Only **37%** have processes for assessing AI tool security before implementation

## Access Control - Detailed Analysis

### Access Control Models:

#### 1. DAC (Discretionary Access Control)
- **Resource owner** decides on permissions
- Flexible but potentially dangerous
- Example: file permissions in Windows

#### 2. MAC (Mandatory Access Control) 
- **System centrally** defines access policies
- Based on security classifications
- Used in military/government environments

#### 3. RBAC (Role-Based Access Control)
- Permissions assigned based on **organizational role**
- Most popular in enterprises
- Easier management with large numbers of users

### Security Control Categories:

#### Technical Controls:
- **Firewalls** - network traffic filtering
- **IDS/IPS** - intrusion detection/prevention systems
- **Encryption** - protection of data at rest and in transit
- **2FA/MFA** - multi-factor authentication

#### Administrative Controls:
- **Policies and procedures** - formal security guidelines
- **Employee training** - building security awareness  
- **Risk assessments** - threat identification and prioritization
- **DFIR** (Digital Forensics and Incident Response) - incident response

#### Physical Controls:
- **Facility access control** - cards, biometrics
- **CCTV** - visual monitoring
- **Locks and barriers** - physical security
- **Physical security** - security personnel

### Control Functions by Time of Action:

#### Preventive [PREVENT]
- Prevent incidents **before occurrence**
- Examples: training, policies, technical barriers
- Most cost-effective

#### Detective [IDENTIFY]  
- Identify incidents **during occurrence**
- Examples: monitoring, IDS, log analysis
- Critical for rapid response

#### Corrective [RESPONSE]
- Repair damage **after incident**
- Examples: backups, recovery plans, procedures
- Minimize losses

## Cybersecurity Threats - 2025 Analysis

### Threat Sources by Statistics:

#### External (72% risk increase):
- **Professional cybercriminals** - organized groups
- **APT Groups** (Advanced Persistent Threat) - state-sponsored attacks
- **Competition** - industrial espionage  
- **Bots and automation** - automated attacks

#### Internal (48% of organizations experience):
- **Human errors** - accidental violations
- **Employees** - malicious insider actions
- **Environment** - failures, natural disasters
- **Negligence** - non-compliance with procedures

### Types of Threats from 2025 Perspective:

#### 1. Ransomware - Still the King of Threats
- **45%** of organizations indicate ransomware as the main threat
- **81%** increase in attacks year-over-year (2023-2024)
- Evolution toward **Ransomware-as-a-Service (RaaS)**

**How RaaS Works:**
- **Operators** create ransomware software
- **Affiliates** pay for access (20-30% for operator, 70-80% for affiliate)
- Business models: subscription, one-time payment, profit sharing
- Example groups: LockBit, BlackCat (ALPHV), Clop

#### 2. AI-Enhanced Threats - New Era of Threats
**Generative AI in Cybercriminals' Hands:**
- **5 minutes** - time needed for AI to create effective phishing (vs 16 hours for experts)
- **42%** of organizations experienced successful social engineering attacks
- **550%** increase in deepfakes from 2019-2023
- **8 million** deepfakes predicted in 2025

#### 3. Zero-day Vulnerabilities - Record Year 2025
- **Over 30** zero-days in Q1 2025
- **90** zero-days disclosed in all of 2024
- **41%** of CVEs added to KEV (Known Exploited Vulnerabilities) catalog are zero-days
- Examples: CVE-2025-53770 (SharePoint), CVE-2025-6558 (Chrome)

#### 4. Supply Chain Attacks
- **45%** of global organizations will have supply chain problems by 2025
- Attacks on software and service providers
- Domino effect - one compromised supplier = thousands of victims

## Contemporary Attack Techniques - Presentation Demonstrations

### Password Profiling - Case Study
The presented example of a password generation profile shows how attackers use OSINT information:

**Example Profile:**
- Name: John Doe  
- Gender: Male
- Organization: Sigma
- Birthdate: 06/09/1337
- Job: ITsec expert
- Hobbies: Photography, gym, motorcycles
- Movies: Star Wars, Jaws
- Pet: Dog "dog"
- Car: Ford Mustang GTR "Eleanor"

**Potential Passwords:**
- `Sigma2025!`
- `StarWars1337`  
- `Photography@Gym`
- `EleanorMustang06`
- `DogLover1337!`

### Breach Checking Tools:
- **haveibeenpwned.com** - check if email was in a breach
- **dehashed.com** - search for data in breaches
- Example from presentation: `barbara.makowka1111@onet.eu:marchewka!`

### Technical Reconnaissance - Shodan Dorks:

```bash
webcam has_screenshot:yes
camera country:pl has_screenshot:yes
"SERVER: EPSON_Linux UPnP" "200 OK"
```


**Additional Reconnaissance Resources:**
- https://insecam.org - unsecured cameras
- https://viz.greynoise.io/ - internet scanning
- https://search.censys.io/ - IoT device search engine
- https://www.zoomeye.ai - Chinese Shodan equivalent

### Contemporary Threats in Practice:

#### Deepfakes and Media Manipulation
- **Face Swap Technique:** https://aifaceswap.io/
- **Document Deepfakes** - KYC (Know Your Customer) bypass
- **Fake News** - public opinion manipulation

#### QR Code Attacks
- **New Attack Vectors** - malicious QR codes in public places
- **Particular Vulnerability of Children** - lower threat awareness
- **Phishing Redirects** - seemingly legitimate codes

#### Hardware Attacks
- **USB Ninja** - hidden keyloggers in USB cables
- **Flipper Zero** - universal tool for RF, NFC, infrared attacks
- **Keyboard Emulation** - HID device emulation capability

## Defense - Best Practices 2025

### Password Management - New Approach

#### Expert Recommendations for 2025:
**Length > Complexity:**
- Minimum **15+ characters**
- **4+ relatively random words** instead of complex symbols
- Example: `thispasswordyouwillneverforget` vs `uAy6*m;+fUkD=xGj}Jsf`

#### Password Managers - Business Benefits:

**Security:**
- **Unique passwords** for each account
- **Protection against credential stuffing**
- **Automatic generation** of strong passwords
- **Encryption** locally or in cloud

**Productivity:**
- **Autofill** - automatic completion
- **Synchronization** between devices  
- **Single Sign-On** - integration capabilities
- **Centralized access** management

**Compliance and Audit:**
- **Audit trails** - who, when, what
- **Password policies** - standard enforcement
- **Secure sharing** - controlled sharing
- **Dark Web monitoring** - breach alerts

#### Recommended Solutions:
- **KeePass** - https://keepass.info/ (open source, local)
- **Bitwarden** - https://bitwarden.com/ (freemium, cloud)
- **Built into systems** - Apple Keychain, Google Password Manager

### Multi-Factor Authentication (MFA/2FA)

#### Types of Authentication Factors:
1. **Something you know** (Knowledge) - password, PIN
2. **Something you have** (Possession) - phone, token
3. **Something you are** (Inherence) - biometrics

#### Recommended MFA Solutions:
- **Microsoft Authenticator** - mobile app with push notifications
- **YubiKey** - https://www.yubico.com/products/ - U2F/FIDO2 hardware keys
- **Google Authenticator** - TOTP (Time-based One-Time Password)
- **SMS** - **NOT RECOMMENDED** due to SIM swapping

#### Attacks on 2FA - Threat Awareness:

**Popular Bypass Techniques:**
1. **Password Reset** - bypassing 2FA through password reset
2. **Social Engineering** - obtaining codes via phone/email  
3. **SIM Swapping** - phone number takeover
4. **MFA Prompt Bombing** - push notification bombardment
5. **Adversary-in-the-Middle** - reverse proxy intercepting sessions
6. **Session Cookie Theft** - authentication cookie theft

**Advanced Technique Examples:**
- **Response Manipulation** - changing `success: false` to `success: true`
- **Status Code Manipulation** - changing HTTP error codes
- **CSRF on 2FA disable** - cross-site request forgery
- **Path Traversal** - `1234/../../../../` in 2FA code

## Frameworks and Threat Models

### MITRE ATT&CK Framework - Detailed Analysis

**ATT&CK** = **A**dversarial **T**actics, **T**echniques & Common **K**nowledge

#### 14 Tactics in Enterprise Matrix:

| ID | Tactic | Attacker Goal |
|---|---------|---------------|
| TA0043 | **Reconnaissance** | Gather data for planning |
| TA0042 | **Resource Development** | Identify resources for attacks |
| TA0001 | **Initial Access** | First entry into network |
| TA0002 | **Execution** | Run malicious code |
| TA0003 | **Persistence** | Maintain position |
| TA0004 | **Privilege Escalation** | Gain higher privileges |
| TA0005 | **Defense Evasion** | Bypass security |
| TA0006 | **Credential Access** | Obtain login credentials |
| TA0007 | **Discovery** | Environment reconnaissance |
| TA0008 | **Lateral Movement** | Move within network |
| TA0009 | **Collection** | Gather data |
| TA0011 | **Command and Control** | Communication with attacker |
| TA0010 | **Exfiltration** | Steal collected data |
| TA0040 | **Impact** | Destroy/disrupt operations |

#### Practical ATT&CK Applications:
- **Red Teams** - attack simulation
- **Blue Teams** - detection and response
- **Threat Intelligence** - threat classification
- **Security Tools** - SIEM/XDR tool configuration

### Cyber Kill Chain - Attack Stage Analysis

**Classic Lockheed Martin Model:**
1. **Reconnaissance** - target information gathering
2. **Weaponization** - exploit/malware preparation
3. **Delivery** - payload transmission (email, USB, etc.)
4. **Exploitation** - vulnerability exploitation
5. **Installation** - backdoor installation
6. **Command & Control** - C2 server communication
7. **Actions on Objectives** - data theft or destruction

### APT (Advanced Persistent Threat) - Characteristics

**Component Definitions:**
- **ADVANCED** - advanced knowledge, techniques, tools
- **PERSISTENT** - persistent, long-term, "low-and-slow"  
- **THREAT** - coordinated, deliberate, targeted

**Example APT Groups:**
- **APT1** (Comment Crew) - China, PLA Unit 61398
- **Lazarus Group** - North Korea, responsible for WannaCry
- **Fancy Bear (APT28)** - Russia, GRU
- **Cozy Bear (APT29)** - Russia, SVR

## Threat Indicators (IOC) - Practical Identification

### IOC Categories by "Pyramid of Pain":

#### Level 1 - Hash Values (easy to change):
- MD5, SHA-1, SHA-256 of files
- Example: `a1b2c3d4e5f6...`

#### Level 2 - IP Addresses:
- C2 server addresses
- Example: `192.168.1.100`

#### Level 3 - Domain Names:
- Domains used in attacks
- Example: `malicious-site.com`

#### Level 4 - Network/Host Artifacts:
- File names, paths, registry keys
- Example: `%TEMP%\malware.exe`

#### Level 5 - Tools:
- Specific tools used by attackers
- Example: Mimikatz, Cobalt Strike

#### Level 6 - TTPs (hardest to change):
- Tactics, techniques, procedures
- Example: "Using PowerShell to download second stage"

### Practical IOC Indicators from Presentation:

**Behavioral Anomalies:**
- Strange login activities (outside work hours)
- Unusual DNS queries (to C2 domains)
- "Non-human" web traffic (bots, automation)
- Unusual network activity IN/OUT
- Geolocation anomalies (logins from different countries)
- Increased disk R/W (possible exfiltration)
- Unusual software updates
- Strange frame and packet sizes
- Unauthorized changes in user profiles
- DDoS attacks
- Incorrectly signed documents/certificates
- Service availability problems
- Disproportionate queries/responses
- Unauthorized registry changes
- General system slowdowns

## Cyber Threat Intelligence (CTI)

### CTI Definition and Scope:
**Cyber Threat Intelligence** is a specialized OSINT branch focusing on:
- Cybersecurity threats
- Supporting organizations in fighting cybercriminals  
- Preventing cyberattacks through pattern recognition
- Analyzing IOC indicators, TTPs, and incidents

### Practical CTI Tools:

#### Threat Intelligence Platforms:
- **OpenCTI** - https://docs.opencti.io/ (open source)
- **MISP** - https://misp.github.io/ (Malware Information Sharing Platform)
- **AlienVault OTX** - https://otx.alienvault.com/
- **ThreatConnect** - enterprise commercial solution

#### OSINT Framework - Intelligence Resources:
- **OSINT Framework** - https://osintframework.com/
- **Nixintel's Resource List** - https://start.me/p/rx6Qj8/
- **AttackerKB** - https://attackerkb.com/
- **Ransomlook** - https://www.ransomlook.io/recent
- **DNS Dumpster** - https://dnsdumpster.com/
- **Domain Tools WHOIS** - https://whois.domaintools.com/

#### Technical Reconnaissance - Advanced Tools:
- **Censys** - https://search.censys.io/
- **ZoomEye** - https://www.zoomeye.ai
- **Criminal IP** - https://www.criminalip.io/
- **URLScan** - https://urlscan.io/

#### Malware and Threat Analysis:
- **VirusTotal** - https://virustotal.com (file/URL analysis)
- **Malware Traffic Analysis** - https://malware-traffic-analysis.net/
- **Dynamite AI Lab** - https://lab.dynamite.ai/
- **Malpedia** - https://malpedia.caad.fkie.fraunhofer.de/
- **MalwareBazaar** - https://bazaar.abuse.ch/browse/

### CVSS (Common Vulnerability Scoring System)

**CVSS 4.0 - Current Vulnerability Assessment Standards:**
- **Calculator** - https://www.first.org/cvss/calculator/4-0
- **Alternative Calculator** - https://chandanbn.github.io/cvss/

**CVSS Metrics:**
- **Base Score** (0.0-10.0) - basic vulnerability assessment
- **Temporal Score** - changes over time (available exploits, patches)
- **Environmental Score** - specific to organizational environment

## Practical Tools for Specialists

### Tool Installation and Configuration:

#### MISP - Community Threat Intelligence:

```bash
wget --no-cache -O /tmp/INSTALL.sh
https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/INSTALL.sh
bash /tmp/INSTALL.sh -A
```

**Requirements:** Ubuntu 22.04 LTS, non-root user

#### OpenCTI - Threat Intelligence Platform:

#### Using Docker
https://docs.opencti.io/latest/deployment/installation/#using-docker


#### Reconnaissance Tools:
- **theHarvester** - email addresses, subdomain collection
- **crt.sh** - SSL certificate search
- **FerroxBuster** - web directory fuzzing (FFuf alternative)
- **SpiderFoot(-HX)** - https://github.com/smicallef/spiderfoot

## Competency Development - Career Path

### Certification Path According to PaulJerimy:
**Link:** https://pauljerimy.com/security-certification-roadmap/

#### Entry-Level:
- **CompTIA Security+** - cybersecurity fundamentals
- **CompTIA Network+** - networking basics
- **CISSP Associate** - security management

#### Mid-Level:
- **CISSP** - Certified Information Systems Security Professional
- **CISA** - Certified Information Systems Auditor  
- **CISM** - Certified Information Security Manager

#### Advanced:
- **CISSP Concentrations** - specializations
- **SABSA** - security architecture
- **TOGAF** - enterprise architecture

#### Technical/Hands-on:
- **CEH** - Certified Ethical Hacker
- **OSCP** - Offensive Security Certified Professional
- **GIAC** - various technical specializations

### Where to Learn - 2025 Recommendations:

#### Training Platforms:
- **Sekurak.Academy** - comprehensive Polish-language training
- **HackTheBox** - practical network security labs
- **PortSwigger Academy** - web application security (BURP Suite)
- **Cybrary** - free online courses
- **SANS** - prestigious training and certifications

#### Community and Networking:
- **Discord #szkolenie-1** - Polish knowledge exchange
- **Reddit r/cybersecurity** - international community
- **LinkedIn Groups** - professional networking
- **Conferences** - BSides, DefCon, BlackHat

## Trends and Forecasts for 2025-2026

### Key Threats According to Experts:

#### 1. AI vs AI - Arms Race
- **Attackers use AI** to generate phishing and malware
- **Defenders use AI** for detection and response  
- **85%** of professionals see increased attacks due to generative AI
- **60%** of IT experts indicate AI-enhanced malware as main threat

#### 2. Supply Chain - Expanding Risk
- **45%** of organizations will experience supply chain attacks
- **Domino Effect** - one supplier = thousands of victims
- **Software Supply Chain** - attacks on code repositories
- **Hardware Supply Chain** - chip backdoors

#### 3. Cloud Security - New Challenges
- **Multi-cloud** - security management complexity
- **Container Security** - Kubernetes, Docker
- **Serverless** - Function-as-a-Service security
- **Identity is the new perimeter** - cloud identity management

#### 4. Quantum Computing - Post-Quantum Preparations
- **NIST Post-Quantum Cryptography** - new encryption standards
- **Crypto-Agility** - ability to quickly change algorithms
- **Timeline** - practical quantum computers in 2030s+
- **Preparation Now** - start migration now

### Cybersecurity Budgets and Investments:
- **15%** increase in global cybersecurity spending in 2025
- **377 billion USD** - predicted global spending by 2028
- **12.2%** annual investment growth
- **USA and Western Europe** - 70% of global spending

### Skills Gap - Specialist Shortage:
- **85 million** - predicted specialist shortage by 2030
- **74 out of 100** - ratio of available candidates to job offers in USA
- **10%** of employers require AI as mandatory skill
- **54%** of positions no longer require formal higher education

## Summary and Key Conclusions

### Fundamental Information Security Principles:

1. **Defense in Depth** - layered defense
2. **Zero Trust** - "never trust, always verify"
3. **Continuous Monitoring** - continuous monitoring and response
4. **Human Factor** - 98% of attacks exploit human element
5. **Risk-Based Approach** - risk-based prioritization

### Practical Recommendations for Organizations:

#### Immediate Actions:
1. **Password Manager Implementation** - for all employees
2. **MFA Enforcement** - on all critical systems  
3. **Software Updates** - especially zero-day patches
4. **3-2-1 Backup** - 3 copies, 2 different media, 1 offline
5. **Employee Training** - phishing and social engineering awareness

#### Medium-term (6-12 months):
1. **SIEM/SOC Implementation** - centralized monitoring
2. **Incident Response Plan** - incident response procedures
3. **Penetration Testing** - regular penetration tests
4. **Threat Intelligence** - threat feed subscription
5. **Compliance Framework** - ISO27001, NIST, etc.

#### Long-term (12+ months):
1. **Zero Trust Architecture** - architecture redesign
2. **AI-Powered Security** - AI-based tool implementation
3. **Post-Quantum Cryptography** - quantum era preparation
4. **Security Culture** - security culture building
5. **Continuous Improvement** - continuous process improvement

### Resources for Further Learning:

#### Instructor's Educational Platforms:
- **ksiazka.sekurak.pl** - publications and books
