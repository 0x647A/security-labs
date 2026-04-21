# DFIR Essential Commands Cheat Sheet

## File System Forensics Commands

### Disk Imaging with dd

```bash
# Create disk image with progress
dd if=/dev/sdX of=/path/to/image.dd bs=64K conv=noerror,sync status=progress

# Create compressed image
dd if=/dev/sdX bs=64K conv=noerror,sync | gzip > image.dd.gz

# Verify image integrity
md5sum /dev/sdX
md5sum image.dd
sha256sum image.dd
```

### The Sleuth Kit Commands
```bash
# Display partition table
mmls disk.dd

# List files in filesystem
fls -r -m / disk.dd

# Get filesystem statistics
fsstat disk.dd

# Extract file by inode
icat disk.dd 12345 > recovered_file.txt

# Timeline creation
fls -r -m / disk.dd > body_file.txt
mactime -b body_file.txt -d > timeline.csv
```

### File Analysis
```bash
# File type identification
file suspicious_file.exe
file -i document.pdf

# Extract strings from binary
strings -n 8 malware.exe
strings -e l -n 8 malware.exe  # Unicode strings

# Calculate file hashes
md5sum file.txt
sha1sum file.txt
sha256sum file.txt

# Base64 encoding/decoding
base64 file.txt
base64 -d encoded_file.txt
```
### YARA Rules
```bash
# Scan file with YARA rule
yara rule.yar file_to_scan.exe

# Scan directory recursively
yara -r rule.yar /path/to/directory/

# Multiple rules
yara rules_directory/ target_file.exe
```
## Memory Forensics Commands
### Memory Acquisition
```bash
# Linux memory acquisition with AVML
sudo ./avml memory_dump.lime

# Using LiME (Linux Memory Extractor)
sudo insmod lime.ko "path=/tmp/memory.lime format=raw"

# Windows - using DumpIt (GUI tool)
# or Winpmem for command line
```

### Volatility Framework
```bash
# Determine OS profile (Volatility 2.x)
volatility -f memory.dmp imageinfo

# Process list
volatility -f memory.dmp --profile=Win7SP1x64 pslist
volatility -f memory.dmp --profile=Win7SP1x64 pstree

# Network connections
volatility -f memory.dmp --profile=Win7SP1x64 netscan
volatility -f memory.dmp --profile=Win7SP1x64 netstat

# Command history
volatility -f memory.dmp --profile=Win7SP1x64 consoles
volatility -f memory.dmp --profile=Win7SP1x64 cmdscan

# Dump process memory
volatility -f memory.dmp --profile=Win7SP1x64 procdump -p 1234 -D output/

# Registry analysis
volatility -f memory.dmp --profile=Win7SP1x64 hivelist
volatility -f memory.dmp --profile=Win7SP1x64 printkey -K "Software\Microsoft\Windows\CurrentVersion\Run"

# Malware detection
volatility -f memory.dmp --profile=Win7SP1x64 malfind
volatility -f memory.dmp --profile=Win7SP1x64 apihooks
```

### Volatility 3 Commands
```bash
# List available plugins
python3 vol.py -h
# Process list
python3 vol.py -f memory.dmp windows.pslist
python3 vol.py -f memory.dmp windows.pstree
# Network connections
python3 vol.py -f memory.dmp windows.netstat
# Command line history
python3 vol.py -f memory.dmp windows.cmdline
```

## Network Forensics Commands

### PCAP Analysis with tcpdump
```bash
# Basic packet capture
tcpdump -i eth0 -w capture.pcap
# Read PCAP file
tcpdump -r capture.pcap
# Filter by host
tcpdump -r capture.pcap host 192.168.1.100
# Filter by port
tcpdump -r capture.pcap port 80
# HTTP traffic only
tcpdump -r capture.pcap 'port 80 or port 443'
# Extract specific timeframe
tcpdump -r capture.pcap -w filtered.pcap host 192.168.1.100
# Display packet contents
tcpdump -r capture.pcap -X -s 0
```

### Wireshark/tshark Commands
```bash
# Basic tshark usage
tshark -r capture.pcap
# Extract specific fields
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.port
# Filter HTTP traffic
tshark -r capture.pcap -Y "http"
-T fields -e http.host -e http.request.uri
# Extract HTTP objects
tshark -r capture.pcap --export-objects http,/output/directory/
# Statistics
tshark -r capture.pcap -q -z conv,ip
tshark -r capture.pcap -q -z http,tree
```

### PCAP File Manipulation
```bash
# Get PCAP file information
capinfos capture.pcap
# Split PCAP by time
editcap -A "2023-01-01 00:00:00"
# Merge PCAP files
mergecap file1.pcap file2.pcap -w merged.pcap
# Split PCAP by size
editcap -c 1000 large_capture.pcap split_
```

### Zeek(Bro) Analysis
```bash
# Process PCAP with Zeek
zeek -r capture.pcap
# Extract specific logs
zeek -r capture.pcap protocols/http/
# Custom scripts
zeek -r capture.pcap custom_script.zeek
```

## Log Analysis Commands

