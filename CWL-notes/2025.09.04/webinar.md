# CompTIA Security+ SY0-701 - Training Notes

## Exam Structure and Domain Breakdown

### Domain 1: General Security Concepts (12%)
### Domain 2: Threats, vulnerabilities and mitigations (22%)  
### Domain 3: Security architecture (18%)
### Domain 4: Security operations (28%) - largest domain
### Domain 5: Security program management and oversight (20%)

## Domain 1: General Security Concepts (12%)

### 1.1 Security Controls

#### Types of Security Controls
- **Preventive Controls** - prevent incidents from occurring
- **Detective Controls** - detect incidents as they occur  
- **Corrective Controls** - remediate the effects of incidents

#### Control Diversity
- **Technical** - firewalls, IDS/IPS systems, encryption
- **Administrative** - security policies, procedures, training
- **Physical** - locks, access control, monitoring

### 1.2 Fundamental Security Concepts

#### Defense-in-Depth (Layered Defense)
**Definition**: Layered approach to security - using multiple types of controls to provide redundancy and increase attack resilience.

**Key Principles**:
- **Technology Diversity** - different operating systems, programming languages, applications (avoiding single point of failure)
- **Vendor Diversity** - avoiding dependency on a single vendor
- **Control Diversity** - combination of technical, administrative, and physical controls

### 1.3 Change Management
- Systematic approach to implementing system changes
- Control and documentation of all modifications
- Risk minimization related to changes

### 1.4 Cryptographic Solutions
- Data encryption at rest and in transit
- PKI (Public Key Infrastructure)
- Digital signatures and certificates
- Cryptographic key management

## Domain 2: Threats, Vulnerabilities and Mitigations (22%)

### 2.1 Threat Actors and Motivations
- **Nation-state actors** - state-sponsored actors
- **Cybercriminals** - financially motivated criminals  
- **Hacktivists** - ideologically motivated hackers
- **Insider threats** - internal threats

### 2.2 Threat Vectors and Attack Surfaces

#### Main Attack Vectors
- **Malware, phishing, ransomware** - malicious software
- **DoS and botnets** - denial of service attacks
- **Wireless Attacks**:
  - **Evil Twin** - rogue WiFi access points
  - **DeAuth** - forced disconnection of WiFi clients
- **Application Attacks**:
  - **SQL Injection (SQLi)** - injecting malicious SQL code
  - **Cross-Site Scripting (XSS)** - executing scripts in victim's browser
  - **SSRF** - Server-Side Request Forgery

### 2.3 Vulnerabilities

#### CVE/CVSS System
- **CVE** (Common Vulnerabilities and Exposures) - standard vulnerability identification
- **CVSS** (Common Vulnerability Scoring System) - criticality scoring 0-10 scale

### 2.4 Malicious Activity

#### Supply Chain Attacks
**Definition**: Attacks exploiting dependencies in the supply chain (hardware, software, services)

**Attack Vector Examples**:
- Malicious software updates
- Firmware backdoors  
- Compromised hardware components

**Safeguards**:
- Vendor auditing
- Security certificates
- Version control
- Digital signature verification

#### IoT/OT Threats
**IoT (Internet of Things)**:
- Lack of updates
- Weak passwords
- DDoS attacks (e.g., Mirai botnet)

**OT (Operational Technology)**:
- Industrial control systems - often legacy, without updates
- Difficult to replace due to process criticality

**SCADA**:
- Industrial process monitoring systems
- Vulnerable to Stuxnet-type attacks
- Critical infrastructure

**Main IoT/OT Risks**:
- Lack of network segmentation
- Weak authorization  
- Remote attacks on **HMI** interfaces, **PLC**, sensors

### 2.5 Mitigation Techniques
- Security control implementation
- Regular updates and patching
- Network segmentation
- Threat monitoring and detection

## Domain 3: Security Architecture (18%)

### 3.1 Architecture Models

#### Shared Responsibility Model
**Definition**: Model defining responsibility division between cloud provider (CSP) and customer

