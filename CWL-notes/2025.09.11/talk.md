# CyberWomen Leaders – Training 10: Incident Analysis and Digital Forensics (DFIR)

## DFIR Fundamentals – Digital Forensics and Incident Response

### Cyber Kill Chain
Presents attack stages:
- Reconnaissance
- Delivery
- Weaponization
- Exploitation
- Installation (persistence)
- C&C (command and control)
- Data exfiltration and other final actions

Each stage requires separate detection measures and post-breach analysis. In practice, the kill chain is additionally divided into actions like: Initial Access, Discovery, Credential Access, Persistence, Data Exfiltration, where log collection and dumps should begin as early as possible, always prioritizing intelligence and quick access to evidence.

#### Tools Used at Individual Stages (Linux/Windows)

**System Discovery & Reconnaissance:**
- System commands: `whoami` (user context identification), `ss`/`netstat` (network connection enumeration), `ps` (process listing), `ip a` (network interface discovery)
- Cross-platform tools: `systeminfo` (Windows), `uname -a` (Linux), `hostname`, `id`, `groups`
- Network discovery: `nmap`, `arp -a`, `route`, `ifconfig`/`ipconfig`

**Credential Access & Privilege Escalation:**
- **Windows**: Mimikatz (memory credential extraction), Kerberoasting tools, SAM/LSA dumping utilities
- **Linux**: Mimipenguin (cleartext password extraction from memory), `/proc` filesystem analysis, swap file analysis with `swap_digger`
- **Cross-platform**: Volatility framework for memory analysis, credential harvesting from browser storage, SSH key extraction
- **Post-exploitation**: Token manipulation, credential reuse attacks, pass-the-hash/pass-the-ticket techniques

**Data Collection & Exfiltration:**
- **Network transfer**: `nc` (netcat for backdoor channels), `scp` (secure file transfer), `rsync` (efficient synchronization), `wget`/`curl` (HTTP-based downloads)
- **Compression & encryption**: `7z`, `gzip`, `openssl enc` for data preparation
- **Covert channels**: DNS tunneling, ICMP exfiltration, steganographic methods
- **Cloud storage**: Direct uploads to cloud services, temporary file hosting services

**Log Analysis & Evidence Review:**
- **Linux**: `logwatch` (automated log summarization), `rsyslog` analysis, `journalctl` (systemd logs), `goaccess` (web log analysis)
- **Windows**: PowerShell cmdlets (`Get-EventLog`, `Get-WinEvent`), Event Viewer analysis, `logparser` (Microsoft Log Parser)
- **Cross-platform**: ELK Stack (Elasticsearch, Logstash, Kibana) for centralized log management, Graylog for enterprise log aggregation
- **SIEM platforms**: Splunk, Wazuh, OSSEC for real-time monitoring and correlation

**Persistence & Lateral Movement:**
- **Service installation**: `systemd` payloads (Linux), Windows services, scheduled tasks
- **Network persistence**: SSH backdoors, RDP modifications, WMI event subscriptions
- **File system**: Hidden executables, configuration modifications, startup script alterations

Each tool category serves specific phases of both offensive operations and defensive analysis, with platform-specific implementations reflecting the underlying operating system architectures and security models.

### Standards and Procedures in DFIR

#### Key Standards and Documents:
- **ISO/IEC 27035** – Incident response principles and guidelines providing comprehensive framework for managing security incidents
- **ISO/IEC 27037** – Evidence identification, collection, and preservation standards ensuring legal admissibility and forensic integrity
- **NIST SP 800-86** – Digital forensics guidelines covering technical and procedural aspects of computer forensics investigations
- **RFC 3227** – Digital evidence collection procedures defining best practices for evidence handling and documentation
- **Implementation considerations**: Organizational procedures integration, process automation using specialized distributions (TSURUGI Linux), utilization of advanced containerized environments (Security Onion), compliance with national frameworks (PB, SZBI, IZSI)

