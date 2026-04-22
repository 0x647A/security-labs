# CyberWomen Leaders – Training 7: Endpoint Security

## 1. Introduction and Architecture

| Key Facts | Description |
| --- | --- |
| 70% of incidents | Start from endpoint compromise (phishing, malware, ransomware, data exfiltration). |
| Cyber Kill Chain | Recon → Payload → Delivery → Exploitation → Persistence → C2 → Exfiltration. |
| Secure architecture | Stops attack escalation (network segmentation, microsegmentation). |
| Principles | **Principle of Least Privilege** and **Zero Trust** – no default trust. |
| Benchmarking | Use **CIS Benchmarks** for systems/servers/applications. |

## 2. Windows Hardening

### 2.1 Common Attack Vectors
- **Phishing (malicious macros, Follina CVE-2022-30190)**
- **Infostealers** (cookie theft, sessions, passwords)
- **Malware/Ransomware**
- **OS Features** abused by attackers: RDP, SMB, NTLM

### 2.2 VBA Macros and Defense
1. Old macros (`makro.old`) vs. new ones (`makro.365`).  
2. PowerShell malicious macro generation (`evil_macro_gen.py`) – Metasploit demonstration.  
3. **Makro.ai** – AI model prompt example for VBA code obfuscation (15 iterations).  
4. **VBA Stomping** (source code corruption) vs. **AMSI** – AV engine bypass.  

### 2.3 CVE and ATS
- **CVE-2022-30190 (Follina)** – remote RCE via **MS-MSDT** in Office (linked Sekurak article).  
- **Alternate Data Streams (ADS)** – hiding NTFS resources.  

### 2.4 Best Practices (Windows Client)

1. **Account and Password Management**  
```bash
Disable-LocalUser -Name "Guest" # disable Guest account
net accounts /minpwlen:14 /complexity:yes # strong password policy
net accounts /lockoutthreshold:3 /lockoutduration:30 /lockoutwindow:30
```

2. **System and Application Updates**  
```bash
Set-Service wuauserv -StartupType Automatic # Windows Update
winget upgrade --all # update applications
```

3. **System Security**  
```bash
Set-MpPreference -DisableRealtimeMonitoring $false # Defender AV
netsh advfirewall set allprofiles state on # Firewall
Add-MpPreference -AttackSurfaceReductionRules_Ids D4F940AB-401B-4EFC-AADC-AD5F3C50688A -AttackSurfaceReductionRules_Actions Enabled # ASR
manage-bde -on C: # BitLocker
```

4. **Monitoring and Logging**  
```bash
auditpol /set /category:* /success:enable /failure:enable
sysmon -accepteula -i sysmonconfig.xml
wevtutil qe Security /f:text /c:5
```

5. **Software Control**  
- AppLocker / SRP  
- Macro blocking GPO: *Block macros from running in Office files from the Internet*.  

6. **Network and Protocols**  
```bash
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient" -Name "EnableMulticast" –Value 0 # LLMNR off
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" –Value 1 # NLA on
New-NetFirewallRule -DisplayName "RDP Allowed IPS" -Direction Inbound -Protocol TCP -LocalPort 3389 -RemoteAddress 192.168.1.0/24 -Action Allow
```

7. **Ransomware Protection**  
```bash
Set-MpPreference -EnableControlledFolderAccess Enabled
wbadmin start backup -backupTarget:E: -include:C:
```

## 3. Linux Hardening

### 3.1 Attack Vectors
- Local/remote exploits, rootkits, infostealers
- Docker/Kubernetes containers (privileges, docker.sock, API, Insecure Images)
- Ransomware

### 3.2 Container Attacks (DEMO)
| Attack # | Technique | Key Takeaway |
| --- | --- | --- |
| 0 | **Mem DoS** (stress, /dev/urandom → netcat) | Limit resources `--memory`, `--cpu-shares`. |
| 1 | **Insecure image** (malicious Alpine + netcat) | Snyk scans, Docker Scan. |
| 2 | **Command injection in DVWA app** | Input validation, minimal ACL. |
| 3 | **Docker-in-Docker** (`--privileged`, `chroot /host`) | Forbid privileged mode. |
| 4 | **docker.sock** mount | Restrict daemon socket access. |
| 5 | **Fastest privesc** (`-v /:/host`) | Use AppArmor/SELinux/seccomp. |
| 6 | **API REST 2376** | TLS + auth, firewall. |

### 3.3 Container Defense
```bash
docker system prune # atomic cleanup
docker volume rm $(docker volume ls -q -f "dangling=true")
docker scan <image> # Docker Scan
snyk container test <image> --severity-threshold=high
docker run -it -m 500M --kernel-memory 50M --cpu-shares 512 ...
```

### 3.4 Best Practices (Linux Host)

