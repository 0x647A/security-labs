# CyberWomen Leaders – Training 9: Cloud and Virtual Environment Security

## 1. Introduction and Training Objectives
This session focuses on securing cloud and virtual environments, covering:
- Shared Responsibility Model
- Access control failures in cloud services
- Reconnaissance techniques in the cloud
- VPC network architecture and isolation mechanisms
- Traffic tunneling (SSH SOCKS proxy)
- Common web application vulnerabilities in cloud contexts (SSRF, XXE)
- Defending against metadata service abuse (IMDS)
- Managing publicly known component vulnerabilities
- Hands-on demos: from reconnaissance to flag exfiltration

## 2. Cloud Infrastructure Responsibility
### 2.1 Shared Responsibility Model
- Cloud provider secures the “cloud” (physical layer, hardware, hypervisor).
- Customer secures configuration, applications, data, and identities.

#### Documentation Links
- Microsoft Azure Shared Responsibility Model  
- OWASP Top 10 CI/CD Security Risks  
- OWASP Cloud-Native Application Security Top 10  

## 3. Access Control Failures
- Over-privileged resource permissions (e.g., S3 buckets).
- Impact: unauthorized read/write/modify/delete.
- Recommendation: enforce least privilege and verify necessary access.

## 4. Cloud Reconnaissance
### 4.1 Tools and Techniques
- **masscan** – extremely fast port scanning
```bash
masscan -p 80,443 192.168.0.0/24
masscan -p- 192.168.0.1 --rate 250000
masscan -p U:123,U:53 192.168.0.1
```

- **nmap** – precise host and service discovery  
```bash
nmap -sn 10.0.0.0/24
nmap -Pn 10.0.0.0/24
nmap -sS 192.168.89.191 -D 10.0.0.1,10.0.0.2
nmap -iL list.txt -p80,443
nmap -oA allformats 192.168.1.2 -p22
```

- **Google Hacking Database** – finding public exploits and S3 buckets  
- **grayhatwarfare** – discovering public storage (AWS, Azure, GCP)  
- **VirusTotal** – file scanning and subdomain enumeration  
- **crt.sh** – certificate transparency and subdomains  
- **subfinder**, **ffuf** – automating subdomain and web path discovery  
- **gowitness** – website screenshots and reports

### 4.2 Cloud CLI Tools
- AWS CLI, GCP gcloud, Azure CLI for asset enumeration:

```bash
aws configure list
aws configure --profile test
aws ec2 describe-instances
gcloud compute instances list
az vm list
```

## 5. Instance Metadata Service (IMDS)
- Retrieves VM metadata (name, network, IAM role, temporary keys).
- Endpoint: `http://169.254.169.254`
- IMDSv2 requires a token:
```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token"
-H "X-aws-ec2-metadata-token-ttl-seconds:21600")
curl -H "X-aws-ec2-metadata-token:$TOKEN"
http://169.254.169.254/latest/user-data
```

- Defense:
    - Enforce IMDSv2 token requirement
    - Restrict metadata endpoint via firewall
    - Disable if not needed

## 6. VPC Network Architecture
- Two subnets: public (public IPs) and private (NAT Gateway for egress).
- Default Network ACLs may allow inter-subnet traffic.
- Security Groups control instance-level port access.
- Common pitfall: missing subnet isolation controls.

## 7. SSH Traffic Tunneling
- Establish a SOCKS proxy:
```bash
ssh -i ~/.ssh/id_ed25519 -D 9999 user@bastion.example.com
```

- Configure Burp Suite: host `127.0.0.1`, port `9999`
- Enables browsing internal resources via proxy.

## 8. Web Application Vulnerabilities in Cloud
### 8.1 Server-Side Request Forgery (SSRF)
- Forces server to send HTTP requests to internal hosts.
- Example: avatar upload URL `http://localhost:8983`
- Can exfiltrate IMDS data:

```bash
http://169.254.169.254/latest/meta-data/iam/security-credentials/role
```

### 8.2 XML External Entity (XXE)
- Injects external entities to read local or remote resources:
```html
<!DOCTYPE x [ <!ENTITY s SYSTEM "http://localhost:8983">
]>
<root>
<elem>&s;</elem>
</root>
```

### 8.3 Bypassing URL Filters
- Alternative 127.0.0.1 representations:
- `127.0.0.1`, `localhost`, `0x7f.000001`, `017700000001`, `2130706433`
- nip.io wildcard DNS:
- `10.0.0.1.nip.io` → 10.0.0.1

## 9. Mitigations for SSRF and XXE
- Enforce strict URL protocol checks (`http`/`https`).
- Implement allow-lists for domains/IPs.
- Restrict outbound traffic via firewall.
- Use dedicated proxy for external requests.

## 10. Demo 1 & 2: Reconnaissance and Metadata Access
1. SSH to bastion, retrieve IMDSv2 token, fetch user-data.  
2. VPC scan:
```bash
masscan -p22 10.10.0.0/16 --rate 1000
nmap -sT -p- 10.10.1.99 -sV
```
3. Finding: default NACLs allowed inter-subnet communication.

## 11. Demo 3: SSRF Exploitation and Flag Exfiltration
1. Inject SSRF URL in upload form:
```bash
https://domain/upload?url=http://127.0.0.1?.jpg
```
2. List S3 bucket with exfiltrated IAM keys:
```bash
aws s3 ls s3://bucket-name
aws s3 sync s3://bucket-name s3-data
grep -R 'FLAG' s3-data
```

## 12. Publicly Known Component Vulnerabilities
- Outdated libraries, dependencies, and services.
- Identify versions, search CVEs and exploits:
    - CVE MITRE, Exploit-DB, GitHub.
- Mitigation: continuous version scanning and patch management.

## 13. Demo 4: GitLab CVE-2023-5612 & CVE-2023-7028
1. Identify GitLab port (38123) and access `/explore`.  
2. Retrieve commit emails using `?format=atom`:
```bash
https://host:38123/project/repo/tags?format=atom
```
3. Reset victim’s password, capture email via webhook.site.  
4. Defense: ensure timely component updates and secure password reset flows.