### Basic Text Processing
```bash
# View log files
cat access.log
less access.log
tail -f access.log head -100 access.log
# Follow log in real-time
# Count lines in log
wc -l access.log
# Search in logs
grep "ERROR" application.log
grep -i "failed" /var/log/auth.log # Case insensitive
grep -v "INFO" application.log # Exclude INFO messages
```

### Advanced Log Analysis
```bash 
# Extract unique IP addresses
cat access.log | cut -d' '
-f1 | sort | uniq -c | sort -nr
# Top 10 most frequent IPs
cat access.log | cut -d' '
-f1 | sort | uniq -c | sort -nr | head -10
# Failed login attempts
grep "Failed password" /var/log/auth.log | cut -d' '
-f1-3,9-11
# Extract specific fields with awk
awk '{print $1, $4, $7}' access.log
# Date range filtering
sed -n '/Jan 01/,/Jan 31/p' access.log
# Statistical analysis
cat access.log | cut -d' ' -f9 | sort | uniq -c | sort -nr # HTTP status codes
```

### Regular Expression for Logs
```bash
# IP addresses
grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log
# Email addresses
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' mail.log
# URLs
grep -E 'https?://[^ ]+' access.log
# Hash values (MD5)
grep -E '[a-f0-9]{32}' malware.log
```

### Specialized Log Tools
```bash
# GoAccess for web log analysis
goaccess access.log --log-format=COMBINED -o report.html
# AWStats configuration and run
# Edit /etc/awstats/awstats.conf first
awstats.pl -config=website -update
# Log rotation and compression
logrotate /etc/logrotate.conf
```

## System Investigation Commands

### Process Analysis
```bash
# Running processes
ps aux
ps -ef
pstree
# Process information
lsof -p 1234 # Files opened by process
netstat -tulnp # Network connections with processes
ss -tulnp # Modern alternative to netstat
```

### System information
```bash
# System details
uname -a
hostnamectl
cat /etc/os-release
# Users and authentication
who
last
lastlog
cat /etc/passwd
cat /etc/shadow (with appropriate permissions)
# Scheduled tasks
crontab -l # User crontabs
cat /etc/crontab # System crontab
ls /etc/cron.* # Cron directories
```

### File System Investigation
```bash
# Find recently modified files
find /home -type f -mtime -7 # Modified in last 7 days
find /tmp -type f -atime -1 # Accessed in last 24 hours
# Find files by size
find / -type f -size +100M # Files larger than 100MB
# Find SUID/SGID files
find / -perm -4000 -type f # SUID files
find / -perm -2000 -type f # SGID files
# Check file permissions and ownership
ls -la /suspicious/directory/
stat filename.txt
# Disk usage analysis
du -sh /var/log/*
df -h
```

### Network Investigation
```bash
# Network configuration
ip addr show
ip route show
cat /etc/hosts
cat /etc/resolv.conf
# Active connections
netstat -antup
ss -antup
lsof -i
# Firewall rules
iptables -L -n -v
ufw status verbose
```

## Incident Response Automation

### Quick Triage Script
```bash
#!/bin/bash
# Quick system triage
echo "
=== System Information ===
uname -a >> triage.txt
date >> triage.txt
echo -e "\n=== Running Processes ===
ps aux >> triage.txt
" > triage.txt
" >> triage.txt
echo -e "\n=== Network Connections ===
" >> triage.txt
netstat -antup >> triage.txt
echo -e "\n=== Recently Modified Files ===
" >> triage.txt
find /home -type f -mtime -1 >> triage.txt
echo -e "\n=== Login History ===
" >> triage.txt
last >> triage.txt
```

### Hash Calculation for Evidence
```bash
#!/bin/bash
# Calculate multiple hashes for evidence files
FILE=$1
echo "File: $FILE"
echo "MD5: $(md5sum $FILE | cut -d' ' -f1)"
echo "SHA1: $(sha1sum $FILE | cut -d' ' -f1)"
echo "SHA256: $(sha256sum $FILE | cut -d' ' -f1)"
```

### Log Analysis Automation
```bash
#!/bin/bash
# Automated suspicious activity detection
LOG_FILE=$1
echo "=== Top Source IPs ==="
cat $LOG_FILE | cut -d' ' -f1 | sort | uniq -c | sort -nr | head -10
echo -e "\n=== Failed Requests ==="
grep " 40[0-9] " $LOG_FILE | wc -l
echo -e "\n=== Suspicious User Agents ==="
grep -i "bot\|crawler\|scanner" $LOG_FILE | cut -d'"' -f6 | sort | uniq -c
```

### Essential One-Liners
```bash
# Find all executable files in user directories
find /home -type f -executable -not -path "*/.*" 2>/dev/null
# Monitor file changes in real-time
inotifywait -m -r /important/directory -e modify,create,delete
# Extract compressed logs and search
zgrep "ERROR" /var/log/syslog.*.gz
# Network traffic summary
tcpdump -r capture.pcap -nn | awk '{print $3}' | sort | uniq -c | sort -nr
# Memory strings analysis
strings memory.dump | grep -E "(http|ftp|password|user)" > interesting_strings.txt
# Quick malware hash check (with known bad hash list)
md5sum suspicious_file.exe | cut -d' ' -f1 | grep -f known_bad_hashes.txt
```