**SaaS** (Software as a Service):
- **CSP responsible for**: OS, applications, infrastructure, runtime
- **Customer responsible for**: data and user access

**PaaS** (Platform as a Service):  
- **CSP responsible for**: platform, OS, infrastructure
- **Customer responsible for**: applications and data

**IaaS** (Infrastructure as a Service):
- **CSP responsible for**: infrastructure (servers, network, storage)
- **Customer responsible for**: OS, applications, configurations

### 3.2 Enterprise Infrastructure
- Enterprise network architecture
- Segmentation and microsegmentation
- Zero Trust Architecture (ZTA)
- ICAM (Identity, Credential, Access Management)

### 3.3 Data Protection
- **Data Classification** - data classification by sensitivity
- **Data/Drive Encryption** - data and disk encryption  
- **DLP** (Data Loss Prevention) - preventing data loss
- **Data Wiping** - secure data deletion

### 3.4 Resilience and Recovery
- **Business Continuity Plan** - business continuity planning
- **IT Disaster Recovery Plan** - IT disaster recovery plan
- **Disaster Recovery Sites**:
  - **Hot Site** - full replica, ready immediately
  - **Warm Site** - partial infrastructure  
  - **Cold Site** - basic infrastructure

## Domain 4: Security Operations (28%)

### 4.1 Computing Resources
- Computing resource management
- Virtualization and containerization
- Cloud computing security

### 4.2 Asset Management
- **Asset inventory** - complete IT asset inventory
- **Asset classification** - classification by criticality
- **Lifecycle management** - lifecycle management
- **CMDB** (Configuration Management Database)

### 4.3 Vulnerability Management
- **External/Internal Vulnerability Scanning** - vulnerability scanning
- **Patch Management** - update management
- Risk-based prioritization
- **Remediation tracking** - remediation tracking

### 4.4 Alerting and Monitoring

#### SIEM (Security Information and Event Management)
- **Centralized collection** of logs and events
- **Event correlation** - attack pattern detection  
- **Real-time monitoring** - real-time monitoring
- **Security Dashboard** - security dashboards
- **Continuous Monitoring & Assessment** - continuous monitoring

#### SOC/NOC Operations
- **SOC/NOC Monitoring (24x7)** - 24/7 monitoring
- **Escalation Management** - escalation management
- **Situational Awareness** - situational awareness
- **Security SLA/SLO** - security service levels

### 4.5 Enterprise Security

#### Perimeter Security
- **Firewall** - network traffic control
- **VPN** - secure remote connections
- **DMZ** - demilitarized zone  
- **IDS/IPS** - intrusion detection and prevention
- **Web Content Filter** - content filtering
- **WAF** (Web Application Firewall) - web application firewall

#### Network Security
- **Internal IDS/IPS** - internal detection systems
- **DDoS Prevention** - denial of service protection
- **NAC** (Network Access Control) - network access control
- **VoIP Security** - voice communication security
- **Wireless Security** - wireless network protection
- **Honeypots** - attacker traps

#### Endpoint Security  
- **NGAV/EDR/MDR** - advanced endpoint protection
- **Endpoint Hardening** - device security hardening
- **File Integrity Monitoring** - file integrity monitoring
- **Mobile Security** - mobile device protection
- **Endpoint Disk Encryption** - disk encryption

#### Application Security
- **Vulnerability Scanning** - application vulnerability scanning
- **Static App Testing** - static code analysis
- **Dynamic App Testing** - dynamic application testing  
- **Database Security** - database protection
- **Virtual Patching** - virtual patching

### 4.6 Identity and Access Management
- **ICAM/ZTA** - identity management in Zero Trust architecture
- **2FA/MFA** - multi-factor authentication
- **Device Management** - device management
- **White/Blacklisting** - allowed/forbidden lists

### 4.7 Automation and Orchestration
- Security process automation
- SOAR (Security Orchestration, Automation and Response)
- Playbook automation

### 4.8 Incident Response

#### NIST 800-61 Framework (DFIR)
**1. Preparation**:
- **CSIRT** team creation (Computer Security Incident Response Team)
- Procedure and playbook development
- Tool preparation

