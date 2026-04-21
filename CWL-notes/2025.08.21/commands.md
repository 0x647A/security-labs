## Useful Commands and Tools

### Network Scanning  
- `nmap -sV -p 1-65535 target.com`  
  Scan open ports and service versions  
- `curl -I https://example.com`  
  Fetch HTTP response headers  
- `wget --mirror --convert-links https://example.com`  
  Mirror a website for offline analysis  

### TLS/SSL Testing  
- `openssl s_client -connect example.com:443 -tls1_2`  
  Test TLSv1.2 connectivity and certificate chain  
- `openssl x509 -in cert.pem -noout -text`  
  Display certificate details  

### SQL Injection  
- `sqlmap -u "https://example.com/item?id=1" --batch --level=5`  
  Automated SQL injection detection and exploitation  
- `sqlmap -u "https://example.com/search?q=test" --dump`  
  Dump database contents  

### XSS Testing  
- `xsser --url "https://example.com/page?param=<script>alert(1)</script>"`  
  Automated XSS testing  
- `grep -R "<script" .`  
  Search for script injection points in code  

### Dependency Vulnerability Scanning  
- `snyk test --file=package.json`  
  Scan npm dependencies for known vulnerabilities  
- `trivy image myapp:latest`  
  Scan container image for CVEs  

### Log Monitoring  
- `tail -F /var/log/nginx/access.log`  
  Follow NGINX access logs in real time  
- `grep "ERROR" /var/log/app.log | less`  
  Filter application errors in logs  

### SSRF Testing  
- `curl -v --max-time 5 --url "http://127.0.0.1:80"`  
  Test SSRF against local services  
- `python3 - <<EOF  
import ipaddress  
print(ipaddress.ip_address("127.0.0.1").is_private)  
EOF`  
  Check if an IP address is private  

### YAML/JSON Linting  
- `yamllint config.yaml`  
  Validate YAML files (CI/CD pipeline configs)  
- `jq . config.json`  
  Pretty-print and validate JSON  

### Code Security Auditing  
- `bandit -r ./src`  
  Python security analysis  
- `gosec ./...`  
  Go code security audit  