#### Incident Documentation Requirements:
- Detection date and incident status tracking
- Status change timestamps and closure dates
- Detailed incident descriptions and impact assessments
- Actions taken documentation with responsible personnel identification
- Risk analysis updates and remediation recommendations
- Periodic review and lessons learned integration

## Filesystem Forensics – Digital Forensics on File Systems

### Core Imaging and Acquisition Tools:
- **dd, FTK Imager** – Bit-for-bit disk imaging with verification capabilities, supporting both physical and logical acquisitions
- **Write blockers** – Hardware/software protection preventing target drive modifications during acquisition
- **Hash verification** – Integrity validation using md5sum, sha256sum for evidence authenticity

### Analysis and Investigation Tools:
- **Sleuth Kit / Autopsy** – Comprehensive filesystem analysis suite featuring:
  - Timeline creation and analysis (fls, mactime)
  - Partition analysis (mmls) and filesystem statistics (fsstat)
  - File extraction and metadata examination (icat, ils)
  - Deleted file recovery and slack space analysis
- **testdisk, foremost, ext4magic** – Specialized recovery tools for:
  - Filesystem reconstruction after corruption or attacks
  - File carving from unallocated space
  - Partition table recovery and repair

### Security Assessment Tools:
- **AIDE (Advanced Intrusion Detection Environment)** – File integrity monitoring detecting unauthorized system modifications
- **rkhunter** – Rootkit detection scanning for known malicious signatures and suspicious system changes
- **OSForensics** – Advanced Windows-focused analysis platform with registry examination and application artifact analysis

### YARA Integration:
- **Malware detection rules** – Custom signatures for identifying malicious executables and suspicious patterns
    - Enable classification and detection of malicious software at file level, using characteristic byte sequences or text patterns (e.g., "sekurak.pl")
    - Automate analysis of infected files, important for detecting malware variants in archives and system images
- **File classification** – Automated categorization of discovered files based on content analysis
- **Threat intelligence integration** – Correlation with known indicators of compromise (IoCs)

### Best Practices:
- **Read-only acquisition** – Preventing evidence contamination through write-protected imaging
- **Chain of custody** – Detailed documentation of evidence handling and transfer
- **Baseline comparison** – Establishing known-good system states for change detection
- **Cross-platform compatibility** – Tools supporting multiple filesystem types (NTFS, ext4, HFS+, etc.)

### Key Recommendations:
- Secure image integrity (work on copies, not originals)
- Don't restore files to source without verification
- Develop forensic automation, but remember the need for manual audit before overwriting evidence or automatic case closure

## Memory Forensics – RAM Dump Analysis

### Memory Acquisition Tools:
- **Windows**: Procdump (Microsoft Sysinternals), DumpIt (MoonSols), WinPmem (Google Rekall) for complete physical memory capture
- **Linux**: LiME (Linux Memory Extractor), AVML (Azure Virtual Machine Extractor), fmem kernel module for live memory acquisition
- **Cross-platform**: Volatility Framework with built-in acquisition capabilities for various operating systems

### Analysis Framework - Volatility:
- **Volatility 2.x & 3.x** – Premier memory analysis framework supporting Windows, Linux, and macOS memory dumps
- **Process analysis**: pslist (running processes), pstree (process hierarchy), psaux (detailed process information)
- **Network artifacts**: netstat (network connections), netscan (comprehensive network analysis), connscan (connection scanning)
- **System artifacts**: hivelist (registry hives), printkey (registry key analysis), filescan (file object enumeration)
- **Malware detection**: malfind (injected code detection), apihooks (API hook analysis), check_syscall (system call integrity)
- **Command history**: cmdscan (command line history), consoles (console command extraction)

### Kernel Symbol Management:
- **DWARF (Debugging With Attributed Record Formats)** – Debug symbol format for Linux kernel analysis
- **ISF (Intermediate Symbol Format)** – Volatility 3 symbol format for enhanced cross-platform support
- **Profile creation**: Building custom profiles for specific kernel versions and configurations
- **System.map integration**: Kernel symbol mapping for accurate memory structure interpretation

