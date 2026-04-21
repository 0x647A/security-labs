# Linux and Related Network Commands

1. `ifconfig`  
   Display or configure network interfaces on Linux.

2. `ipconfig /all`  
   Display network configuration details on Windows.

3. `tcpdump -i eth0 host sekurak.pl`  
   Capture all traffic to/from domain `sekurak.pl` on interface `eth0`.

4. `wget https://sekurak.pl`  
   Download the homepage of `sekurak.pl`.

5. `tcpdump -i eth0 host sekurak.pl -w pcap_sekurak.pcap`  
   Capture to/from `sekurak.pl` and write to `pcap_sekurak.pcap`.

6. `tcpdump -r pcap_sekurak.pcap`  
   Read and display packets from the capture file.

7. `tcpdump -r pcap_sekurak.pcap -nn`  
   Read the file without resolving IPs to names (`-nn`).

8. `tcpdump -r pcap_sekurak.pcap -nn -A`  
   Read the file (`-r`), no name resolution (`-nn`), and show packet payload (`-A`).

9. `nmap 192.111.1.0/24`  
   Scan the network for hosts and open ports.

10. `tcpdump -i eth0 host 192.222.2.22`  
    Capture traffic to/from IP `192.222.2.22` on `eth0`.

11. `nmap 192.222.2.22 -p 9000`  
    Scan port 9000 on host `192.222.2.22`.

12. `tcpdump -i eth0 host 192.222.2.22 -sU`  
    Capture UDP traffic to/from `192.222.2.22` (`-sU` for UDP).

13. `nmap -Pn -sV -p- -iL hosty.txt -oX wynik.xml`  
    Full, aggressive scan (-Pn skip ping; -sV version detect; -p- all ports) on hosts in `hosty.txt`, output XML.

14. `mkdir cap`  
    Create a directory named `cap`.

15. `mv pcap_test.pcap cap`  
    Move `pcap_test.pcap` into the `cap` directory.

16. `cd cap/`  
    Change working directory to `cap`.

17. `python3 -m http.server 8001`  
    Start a simple HTTP server on port 8001 in the current directory.

18. `nc -nv 8.8.8.8 443`  
    Connect to 8.8.8.8:443 with netcat, capture the banner.

19. `nmap 192.168.1.0/24 -sV`  
    Scan network and detect service versions (-sV grabs banners).

20. `nmap 192.168.1.0/24 -p 22 -sV`  
    Scan only port 22 across the network and detect its version.

21. `apt install ffuf`  
    Install the `ffuf` directory fuzzing tool on Debian/Ubuntu.

22. `wget https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt`  
    Download a common wordlist for fuzzing.

23. `ffuf -w common.txt -u https://sekurak.pl/FUZZ`  
    Fuzz `sekurak.pl` paths using `common.txt`.

24. `ffuf -w common.txt -u https://sekurak.pl/FUZZ -fc 301,302`  
    Fuzz while filtering out HTTP 301/302 responses.

25. `ffuf -w common.txt -u https://gmail.com/video/.swf/FUZZ -r`  
    Recursive fuzzing (`-r`) on `.swf` paths under `/video`.

26. `hping3 -S --flood -p 8999 127.0.0.1`  
    Send a SYN-flood to localhost port 8999.

27. `python3 -m http.server 8999`  
    Run a simple HTTP server on port 8999 for testing.

28. `tcpdump -i lo -A`  
    Capture and display packet contents on the loopback interface.
