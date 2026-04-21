### A
- **ACL:** Access Control List — rules on routers/firewalls permitting or denying traffic by IP, protocol, port.  
- **Amplification Attack:** DDoS technique where small spoofed request to UDP service (DNS/NTP) triggers large response to victim.  
- **ARP Spoofing:** Data-link-layer attack forging ARP replies to intercept or redirect LAN traffic.  
- **Asset:** Any valuable resource to an organization (data, systems, reputation).

### B
- **BEC:** Business Email Compromise — targeted social-engineering email scams to defraud organizations.  
- **Behavioral Analysis:** Detecting threats by monitoring user or network anomalies instead of static signatures.  
- **BIMI:** Brand Indicators for Message Identification — email standard displaying brand logos when DMARC enforced.  
- **Burp Suite:** Web security testing proxy with modules (Proxy, Intruder, Repeater, Scanner).

### C
- **Chisel:** SSH-secured TCP/UDP tunnel over HTTP for pivoting in pentests.  
- **Connect Scan (-sT):** nmap scan performing full TCP three-way handshake.  
- **Cloud DDoS:** Always-on cloud-based mitigation (Cloudflare/Akamai) performing deep-packet inspection.

### D
- **DDoS:** Distributed Denial-of-Service — flood of traffic from multiple sources exhausting target resources.  
- **Decoy Scan (-D):** nmap uses multiple fake source IPs to mask true scan origin.  
- **DNS Amplification:** Spoofed DNS query causing large DNS response directed at victim.  
- **DMARC:** Domain-based Message Authentication, Reporting & Conformance — enforces SPF/DKIM policies and reporting.

### E
- **EDR:** Endpoint Detection & Response — endpoint software for threat hunting, behavioral monitoring, sandboxing.  

### F
- **Flow Control:** TCP mechanism regulating data transmission to prevent congestion.  
- **FIN/XMAS/NULL Scans:** nmap stealth scans sending FIN only, all flags, or no flags to probe port state.  
- **Firewall (Packet Filtering):** Blocks or allows IP packets based on header attributes (IP, port).
- **Fuzzer (ffuf/gobuster):** Tool for directory and file enumeration by brute-forcing URLs with wordlists.

### H
- **Honeypot:** Deceptive service mimicking vulnerable targets to log attacker behavior.  
- **HTTP Flood (L7 Attack):** Application-layer DDoS using GET/POST requests to exhaust server resources.

### I
- **IDS/IPS:** Intrusion Detection/Prevention Systems — IDS alerts on suspicious traffic; IPS blocks it inline.  
- **IP Spoofing:** Forging source IP addresses to bypass filters and obscure attacker identity.

### L
- **L2/L3/L4:** OSI layers 2 (Data Link), 3 (Network), 4 (Transport) for LAN frame switching, IP routing, TCP/UDP communication.  
- **Layer 7 (L7):** Application-layer attacks and filtering via HTTP, SMTP protocols.  
- **Local/Remote Port Forwarding (-L/-R):** SSH options forwarding specific ports through SSH tunnels.  
- **Logger (SIEM):** Security Information & Event Management — aggregates, correlates logs for alerts and compliance.

### M
- **MFA:** Multi-Factor Authentication — combining knowledge, possession, or biometrics for secure access.  
- **Metasploit Autoroute:** Metasploit module adding routes to compromised networks for pivoting.  
- **MTA-STS:** Mail Transfer Agent Strict Transport Security — enforces TLS for SMTP via DNS/HTTPS policy.

### N
- **nc/ncat:** Netcat utilities for raw TCP/UDP data transfer and banner grabbing.  
- **nmap:** Network scanner supporting various scan types, version detection, OS fingerprinting.  
- **Network Time Protocol (NTP):** UDP protocol often abused in amplification DDoS.

### P
- **PCAP:** Packet capture format for recording network traffic analyzable by Wireshark.  
- **Pivoting:** Using compromised host to route additional scans or traffic into target network.  
- **ProxyChains:** Tool forcing TCP connections through configurable proxy chains (SOCKS/HTTP).  
- **Python tcpdump:** CLI tool capturing live packets for analysis.

### R
- **Rate Limiting:** Restricts request volume per client/time window to mitigate application floods.  
- **Route Poisoning:** Malicious routing updates to disrupt legitimate network paths.  
- **RIP/OSPF/BGP:** Dynamic routing protocols — distance-vector (RIP), link-state (OSPF), inter-domain (BGP).

### S
- **Sandbox:** Isolated environment executing untrusted code/files for safe analysis.  
- **SIEM:** Security Information and Event Management platform for log aggregation, correlation, alerting.  
- **SMTP AUTH:** SMTP extension enabling authenticated email relay to prevent open relays.  
- **SMTPS/STARTTLS:** Encryption methods for SMTP — implicit TLS on port 465 or opportunistic TLS on 587.  
- **SYN Flood:** DDoS sending numerous SYNs without completing handshake, exhausting server backlog.  
- **SYN Scan (-sS):** nmap stealth scan sending SYNs and interpreting responses without completing handshake.  
- **SOCKS5 Proxy:** General-purpose proxy supporting TCP/UDP forwarding and DNS over the tunnel.

### T
- **TCP Flags:** Bits (SYN, ACK, FIN, RST, PSH, URG) controlling TCP session states and control messages.  
- **Three-Way Handshake:** TCP session initiation via SYN → SYN-ACK → ACK sequence.  
- **TTL:** Time-To-Live field in IP decrementing per hop to prevent routing loops.

### U
- **UDP:** Connectionless transport protocol without flow control, used by DNS, NTP, DHCP, LDAP.  
- **UDP Flood:** Volumetric DDoS exploiting lack of session control, sending many UDP packets to exhaustion.

### V
- **VLAN:** Virtual LAN segmentation within a switch to isolate broadcast domains.  
- **Vulnerability Scan:** Automated assessment of systems/services for known security flaws.

### W
- **Wireshark:** GUI packet analyzer inspecting PCAPs and live traffic for protocol-level details.
