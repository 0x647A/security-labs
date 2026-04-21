# CyberWomen Leaders – Training 6: Network Security

## 1. Network Fundamentals and the OSI/ISO Model

### OSI/ISO Model – Detailed Layers

**Layer 1: Physical**  
- Carries raw bits over cables, fiber, or wireless  
- Defines voltages, signal timing, bit rate, connectors, hubs  

**Layer 2: Data Link**  
- Frames bits into Ethernet frames  
- MAC addressing and switch forwarding  
- Error detection (CRC) and ARP for MAC↔IP lookups  

**Layer 3: Network**  
- Routes IP packets across networks  
- IP addressing (IPv4/IPv6), TTL, fragmentation  
- Routers, ICMP for diagnostics  

**Layer 4: Transport**  
- End-to-end host communication  
- TCP: ports, sequence numbers, ACKs, windowing  
- UDP: ports, connectionless, minimal overhead  

**Layer 5: Session**  
- Establishes/terminates dialogs  
- Manages full/half-duplex exchanges and checkpoints  

**Layer 6: Presentation**  
- Translates and formats data  
- Encryption/decryption, compression, character encoding  

**Layer 7: Application**  
- Interfaces for user applications  
- Protocols: HTTP, SMTP, DNS, FTP, SSH, etc.  
- Directly supports services like web browsing and email  

**Packet Structure:**

1. **Ethernet Header**  
   - Destination MAC | Source MAC | Ethertype  

2. **IP Header**  
   - Source IP → Destination IP  
   - Version | IHL | TTL | Protocol  

3. **TCP Header**  
   - Source Port → Destination Port  
   - Seq # | Ack # | Flags (SYN/ACK/FIN) | Window Size  

4. **HTTP Payload**  
   - HTTP Method/Status | Headers | Body  

Flow:  
[Dst MAC|Src MAC|Type] → [Src IP→Dst IP|TTL|Proto] → [Src Port→Dst Port|Flags|Seq/Ack] → [HTTP Data]

**TCP Three-Way Handshake:**  
1. SYN (SEQ: 100) – Host A → Host B  
2. SYN-ACK (ACK: 101, SEQ: 300) – Host B → Host A  
3. ACK (ACK: 301, SEQ: 101) – Host A → Host B

## 2. Attacks on OSI Layers

### Layer 2 (Data Link)  
- **MAC Flooding**  
  - Send massive bogus MAC addresses to a switch  
  - Switch MAC table overflows → fail-open (broadcast all traffic)  
  - Attacker can sniff all VLAN traffic  

- **ARP Spoofing**  
  - Forge ARP replies mapping attacker’s MAC to victim IP  
  - Intercept or redirect traffic (Man-in-the-Middle)  
  - Commonly used to capture credentials or inject malicious packets  

### Layer 3 (Network)  
- **Routing Protocol Attacks**  
  - Manipulate RIP/OSPF/BGP advertisements  
  - Route poisoning: Inject false routes → traffic rerouted through attacker  

- **IP Spoofing**  
  - Craft packets with forged source IP  
  - Bypass ACLs or hide attacker’s real address  
  - Often used in DDoS amplification and reflection attacks  

## 3. Network Recon and Port Scanning

### Key Info

- TCP/UDP port range: **0–65535**  
- Any service can run on any port (e.g., HTTP ≠ port 80)  
- nmap may misidentify services by default

### Port States (nmap)

| Protocol | State         | Indicator | Description                |
|----------|---------------|-----------|----------------------------|
| TCP      | open          | SYN-ACK   | TCP connection established |
| TCP      | closed        | RST       | Port closed                |
| TCP      | filtered      | no reply  | Firewall or network filter |
| UDP      | open          | response  | Service responded          |
| UDP      | closed        | ICMP 3/3  | Port unreachable           |
| UDP      | open|filtered | no reply  | Open or filtered           |

### nmap Scan Types

- **-sS** – SYN scan (stealth handshake)  
- **-sT** – Connect scan (full handshake)  
- **-sF/-sX/-sN** – FIN/XMAS/NULL scans (advanced stealth)  
- **-Pn** – skip host discovery  
- **-sV** – version detection (banner grabbing)  
- **-p-** – scan all ports  

**Example:**

```bash
nmap -Pn -sV -p- -iL hosts.txt -oX output.xml
```

### Banner Grabbing
- **nc/ncat** – manual  
- **nmap -sV** – automated

## 4. Web Application Recon and Testing

### Directory/File Fuzzing

Tools:  
**gobuster**  
A CLI tool written in Go for directory/file and DNS brute-forcing. Fast, supports wordlists, extensions, virtual hosts, and status code filtering.

**dirbuster**  
A Java GUI application for brute-forcing web directories and files. Uses customizable wordlists and supports recursive scanning, making it beginner-friendly.

**ffuf**  
A fast, flexible fuzzing tool in Go for discovering hidden resources on web servers.  
Example: `ffuf -w /usr/share/wordlists/dirb/big.txt -u https://target/FUZZ -fc 301,403`) 
– `-w` specifies wordlist, `-u` target with FUZZ marker, `-fc` filters out 301/403 responses.