### Critical Procedures:
- **Incident preservation rule**: Never restart or power down the compromised system during active investigation
- **Live acquisition priority**: Capture volatile memory before any other forensic procedures
- **Timeline correlation**: Integrate memory artifacts with filesystem timestamps and network logs
- **Chain of custody**: Document memory acquisition process, tools used, and hash verification
- **Artifact validation**: Cross-reference memory findings with disk-based evidence and log analysis

### Supporting Analysis Tools:
- **hexdump/xxd**: Raw memory content examination for manual analysis and pattern identification
- **strings**: Extract printable character sequences from memory dumps (ASCII/Unicode support)
- **Hashing utilities**: md5sum, sha256sum for memory dump integrity verification
- **Encoding tools**: base64 decoding for obfuscated content analysis within memory structures

### Advanced Techniques:
- **Rootkit detection**: Analyzing system call tables, interrupt descriptor tables, and kernel object manipulation
- **Process injection analysis**: Identifying code injection, DLL injection, and process hollowing techniques
- **Credential extraction**: Recovering plaintext passwords, Kerberos tickets, and authentication tokens from memory
- **Malware unpacking**: Extracting packed/encrypted malware from memory after runtime decryption

## Network Forensics – Digital Forensics in Computer Networks

### Core Network Analysis Challenges:
- **Full packet capture (PCAP) analysis** – Requires massive storage infrastructure, generates comprehensive attack vectors but creates significant noise requiring intelligent filtering
- **Storage optimization strategies** – Implementing retention policies, data lifecycle management, and automated purging of non-critical traffic
- **Effective filtering methodologies** – Utilizing advanced tools for indexing, temporal segmentation, and intelligent traffic categorization (capinfos for metadata analysis, editcap for precise temporal extraction)
- **Real-time vs retrospective analysis** – Balancing immediate threat detection with comprehensive historical investigation capabilities

### Detection and Monitoring Systems:
- **Intrusion Detection/Prevention (IDS/IPS)** – Advanced threat detection using signature-based (Snort) and behavioral analysis (Suricata) engines
- **Network behavior analysis** – Zeek (formerly Bro) for deep protocol inspection, connection logging, and anomaly detection
- **Active endpoint monitoring** – Real-time surveillance of critical network segments and high-value assets
- **Alert correlation and prioritization** – Reducing false positives through multi-layered validation and threat intelligence integration

### Multi-Source Data Correlation Framework:
- **Proxy server logs** – HTTP/HTTPS request analysis, user agent profiling, URL categorization, and bandwidth utilization patterns
- **DNS resolution data** – Query analysis, malicious domain detection, DNS tunneling identification, and resolution timing analysis  
- **DHCP lease information** – IP address assignment tracking, device identification, and network segmentation analysis
- **IDS/Antivirus alerts** – Threat signature matching, behavioral anomaly detection, and malware family classification
- **Memory/disk dumps** – Process analysis, network connection artifacts, and persistent threat indicators
- **Attack vector reconstruction** – Source identification, target analysis, attack path mapping, file hash correlation, and command & control domain association

### SIEM Architecture and Integration:
- **Centralized log management** – Wazuh for comprehensive security event correlation and automated response
- **Containerized security stack** – Security Onion providing integrated IDS, network monitoring, and analysis capabilities
- **ELK Stack implementation** – Elasticsearch for data storage, Logstash for processing, Kibana for visualization
- **Data pipeline optimization** – Filebeat for log shipping, Redis for queuing, and Elasticsearch for indexing and search
- **Advanced analytics** – Grafana dashboards for statistical analysis, trend identification, and executive reporting
- **Automated correlation** – Machine learning-based anomaly detection and behavioral analysis

