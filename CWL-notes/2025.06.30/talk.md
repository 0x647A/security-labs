# CyberWomen Leaders – Training 2: Risk Management and Regulatory Compliance

## 🎯 TRAINING OBJECTIVES
1. **UNDERSTAND** relevant standards and regulations  
2. **MEASURE** organizational risk  
3. **BUILD** an effective defense  

**Key acronyms:** NIS2, DORA, ARO, SLE

## 📋 MODULE 1: RISK FUNDAMENTALS

### Core Cybersecurity Truth
> **“You can’t protect everything effectively!”**

**Challenge:** Limited resources (budget, time, personnel) versus limitless threats (XSS, SQLi, IDOR, zero-days, RCE, CSRF)  
**Question:** What to prioritize first?

### Key Definitions

#### Asset
- **DATA:** Customer information, intellectual property  
- **SYSTEMS:** Servers, applications, infrastructure  
- **REPUTATION:** Trust of customers and partners  

#### Threat
- **DELIBERATE:** Hacker attacks, malware, theft  
- **NATURAL:** Fire, flood (e.g., OVH data center fire, March 2021)  
- **ACCIDENTAL:** Human error, hardware failure  

#### Vulnerability
- **TECHNICAL:** Outdated software, misconfiguration  
- **HUMAN:** Weak passwords, phishing  
- **PHYSICAL:** Unsecured server room  

### Fundamental Equation

RISK = THREAT + VULNERABILITY (against an ASSET)

## 🔄 MODULE 2: RISK MANAGEMENT PROCESS

### Five-Step Process (NIST SP 800-30)

| Step | Name           | Question                      | Activities                                   |
|------|----------------|-------------------------------|----------------------------------------------|
| 1    | Identify       | What are we concerned about?  | Brainstorming, interviews, incident reviews, checklists |
| 2    | Analyze        | How severe and frequent?      | Likelihood and impact assessment             |
| 3    | Evaluate       | What is most critical?        | Compare against risk appetite                |
| 4    | Respond        | What actions to take?         | Mitigate / Transfer / Avoid / Accept         |
| 5    | Monitor        | Is the strategy still valid?  | Continuous control evaluation                |

### Identification Techniques
1. **Brainstorming & Interviews** – cross-department perspectives  
2. **Incident Analysis** – learning from case studies  
3. **Checklists & Knowledge Bases** – industry standards  

### Qualitative vs. Quantitative Analysis
- **Qualitative:** Subjective, descriptive; Low/Medium/High scale  
- **Quantitative:** Numerical, data-driven; produces monetary metrics  

### Quantitative Metrics
- **SLE (Single Loss Expectancy)** = Asset Value × Exposure Factor  
- **ARO (Annualized Rate of Occurrence)** = expected events per year  
- **ALE (Annualized Loss Expectancy)** = SLE × ARO  

### Risk Appetite
Board-defined threshold of acceptable risk. If exceeded → action required.

### Response Strategies

| Strategy    | Goal                                             | Examples                              |
|-------------|--------------------------------------------------|---------------------------------------|
| Mitigation  | Reduce likelihood or impact                      | Antivirus, training, password policies |
| Transfer    | Shift financial loss                             | Cyber insurance, MSSP outsourcing     |
| Avoidance   | Eliminate risk source                            | Decline high-risk technology          |
| Acceptance  | Formal decision to accept risk                   | When mitigation cost > ALE            |

## 🏗 MODULE 3: GRC STRUCTURES AND FRAMEWORKS

- **Governance:** Strategy, roles, accountability  
- **Risk:** Identification, analysis, response  
- **Compliance:** Legal and policy adherence (GDPR, NIS2, DORA)

### Documentation Pyramid

| Level     | Purpose                     | Example                              |
|-----------|-----------------------------|--------------------------------------|
| Policy    | Why and what                | “We protect personal data”           |
| Standard  | Required technologies/processes | “All disks must be encrypted”        |
| Procedure | Step-by-step instructions   | “How to enable BitLocker”            |

### ISO 27001 vs. NIST CSF

|              | ISO 27001                                    | NIST CSF                             |
|--------------|----------------------------------------------|--------------------------------------|
| Focus        | Formal Information Security Management System (ISMS) | Practical best-practice framework    |
| Approach     | Certification, audit-ready                   | Five core functions                  |
| Functions    | –                                            | Identify, Protect, Detect, Respond, Recover |

## 🏢 MODULE 4: BUSINESS CONTINUITY & LEGAL ENVIRONMENT

### BCP vs. DRP

|                         | BCP (Business Continuity Plan)               | DRP (Disaster Recovery Plan)        |
|-------------------------|----------------------------------------------|-------------------------------------|
| Objective               | Maintain critical business functions         | Restore IT infrastructure and data  |
| Examples                | Alternative work sites, client communication | Backups, replication, system restore |

### Key Metrics
- **RTO (Recovery Time Objective):** Maximum allowable downtime  
- **RPO (Recovery Point Objective):** Maximum allowable data loss  

### Regulations Overview
- **GDPR:** 72 h breach notification, DPIA, right to erasure  
- **NIS2:** Risk management, incident reporting (24 h), triage report (72 h), audits every 3 years  
- **DORA:** ICT risk management, resilience testing (TLPT), incident reporting, sanctions up to 10% turnover
- **PCI-DSS:** Global standard, applies to: Any business that stores, processes, or transmits payment card data
- **HIPPA:** An American law on portability and accountability in health insurance, applies to: Organizations in the healthcare sector in the USA
- **SOX:** The American Sarbanes-Oxley Act, applies to: Public companies listed on US stock exchanges
- **COSO:** Framework created for designing and implementing internal controls
- **FAIR:** Model for quantitative risk assessment.