**feroxbuster**  
A Rust-based recursive content discovery tool. Combines speed and recursion: it auto-expands directories found, supports custom wordlists, extensions, threading, and status code or size filters.    
`feroxbuster -u https://target -w /path/words.txt`

**Wordlists:** `/usr/share/wordlists/dirb/`, SecLists

### Burp Suite

- **Type:** HTTP/HTTPS intercepting proxy  
- **Use:** Industry standard for web application and API security testing  
- **Default Port:** 8080 (can configure others)  
- **HTTPS Support:** Install Burp’s CA certificate in your browser to decrypt SSL/TLS traffic  
- **Core Modules:**  
  - **Target:** Define and manage scope  
  - **Proxy:** Intercept, view, and modify requests/responses  
  - **Spider:** Crawl application to discover content (automated mapping)  
  - **Scanner (Pro):** Automated vulnerability scanning  
  - **Intruder:** Customizable automated attacks (fuzzing, brute-force)  
  - **Repeater:** Manually modify and resend individual requests  
  - **Sequencer:** Analyze randomness of session tokens and nonces  

## 5. DDoS Attacks

An attack in which numerous compromised or controlled devices (a botnet) simultaneously send a massive number of requests to a target (server or service), overwhelming it and preventing legitimate traffic from being served. 

### Motivations
- Socio-political: protests, hacktivism (e.g., ACTA)  
- Military/geopolitical: infrastructure disruption, cyber warfare  
- Criminal: extortion, business competition  

### Attack Types

#### Layers 3–4 (Volumetric)
- **SYN/UDP Flood:** saturate bandwidth  
- **DNS/NTP Amplification:** small query → large response  
- **TCP Christmas Tree:** all TCP flags set  

#### Layer 7 (Application)
- **HTTP GET/POST Flood:** resemble normal user traffic  

### Mitigation
- Network isolation, VLAN segmentation  
- Out-of-state packet filtering, rate limiting, ACLs  
- Deep Packet Inspection, behavioral analysis  
- Cloud DDoS services (Cloudflare/Akamai)  
- On-prem DDoS appliances as additional layer  
- IDS/IPS (Snort/Suricata) rules for SYN/FIN/XMAS detection  

**iptables Example (Christmas Tree):**

```bash
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
iptables -A INPUT -p tcp --tcp-flags FIN,PSH,URG FIN,PSH,URG -j DROP
```

## 6. Detection & Response

### Defense-in-Depth Components

| Component | Role                                                                        | Example Tools                          |
|-----------|-----------------------------------------------------------------------------|----------------------------------------|
| EDR       | Endpoint detection, behavioral analysis, sandboxing, threat hunting         | CrowdStrike Falcon, Microsoft Defender ATP |
| SIEM      | Log aggregation, correlation, compliance reporting                         | Splunk, LogRhythm                      |
| IDS       | Network intrusion detection, alerts                                        | Snort, Suricata                        |
| IPS       | Intrusion prevention (blocking)                                            | Cisco Firepower, Snort (inline mode)   |
| Honeypot  | Deception, attack data collection                                          | Cowrie, Dionaea, Honeyd                |

**Honeypot**  
A decoy system or service designed to appear vulnerable and attractive to attackers. It lures malicious traffic away from real assets and logs attacker behavior for analysis.  

- **How It Works:**  
  1. Deploy a fake server or application with intentionally exposed “vulnerabilities.”  
  2. Monitor all interactions—any connection is likely malicious.  
  3. Collect logs of attack tools, methods, and payloads.  

- **Types:**  
  - **Low-Interaction:** Simulates basic services (e.g., SSH, HTTP) with limited functionality.  
  - **High-Interaction:** Runs real services or full OS instances, giving deeper insight but higher risk.  

- **Famous Examples:**  
  - **Cowrie:** SSH/Telnet honeypot that logs brute-force attempts and commands.  
  - **Dionaea:** Emulates multiple protocols (SMB, FTP) to capture malware.  
  - **Honeyd:** Customizable virtual honeypots mimicking entire networks.  

- **Uses:**  
  - Early warning of attacks  
  - Malware capture and analysis  
  - Understanding attacker techniques  
  - Improving IDS/IPS rules  

### Honeypot Deployment
- **Low-interaction:** simple service emulation (Dionaea, Honeyd)  
- **High-interaction:** full VM/container, richer intel  
- Best practices: isolation, logging, traffic analysis, legal compliance  

**Example Stats:**  
- 40,382 alerts per 60s  
- 1,453,151 alerts per hour  
- 40,639,802 alerts per day  

## 7. Email Security & Authentication

### Business Email Compromise (BEC)
Business Email Compromise attacks have grown more sophisticated, leveraging AI-generated text, highly targeted phishing campaigns, and domain-spoofing to trick employees into wiring funds or disclosing sensitive data. In a notable case, Norfund fell victim when attackers spoofed a COVID-19-related email from a trusted partner, resulting in a significant fraudulent wire transfer.