### Packet Analysis Tools and Techniques:
- **Command-line analysis** – tcpdump for efficient packet capture with Berkeley Packet Filter (BPF) syntax
- **Interactive analysis** – tshark for scriptable packet examination and automated processing
- **Graphical investigation** – Wireshark for deep protocol analysis and network troubleshooting
- **Filtering methodologies**:
  - **Capture filters** – Pre-acquisition traffic selection (e.g., `udp and host 10.0.0.1`)
  - **Display filters** – Post-capture analysis refinement (e.g., `ip.src == 10.0.0.1 && http.user_agent contains "Mozilla"`)

### PCAP File Structure and Analysis:
- **File format internals** – Magic Number identification (D4C3B2A1), version compatibility, timestamp accuracy, and datalink type recognition
- **Packet structure** – Frame length validation, actual packet size verification, and payload extraction
- **Temporal analysis** – editcap for time-based segmentation using precise timestamp ranges
- **Field extraction** – tshark output formatting for specific protocol layers and field isolation
- **Protocol reconstruction** – Layer-by-layer analysis from physical (Ethernet) to application (HTTP/DNS/SMB)

### Advanced Network Forensics Exercises:

#### Traffic Pattern Analysis:
- **Statistical profiling** – IP address frequency analysis, HTTP host correlation, and geographic distribution mapping
- **Protocol distribution** – GET vs POST method analysis, content type examination, and payload size profiling
- **Suspicious file detection** – Executable download identification (*.exe, *.dll), PE header validation (MZ signature), and hash-based malware detection
- **Timeline reconstruction** – Connection establishment patterns, data transfer volumes, and session duration analysis

#### Malware Communication Analysis:
- **Command & Control identification** – C2 server communication patterns, beacon interval analysis, and encrypted channel detection
- **Data exfiltration detection** – Abnormal upload patterns, compression algorithm identification, and covert channel analysis
- **Lateral movement tracking** – Internal network scanning, privilege escalation attempts, and credential reuse patterns
- **Persistence mechanism analysis** – Service installation network traffic, scheduled task creation, and registry modification patterns

### Practical Investigation Methodology:
1. **Initial triage** – PCAP file validation, timeframe identification, and traffic volume assessment
2. **Protocol hierarchy analysis** – Layer distribution, anomalous protocol usage, and encrypted traffic ratios
3. **Conversation analysis** – Top talkers identification, unusual communication patterns, and geographic anomalies
4. **Artifact extraction** – File carving from HTTP streams, certificate analysis, and metadata preservation
5. **Timeline correlation** – Cross-referencing with system logs, memory dumps, and filesystem timestamps
6. **Threat intelligence integration** – IoC matching, reputation scoring, and attribution analysis

## Logs Forensics – Digital Forensics in Logs

### Core Log Analysis Philosophy:
- **Manual analysis foundation** – Understanding traditional Unix text processing tools provides essential baseline skills for forensic investigation
- **Pattern recognition** – Developing expertise in identifying anomalous patterns, attack signatures, and behavioral indicators within log streams
- **Temporal correlation** – Establishing timeline relationships between events across multiple log sources for comprehensive incident reconstruction
- **Automation support** – Leveraging automated tools to augment human analysis rather than replace critical thinking and investigative intuition

### Essential Command-Line Tools:

#### Text Processing Pipeline:
- **cat/zcat** – File content display with compression support for archived logs (`.gz`, `.bz2` formats)
- **grep** – Pattern matching with advanced options:
  - `-P` (Perl-compatible RegEx) for complex pattern matching
  - `-i` (case insensitive) for flexible string searching
  - `-v` (inverse matching) for exclusion filtering
  - `-A x -B x` (context lines) for surrounding event analysis
- **cut** – Field extraction with customizable delimiters (`-d`) and field selection (`-f`) for structured log parsing
- **sort** – Data ordering with numeric (`-n`) and reverse (`-r`) options for chronological and frequency analysis
- **uniq** – Duplicate removal with occurrence counting (`-c`) for frequency analysis and statistical profiling