**2. Detection & Analysis**:
- Incident identification
- Classification and prioritization
- Initial analysis

**3. Containment, Eradication & Recovery**:
- Threat isolation
- Root cause removal  
- Normal operation restoration

**4. Post-Incident Activity**:
- Incident analysis
- Lessons learned
- Procedure updates

#### Digital Forensics
- Digital evidence collection
- **Chain of custody** - evidence chain
- Artifact analysis
- Legal reporting

### 4.9 Data Sources
- **Logging** - event logging at all levels
- **Cyber Threat Intelligence** - threat analysis
- Security analysis data sources

## Domain 5: Security Program Management and Oversight (20%)

### 5.1 Security Governance
- **IT Security Governance** - IT security governance
- **Security Plan** - organizational security plan
- **Security Policies & Compliance** - policies and compliance

### 5.2 Risk Management  
- **Risk Management** - risk identification, analysis and mitigation
- **Security Architecture & Design** - security architecture and design
- Risk assessment methodologies

### 5.3 Third-party Risk
- **Third party and risk management** - vendor risk management
- **Supply chain risk** - supply chain risk
- **SLA** (Service Level Agreements) - service level agreements
- Due diligence processes

### 5.4 Security Compliance
- Regulatory compliance (GDPR, HIPAA, SOX, PCI DSS)
- **Continuous C&A** - continuous certification and accreditation
- Compliance auditing

### 5.5 Audits and Assessments
- **Security audits** - security auditing  
- **Vulnerability Assessment** - vulnerability assessment
- **Penetration Testing** - penetration testing
- Internal vs External audits

### 5.6 Security Awareness

#### Awareness Training  
**Goal**: Building security awareness and habits among employees

**Training Topics**:
- Phishing and social engineering recognition
- Password management and MFA
- Sensitive data handling  
- BYOD and remote work policies

**Methods**:
- **Tabletop exercises** - simulation exercises
- **Phishing simulations** - controlled testing
- **Online training** - e-learning
- **Information campaigns** - posters, newsletters
- **Challenge policy** - visitor ID verification at reception

#### Culture of Security
- Building organizational security culture
- Leadership engagement
- Regular communication
- Security champions programs

## Physical and Environmental Security

### Physical Controls
#### AAA (Authentication, Authorization, Accounting)
- Access authorization to buildings and zones (server rooms, data centers)

#### Site Layout, Fencing, Lighting  
- Secure zones
- Appropriate fencing
- Lighting, signage

#### Locks & Gateways
- Mechanical, electronic, biometric locks

### Environmental Controls
#### HVAC
- Maintaining temperature 20-22°C and humidity ~50%

#### Hot/Cold Aisles
- Server room cooling optimization

#### Fire Suppression  
- Fire suppression systems based on "fire triangle"

#### Faraday Cages, PDS
- **Faraday cages** - electromagnetic shielding
- **Protected Distribution Systems** - cable protection against eavesdropping and physical attacks

## Key Acronyms and Terms

- **ICAM** - Identity, Credential, and Access Management
- **ZTA** - Zero Trust Architecture  
- **C&A** - Certification and Accreditation
- **NGAV** - Next Generation Antivirus
- **EDR** - Endpoint Detection and Response
- **MDR** - Managed Detection and Response
- **HMI** - Human Machine Interface
- **PLC** - Programmable Logic Controller
- **CSIRT** - Computer Security Incident Response Team
- **DFIR** - Digital Forensics and Incident Response
- **MDM** - Mobile Device Management
- **DLP** - Data Loss Prevention
- **NAC** - Network Access Control
- **WAF** - Web Application Firewall

## Most Important Security Principles

1. **Defense in Depth** - layered defense
2. **Principle of Least Privilege** - minimal privileges  
3. **Zero Trust** - "never trust, always verify"
4. **Risk Management** - risk management as continuous process
5. **Incident Response** - incident preparedness
6. **Continuous Monitoring** - continuous monitoring
7. **Security Awareness** - awareness as security foundation