### Common Misconfigurations
- Missing SMTP AUTH → Open relay
- No policy enforcement → Messages failing SPF/DKIM still delivered

### Common Misconfigurations
- Missing SMTP AUTH → open relay  
- No policy enforcement  

### Email Authentication

1. **SMTPS / STARTTLS**  – encrypt transport (port 465 or 587)
- Encrypts the SMTP session to prevent eavesdropping
- SMTPS uses port 465; STARTTLS upgrades an existing connection on port 587

**1. SMTPS/STARTTLS** 

**2. SPF** – DNS TXT allows authorized senders 
```bash 
v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all
example.com. TXT "v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all"
```

**3. DKIM** – domain-key signature  
```bash
mail._domainkey.example.com TXT "v=DKIM1; k=rsa; p=MIGfMA0GCS..."
```

**4. DMARC (Domain-based Message Authentication, Reporting & Conformance)**  – policy enforcement & reporting  
```bash
v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@example.com; sp=reject; adkim=s; aspf=s
- `p=`: none/quarantine/reject  
- `rua=`: aggregate report URI  
- `adkim=/aspf=`: relaxed (r) or strict (s) alignment  
```

**DMARC Flow:** Receive → SPF/DKIM → Alignment → Apply policy → Report

## 8. SSH Tunneling & Pivoting

### SOCKS Proxy for Pentests
- `ssh -D 9999 user@jumphost` – dynamic port forward  
- Burp Suite → Options → SOCKS Proxy → 127.0.0.1:9999  

### Architecture
[Tester] → SOCKS Tunnel → [Jump Host] → [Target LAN]

### Advanced Techniques
- ProxyChains for chaining multiple proxies
- SSH local forwarding: ssh -L local_port:host:port user@jumphost
- SSH remote forwarding: ssh -R remote_port:host:port user@jumphost
- Pivoting tools: Metasploit’s autoroute, Chisel port forwarding

### Detection & Controls
- Monitor long SSH sessions, data volume  
- SSH config: `AllowTcpForwarding no`, `GatewayPorts no`  
- SIEM/IDS rules for anomalous SSH use  

**What is SSH tunneling and is it the same as a VPN?**  
SSH tunneling encapsulates specific TCP connections (or dynamic SOCKS) through an encrypted SSH session, enabling access to internal resources. A VPN creates a virtual network interface and routes all (or selected) IP traffic across an encrypted tunnel. While both provide secure remote access, SSH tunnels forward individual ports or SOCKS, whereas VPNs operate at the network layer to route entire subnets transparently.  

| Feature                       | SSH Tunneling                                        | VPN                                                      |
|-------------------------------|------------------------------------------------------|----------------------------------------------------------|
| Layer                         | Application (TCP ports or SOCKS proxy)               | Network (virtual network interface, all IP traffic)      |
| Scope of Traffic             | Individual ports or dynamic SOCKS sessions            | Entire subnets or selected networks                      |
| Setup Complexity             | Simple SSH command                                     | Requires VPN client/server, certificates or PSK         |
| Encryption                   | Encrypted via SSH (AES, etc.)                         | Encrypted via IPsec/OpenVPN (AES, etc.)                 |
| Authentication               | SSH keys or password                                  | Certificates, pre-shared keys, username/password        |
| Transparent Routing          | Manual port/proxy configuration                       | Transparent routing of all traffic through VPN tunnel   |
| Multi-hop Chaining           | ProxyChains, manual chaining                          | Typically single VPN connection, multi-site via hubs    |
| Use Cases                     | Pentesting, ad-hoc remote port access                 | Site-to-site connectivity, secure remote worker access  |
| Performance Impact           | Minimal for tunneled ports; manual scaling             | Depends on VPN protocol and MTU; can route large volumes |
| Detection & Control          | SSH session monitoring, SSHD config                    | VPN gateway logs, network segmentation, firewall rules  |sss

## 9. Key Takeaways for 2025

- DDoS & BEC attacks are increasingly stealthy (AI, L7 floods, advanced phishing)  
- True defense-in-depth: EDR + SIEM + IDS/IPS + honeypots + robust processes  
- Automation (SOAR, threat intel, behavioral analytics) is essential  
- Zero-trust & compliance-driven security mandatory for critical sectors  
- Mastery of nmap, SSH tunneling, and email auth forms the technical foundation  

## Practical Commands & Examples

### nmap Flags
```bash
nmap -Pn -sV -p- -iL hosts.txt -oX output.xml
nmap --top-ports 500 192.168.1.0/24
nmap -sS -D RND:10 -T2 -f --source-port 53 target.com
```

### DNS Record Checks
```bash
dig TXT example.com # SPF
dig TXT mail._domainkey.example.com +short # DKIM
dig TXT _dmarc.example.com # DMARC

### Honeypot Examples
docker run -p 8022:8022 honeytrap/honeytrap:latest
ssh -p 8022 root@127.0.0.1

### Traffic Capture
sudo tcpdump -i eth0 -nn host target.com
wireshark capture.pcap
```