#### Advanced Text Manipulation:
- **sed** – Stream editing for pattern substitution and log normalization (`s/pattern1/pattern2/g`)
- **awk** – Field-based processing for complex log parsing and calculations
- **strings** – Extractable text identification with encoding options (`-e`) and minimum length filtering (`-n`)
- **wc** – Line counting (`-l`) for volume analysis and statistical baseline establishment

### System Navigation and File Analysis:
- **ls** variations:
  - `ls -lhat` – Human-readable file sizes with timestamps and hidden files
  - `ls -last` – ACL display with detailed permission analysis
- **file** – Content type identification:
  - `file -i` – MIME type detection for log format validation
  - Format verification for corrupted or misnamed log files
- **Directory navigation** – Efficient movement between log directories (`cd ~`, `cd /`, `cd ..`)

### Regular Expression Patterns for Security Analysis:
- **Character classes**: `[a-z]` (lowercase), `[A-Z]` (uppercase), `[0-9]` (digits)
- **Specific character sets**: `[axd]` (literal character matching)
- **Hash pattern detection**: `[a-f0-9]{32}` (MD5), `[a-f0-9]{40}` (SHA-1), `[a-f0-9]{64}` (SHA-256)
- **Alternation patterns**: `text1|text2` for multi-pattern matching
- **IP address extraction**: `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}`
- **Email pattern**: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`

### Practical Analysis Workflows:

#### Rapid Threat Assessment Pipeline:
- **8*Domain-based threat analysis**
```bash
cat logs.txt | grep "suspicious.domain.com" | cut -d'"' -f11 | sort | uniq -c | sort -nr | grep -v legitimate_pattern | head -5 > threat_report.txt
```
- **IP frequency analysis for botnet detection**
```bash
grep -oE '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}' access.log | sort | uniq -c | sort -nr | head -20
```
- **Failed authentication analysis**
```bash
grep "Failed password" /var/log/auth.log | cut -d' ' -f1-3,9-11 | sort | uniq -c
```

## Case Study – Ransomware Incident (Practical Analysis)

### Circumstances:
- Ransomware encrypts report on company president's desktop, filename changes to .encrypted, user doesn't know password
- Forensic analysis begins with incident time identification and IP address assignment to hostname board-2739 computer based on DHCP records and available logs
- Subsequent stages use logs from proxy server (SquidGuard, block.log), Snort and DNS to determine malicious file download source

### Investigation Procedure:
- Incident documentation: dating, status, response correctness and identification of all actions taken and responsible persons
- Network log correlation (proxy, DNS, IDS alerts), event statistical analysis, false-positive elimination through trusted address comparison
- Network traffic analysis (PCAP: capinfos, tcpdump), suspicious stream filtering, data export (TLS Stream), ransomware characteristic artifact identification
- Confirmation (or exclusion) of antivirus system detection, file hash verification
- Final analysis of collected logs and files, forensic artifact collection, recommendations and summary report for management

## Useful Tools and Sources

- Repositories and websites: Malware-Traffic-Analysis.net, ANY.RUN, VirusTotal, Malpedia, bazaar.abuse.ch
- GitHub: awesome-memory-forensics, sample memory dumps MockLabs / MemLabs, HackTheBox tools, forensic compendia
- Popular distributions: TSURUGI Linux (DFIR suite), Security Onion (deployment, SIEM)

## Key Conclusions and Best Practices
- Forensic investigation requires manual engagement, automation can be support, but never replaces expert
- Most important evidence collection points: don't overwrite, don't restart incident machines, secure artifact integrity
- Analysis and reporting facilitated by automation (SIEM, log parsers, ELK platforms), but foundation is deep understanding of CLI tools and their capabilities
- Always maintain incident documentation, follow ISO/NIST standards/recommendations, raise awareness and train IT personnel and end users

## Materials
https://securitum.ninja/shinobi