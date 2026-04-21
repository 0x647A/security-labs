# Linux Commands and Examples for Cryptography

1. Encrypt a file with AES-256-CBC
```bash
openssl enc -aes-256-cbc -in secret.txt -out encrypted.bin -k "yourpassword"
```
2. Decrypt a file with AES-256-CBC
```bash
openssl enc -d -aes-256-cbc -in encrypted.bin -out decrypted.txt -k "yourpassword"
```
3. Generate MD5 hash of a string
```bash
echo -n "admin" | md5sum
```
4. Save MD5 hash to a file
```bash
echo "21232f297a57a5a743894a0e4a801fc3" > hash.txt
```
5. Brute-force MD5 with Hashcat (mode 0, attack 3)
```bash
hashcat -m 0 -a 3 hash.txt ?l?l?l?l?l?1 --force
```
6. Create an MD5Crypt password hash
```bash
echo "123456" | openssl passwd -1 -stdin > passwd_hash.txt
```
7. Crack password hash with John the Ripper using rockyou wordlist
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt passwd_hash.txt
```
8. Create a JWT token with "none" alg
```bash
HEADER='{"alg":"none","typ":"JWT"}'
PAYLOAD='{"user":"admin"}'
echo -n "$HEADER" | base64 -w0 > h.txt
echo -n "$PAYLOAD" | base64 -w0 > p.txt
echo "$(cat h.txt).$(cat p.txt)." > jwt_none.txt
```
9. Capture TLS packets on port 443 with TShark
```bash
tshark -i eth0 -f "tcp port 443" -Y tls
```
10. Test JWT brute-force with Python and pyjwt
(Requires: pip install pyjwt)
```bash
python3 - << 'EOF'
import jwt
token = jwt.encode({"user": "admin"}, "secret", algorithm="HS256")
for word in ["admin","qwerty","secret","password"]:
try:
decoded = jwt.decode(token, word, algorithms=["HS256"])
print(f"Recovered key: {word}")
except:
pass
EOF
```
11. Replay intercepted Bearer token with curl
```bash
curl -H "Authorization: Bearer <intercepted_token>" https://target.app/api/
```
12. Encrypt a file using GPG
```bash
gpg --output secret.txt.gpg --encrypt --recipient you@example.com secret.txt
```
13. Decrypt a GPG-encrypted file
```bash
gpg --output secret.txt --decrypt secret.txt.gpg
```
14. Generate RSA key pair with OpenSSL
```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private.pem -out public.pem
```
15. Decode Base64-encoded content
```bash
base64 --decode encoded.txt > decoded.txt
```
16. Encode content to Base64
```bash
base64 input.txt > encoded.txt
```
17. Compute SHA-256 hash of a file
```bash
sha256sum file.txt
```
18. Create HMAC-SHA256 of data
```bash
echo -n "data" | openssl dgst -sha256 -hmac "yourkey"
```
19. Generate random 16-byte salt in hex
```bash
openssl rand -hex 16
```
20. List installed ciphers and protocols supported by OpenSSL
```bash
openssl ciphers -v 'ALL'
```