1. **Accounts and Passwords**  
```bash
sudo usermod -L <user> # lock account
sudo sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS 90/' /etc/login.defs

2. **Updates**  
```bash
sudo apt update && sudo apt upgrade -y
sudo unattended-upgrades # automatic patches
```

3. **Firewall (UFW/Firewalld)**  
```bash
sudo ufw default deny incoming
sudo ufw allow 22/tcp
```

4. **Audit & Logs** (`auditd`, Syslog, SIEM).

5. **File Integrity** – AIDE/Tripwire.

6. **Services/Protocols** – disable unnecessary, `PermitRootLogin no`, IPv6 off if unneeded.

7. **Network Stack** (`/etc/sysctl.conf`)  
```bash
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.tcp_syncookies = 1
```

8. **Access Control** – AppArmor (Ubuntu), SELinux (RHEL).  

9. **Backups** – encrypted, offline; recovery tests.

10. **Rootkits** – `chkrootkit`, `rkhunter`.  

## 4. AV, EDR, XDR, SIEM, DLP

### 4.1 Antivirus (AV)
- Prevention + malware removal.  
- **On-Access Scan** – Minifilter → kernel hooks (`PsSetCreateProcessNotifyRoutineEx` etc.).  
- **AMSI** – script analysis (PowerShell, JS, VBA).  
- Detection: signatures, fuzzy hash, YARA, API sequence heuristics, ML (n-grams), sandbox.

### 4.2 EDR
- **Sensor:** driver (kernel) + agent (user-mode).  
- Collected data: processes (pid, ppid, hash, signer), network (dst IP, DNS, JA3), memory (RWX alloc).  
- Responses: host isolation, kill process, quarantine, rollback, live-response.  
- **Sigma** rule example (Word → PowerShell encoded, rare DNS → high alert).

### 4.3 XDR
- Multi-domain correlation: EDR + NDR/IDS + email + IdP + SaaS + DLP + Proxy + Cloud.  
- Engine builds graph: User ↔ Device ↔ File ↔ Process ↔ Cloud.  
- Automation: account blocking, OAuth consent revocation, host isolation, mail retraction.

### 4.4 SIEM
- Central logging, correlation, anomaly detection.  
- **Wazuh** (open-source) – HIDS, FIM, vuln detector, eBPF, CTI; Intune integration, AWS Security Hub.

### 4.5 Data Loss Prevention (DLP)
1. **Lifecycle:** identification → classification → rules → monitoring → response → compliance.  
2. Data in motion (HTTP/HTTPS, mail, FTP), at rest (disks, cloud), in use (print, USB, screenshot).  
3. Response: blocking, encryption, masking, alerts.  
4. Integrations: SIEM, CASB, MDM, email gateway, endpoint security.  
5. OSS examples: MyDLP, OpenDLP, USBGuard, YARA/Trivy for scans.

## 5. Patch Management

| Stage | Best Practices |
| --- | --- |
| Inventory | Complete list of systems/applications/versions. |
| Prioritization | CVSS ≥ 9 with "in the wild" exploits first. |
| Testing | QA environment before production. |
| Automation | WSUS, SCCM, Intune, Ansible, cron. |
| Service Windows | Planned downtime, rollback plan. |
| Monitoring & Audit | Installation verification, version logging. |

### 5.1 Windows
```bash
Get-WindowsUpdate
wuauclt /detectnow; wuauclt /updatenow
usoclient StartScan / StartDownload / StartInstall
Get-HotFix | Sort-Object InstalledOn -Descending
```

### 5.2 Linux
```bash
sudo apt update && sudo apt upgrade -y
sudo yum update --security -y
sudo unattended-upgrades
dpkg -l | grep <pkg> # verification
```

**Best time for updates:** *"Yesterday"*  
Statistics (slide 108): Most companies update during 5:00 PM-12:00 AM or 12:00 AM-9:00 AM, mostly on weekends.

## 6. BYOD (Bring Your Own Device)

### 6.1 Risks
- Data leaks from personal devices, lack of patches/AV, device loss, lack of user control.

### 6.2 Minimum Technical Requirements
- Current OS, AV/EDR, disk encryption (BitLocker/FileVault/LUKS), screen lock + MFA, MDM container, no root/jailbreak, corporate security agent.

### 6.3 BYOD Declaration (Template)
1. Consent to install corporate security software and remote wipe.  
2. Incident reporting obligation ≤ 24h.  
3. Company's right to block/disconnect device.  
4. Employer liability exclusion for private data after security actions.

### 6.4 Process
Application → IT audit → security installation → declaration signing → 6-month checks → incident isolation procedure.

## 7. Ransomware

1. **Attack phases:** phishing → unpack/exec → C2 (public key download) → encryption → ransom note.  
2. **Types:** Crypto-, Locker-, Scareware, Extortionware, Wiper, Ransomware-as-a-Service.  
3. **Defense:**  
   - Offline/immutable backups, restore testing.  
   - Controlled Folder Access, ASR, blocked macros, regular browser/plugin patching.  
   - Monitor unusual file changes (`Register-WmiEvent … CIM_DataFile`).  

## 8. Summary – Key Recommendations

1. **Zero Trust + Least Privilege**: every identity, device, and application is potentially malicious.  
2. **Hardening > Detection > Response**: remove unnecessary services and privileges before installing MDR tools.  
3. **Fast patching**: "yesterday" – critical CVE first priority.  
4. **Defense-in-Depth**: AV + EDR + NDR + SIEM + DLP + Backup.  
5. **Containers**: "least privileged containers" principle, SCA scans (Snyk), seccomp/AppArmor restrictions.  
6. **BYOD**: clear policy, MDM/EDR enforcement, remote wipe rights.  
7. **Ransomware**: offline backup, network segmentation, recovery tests, user awareness.
