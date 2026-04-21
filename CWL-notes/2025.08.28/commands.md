# Cheat Sheet – Cloud & Virtual Environment Security Commands

### A  
- **aws configure list** – show current AWS CLI configuration  
- **aws configure set aws_session_token <TOKEN>** – set session token for AWS CLI  

### C  
- **curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds:21600"**  
  – retrieve IMDSv2 token  
- **curl -H "X-aws-ec2-metadata-token:$TOKEN" http://169.254.169.254/latest/user-data**  
  – fetch EC2 user-data  

### D  
- **docker run -it --rm subfinder -d <domain>** – run Subfinder in Docker for subdomain discovery  

### E  
- **egress filtering** – implemented via security group or NACL rules to block unwanted outbound traffic  

### F  
- **ffuf -w /path/to/wordlist -u http://<host>/FUZZ** – directory fuzzing for hidden resources  

### G  
- **gcloud compute instances list** – list GCP VM instances  
- **gowitness file -f domains.txt** – take screenshots of domains in file  
- **gowitness report serve --address :7171** – serve gowitness report on port 7171  

### I  
- **iptables -A OUTPUT -d 169.254.169.254 -m owner --uid-owner root -j ACCEPT** – allow IMDS requests for root  
- **iptables -A OUTPUT -d 169.254.169.254 -j DROP** – block IMDS requests for non-root  

### M  
- **masscan -p 80,443 192.168.0.0/24** – scan TCP ports 80 and 443  
- **masscan -p- 192.168.0.1 --rate 250000** – scan all ports with rate limit  
- **masscan -p U:123,U:53 192.168.0.1** – UDP port scan for ports 123 and 53  

### N  
- **nmap -sn 10.0.0.0/24** – ping scan to identify hosts  
- **nmap -Pn 10.0.0.0/24** – skip host discovery, assume hosts are up  
- **nmap -sT -p- 10.10.1.99 -sV** – TCP connect scan all ports and service version detection  
- **nmap -iL list.txt -p80,443** – scan listed hosts on ports 80 and 443  
- **nmap -oA allformats 192.168.1.2 -p22** – output in three formats for port 22  

### R  
- **rest** – use HTTP methods (GET, POST, PUT, DELETE) for API interactions  

### S  
- **ssh -i ~/.ssh/id_ed25519 -D 9999 user@bastion.example.com** – create SOCKS proxy on port 9999  
- **subfinder -d <domain>** – discover subdomains using Subfinder CLI  

### U  
- **update** – apply security patches to cloud components via provider console or CLI  

### V  
- **aws ec2 describe-instances** – list AWS EC2 instances  
- **az vm list** – list Azure VMs  

### W  
- **webhook.site** – capture and inspect HTTP requests for testing webhooks  
