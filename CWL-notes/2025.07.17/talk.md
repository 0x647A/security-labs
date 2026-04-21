# CyberWomen Leaders – Training 4: Cryptography and Encryption

## 1. Definitions  
- **Cryptography**: securing information by transforming it into an unreadable form (ciphertext). Goals: confidentiality, integrity, authentication, non-repudiation.  
- **Cryptanalysis**: breaking ciphers (brute-force, known-plaintext, chosen-plaintext, birthday, meet-in-the-middle).  
- **Cryptology**: cryptography + cryptanalysis.  
- **Plaintext** vs **Ciphertext**: plaintext is human- or machine-readable data; ciphertext is the secure, encrypted form that protects confidentiality until decrypted back into plaintext.  
- **Encryption/Decryption**: algorithm + key.  
- **Key**: secret bit string.  
- **Cipher (algorithm)**: mathematical transformation.  
- **Cryptosystem**: algorithm + protocol + key management.  
- **Protocols**: SSL/TLS, SSH, IPsec.  
- **Kerckhoffs’s Principle**: security relies on key secrecy, not algorithm secrecy.  
- **IV (Initialization Vector)**: random value for block modes (CBC, GCM).  
- **Nonce**: one-time value.  
- **Hash Function**: one-way, fixed-length digest; used for integrity checks, HMAC, PBKDF2.  
  - **Collision**: when two distinct inputs produce the same hash output. Example: MD5 collisions found in 2004 allow forging two different PDF files with identical digests.  
- **Salt/Pepper**: random values added before hashing.  
- **Padding**: block size filler.  
- **Keyspace**: total number of possible keys.  
- **Steganography**: hiding data in multimedia (LSB).

## 1.1 Cryptography Functions  
- **Confidentiality**: protects data secrecy via encryption (e.g., AES, RSA).  
- **Integrity**: ensures data isn’t altered using hash functions (e.g., SHA-256, HMAC).  
- **Accountability**: enables non-repudiation and audit trails via secure protocols and log integrity (e.g., TLS, signed logs).  
- **Anonymity**: preserves user privacy using encryption and zero-knowledge proofs (e.g., Tor, ZK-SNARKs).

## 1.2 Encryption Process (General)

### Public-Key (Asymmetric) Workflow
- Bob wants to send a confidential message “Hello Alice!”  
- Bob obtains Alice’s **public key** and uses it to **encrypt** the plaintext.  
- The output is ciphertext (e.g., “6EB69570 08F03CE4”), which Bob sends to Alice.  
- Alice uses her **private key** to **decrypt** the ciphertext and recover the original plaintext.  

This ensures confidentiality without requiring Bob and Alice to share a secret key in advance.

### Cryptography Taxonomy
```bash
Cryptography
├─ Keyless
│ └─ Classical ciphers (Caesar, Atbash, ROT13)
└─ Key-Based
├─ Asymmetric Key
│ └─ RSA & Others
├─ Symmetric Key
│ ├─ Block Ciphers
│ │ ├─ DES
│ │ ├─ 3DES
│ │ ├─ Blowfish
│ │ └─ AES
│ └─ Stream Ciphers
│ └─ RC4 & Others
└─ Cryptographic Protocols (SSL/TLS, SSH, IPsec)
```

- **Keyless** algorithms rely on fixed transformations without secret keys (e.g., Caesar cipher).  
- **Asymmetric Key** algorithms use key pairs: public keys to encrypt, private keys to decrypt (e.g., RSA).  
- **Symmetric Key** algorithms use the same secret key for both encryption and decryption:  
  - **Block ciphers** (DES, 3DES, Blowfish, AES) process fixed-size blocks.  
  - **Stream ciphers** (RC4) generate a keystream to XOR with plaintext bytes.  
- **Cryptographic protocols** combine algorithms and key management to secure networked communication.  

## 1.3 Encoding Process (General)

Encoding transforms input data into a fixed-size representation (digest), providing integrity but not confidentiality.
Plaintext ──▶ Hash Function ──▶ Hashed Text (Digest)

- **Plaintext**: original data of arbitrary length.  
- **Hash Function**: deterministic algorithm producing a fixed-length output.  
  - Properties: one-way, collision-resistant, avalanche effect.  
  - Examples: SHA-256, SHA-3, BLAKE2.  
- **Hashed Text**: fixed-size digest (e.g., 256-bit for SHA-256) used to verify data integrity.

### Examples
- Compute SHA-256 in Linux/macOS:
```bash
sha256sum file.txt
```

- Compute MD5:
```bash
md5sum file.txt
```

- HMAC with SHA-256 (requires a secret key):
```bash
echo -n "message" | openssl dgst -sha256 -hmac "secret"
```

Use hashes to:
- Check file integrity (e.g., download verification).  
- Store password verifiers with salt & slow hashing (bcrypt, Argon2).  
- Generate message authentication codes (HMAC) for authenticated encryption.  

## 1.3 Encryption vs Encoding

### Encryption & Decryption Process
Plain Text → Encryption → Encrypted Text → Decryption → Plain Text

- **Reversible** process where data can be encrypted and then decrypted back to its original form
- Requires a **key** for both encryption and decryption operations  
- **Purpose**: Provides confidentiality - makes data unreadable to unauthorized parties
- **Examples**: AES, RSA, DES

### Hashing Process
Plain Text → Hash Function → Hashed Text (fixed-length digest)

- **One-way** process - you cannot reverse a hash back to the original data
- Does **not require** a key (though keyed hashing like HMAC exists)
- **Purpose**: Provides integrity verification - confirms data hasn't been altered
- **Examples**: SHA-256, MD5, bcrypt

### Key Differences

| **Encryption** | **Hashing** |
|---|---|
| Reversible (with key) | One-way (irreversible) |
| Variable output length | Fixed output length |
| Provides confidentiality | Provides integrity |
| Uses keys | Typically keyless |
| Examples: AES, RSA | Examples: SHA-256, MD5 |

### Visual Example
- **Encryption**: "Hello" + key → "5F4DCC3B" → decrypt with key → "Hello"
- **Hashing**: "Hello" → SHA-256 → "2CF24DFA4F21D4288094C79B9E86A8C3..." (always same output)

This demonstrates why encryption and hashing serve different security purposes in the CIAA model (Confidentiality, Integrity, Authentication, Accountability).

## 2. History & Algorithms  
- **Ancient**: scytale, hieroglyphs, Caesar cipher.  
- **Renaissance**: Alberti disk, Vigenère autokey.  
- **20th Century**: Enigma (Rejewski), Lorenz, BB84 (quantum), responsible disclosure.

## 3. Historical Ciphers  
- **Caesar**: letter shift (KOTEK→NRWHN).  
- **Atbash**: reverse alphabet (KOT→PLG).  
- **ROT13**: 13-shift (HELLO→URYYB).  
- **Vigenère**: polyalphabetic table.  
- **Rail Fence**: zig-zag transposition.

## 4. Symmetric Block Ciphers

### What is Symmetric Key Cryptography?
**SKC – Symmetric Key Cryptography** is a type of encryption where the same key is used for both encrypting and decrypting data.

### Uses:

#### Integrity Check
- **Non-cryptographic checksum** - protection against accidental corruption of a message
- **Example**: CRC Checksum
- **Purpose**: Detect transmission errors, hardware failures, or accidental data modification
- **Limitation**: Cannot detect intentional tampering

#### Cryptographic Checksum  
- **Message Authentication Code (MAC)** - sent with the message itself
- **Purpose**: Provides both integrity and authenticity verification
- **Examples**: HMAC-SHA256, CMAC, Poly1305
- **Advantage**: Can detect intentional modification attempts

### Key Characteristics of Symmetric Encryption:
- **Same key** used for both encryption and decryption
- **Fast processing** - suitable for large amounts of data
- **Key distribution challenge** - securely sharing the secret key
- **Examples**: AES, DES, 3DES, ChaCha20

### MAC vs Simple Checksum:
| **Simple Checksum (CRC)** | **MAC (Cryptographic)** |
|---|---|
| Detects accidental errors | Detects intentional tampering |
| No secret key required | Requires secret key |
| Fast computation | Slower but secure |
| Not suitable for security | Provides authentication |

### Common Symmetric Algorithms:
- **AES** (Advanced Encryption Standard) - current standard
- **ChaCha20** - modern stream cipher
- **3DES** - legacy, being phased out
- **DES** - obsolete, broken

### 4.1 DES (Data Encryption Standard)
- **Block size**: 64 bits (8 bytes) - processes data in fixed chunks
- **Key length**: 56 bits effective + 8 parity bits = 64 bits total
  - Parity bits used for error detection, not encryption strength
  - Only 56 bits provide actual security (2^56 = ~72 quadrillion possible keys)
- **Feistel structure**: splits 64-bit block into two 32-bit halves (L and R)
  - **16 rounds** of processing:
    1. Right half becomes new left half
    2. Left half XORed with F-function output becomes new right half
    3. F-function uses: expansion, S-box substitution, permutation
- **S-boxes**: 8 substitution boxes that provide non-linearity and confusion
- **Key schedule**: generates 16 different 48-bit round keys from main 56-bit key
- **Obsolescence**: 56-bit key broken by specialized hardware (1998) and distributed computing
- **Modern status**: Completely insecure, replaced by AES

### 4.2 3DES (Triple DES)
- **Operation**: Three sequential DES operations with different keys
  - **Encrypt** with K₁ → **Decrypt** with K₂ → **Encrypt** with K₃
  - Why decrypt in middle? Backward compatibility with single DES when K₁=K₂=K₃
- **Key configurations**:
  - **Two-key 3DES**: K₁=K₃, K₂ different (112-bit effective security)
  - **Three-key 3DES**: all keys different (168-bit key, ~112-bit effective security)
- **Security improvement**: Meet-in-the-middle attack reduces effective key length
  - 168-bit key provides only ~112 bits of security, not 168
- **Performance**: ~3x slower than single DES, much slower than AES
- **Current status**: Legacy system support only, deprecated in favor of AES
- **Block size**: Still 64 bits (inherited from DES) - smaller than AES's 128 bits

### 4.3 AES (Advanced Encryption Standard)
- **Block size**: 128 bits (16 bytes) - larger blocks than DES/3DES
- **Key lengths**: 
  - **AES-128**: 128-bit key, 10 rounds
  - **AES-192**: 192-bit key, 12 rounds  
  - **AES-256**: 256-bit key, 14 rounds
- **Round operations** (applied in sequence):
  1. **SubBytes**: byte-level substitution using S-box (confusion)
  2. **ShiftRows**: cyclically shift rows of state matrix (diffusion)
  3. **MixColumns**: matrix multiplication in Galois field (diffusion)
  4. **AddRoundKey**: XOR with round key derived from main key
- **Final round**: skips MixColumns step

#### AES Block Cipher Modes:

**CBC (Cipher Block Chaining)**:
- **Initialization Vector (IV)**: random 128-bit value for first block
- **Chaining**: each plaintext block XORed with previous ciphertext block
- **Padding**: PKCS#7 padding required for last block if not full 128 bits
- **Limitations**: 
  - No built-in authentication (vulnerable to padding oracle attacks)
  - Sequential processing (cannot parallelize decryption fully)
  - Error propagation: corruption in one block affects next block
- **Use cases**: File encryption, VPN tunnels (when combined with separate MAC)

**GCM (Galois/Counter Mode)**:
- **Counter mode**: converts block cipher into stream cipher
  - Encrypts incrementing counter values, XORs with plaintext
  - Fully parallelizable encryption/decryption
- **Authentication**: built-in Galois field MAC (GMAC)
- **Nonce requirement**: 96-bit nonce must be unique for each encryption with same key
  - Nonce reuse catastrophically breaks security
- **No padding**: works with any plaintext length
- **Output**: ciphertext + authentication tag (typically 128 bits)
- **Advantages**: 
  - Provides confidentiality AND integrity in single operation
  - High performance (especially with hardware acceleration)
  - Authenticated Encryption with Associated Data (AEAD)
- **Use cases**: TLS 1.2+, IPsec, modern protocols requiring authenticated encryption

## 5. Symmetric Stream Ciphers

### What are Stream Ciphers?
**Stream ciphers** encrypt data one byte at a time, like a continuous stream. They generate a **keystream** (random-looking bytes) and XOR it with your data.

### How they work (simple)
Your data: H e l l o
Keystream: X Y Z A B (random bytes generated from key)
↓ ↓ ↓ ↓ ↓
Encrypted: ? ? ? ? ? (XOR result - looks random)

### Key difference from block ciphers
- **Block ciphers**: Process data in chunks (like 16-byte blocks)
- **Stream ciphers**: Process data continuously, one byte at a time

### 5.1 RC4 - **DON'T USE!**
- **Created**: 1987, was very popular
- **Problem**: Completely broken by researchers
- **Used in**: Old WiFi (WEP), old websites
- **Status**: **Avoid completely** - it's insecure

**Why broken?**
- Predictable patterns in the random keystream
- Attackers can recover your encryption key
- All major browsers/systems have banned it

### 5.2 ChaCha20 - **Modern & Safe**
- **Created**: 2008 by top cryptographer
- **Status**: **Very secure** - recommended everywhere
- **Used in**: Modern websites (TLS 1.3), VPNs, Signal app
- **Speed**: Very fast, works great on phones

**Why it's good:**
- No known attacks against it
- Fast on all devices (phones, computers, servers)
- Simple design = easier to implement correctly
- Used by Google, Cloudflare, and other major companies

### When to use Stream Ciphers
**Good for:**
- Real-time communication (video calls, gaming)
- Devices with limited memory
- When you need very fast encryption

**Examples:**
- **Video streaming**: Encrypt video as it's being sent
- **VoIP calls**: Encrypt voice data in real-time
- **IoT devices**: Small sensors that need efficient encryption

### Simple comparison

| Feature | RC4 | ChaCha20 |
|---------|-----|----------|
| **Security** | Broken ❌ | Excellent ✅ |
| **Speed** | Fast | Very fast |
| **Use today** | Never | Yes |
| **Trust level** | Zero | High |

### Key takeaway
- **RC4 = Old and broken** - never use it
- **ChaCha20 = Modern and secure** - good choice for new projects
- Stream ciphers are fast and good for continuous data (video, audio, real-time communication)

## 6. Asymmetric (Public Key) Ciphers  

### Key Characteristics
- **One public key** is used in the encryption process
- **Another secret key** is used in the decryption process
- **Public Key Cryptography** - eliminates the key distribution problem of symmetric encryption

### How Asymmetric Encryption Works
Plaintext → [Public Key] → Encryption → Ciphertext (encrypted)
Ciphertext (encrypted) → [Private Key] → Decryption → Plaintext

### Key Properties
- **Public Key**: can be freely distributed, shared openly
  - Used for **encryption** by anyone who wants to send secure messages
  - Used for **signature verification**
- **Private Key**: must be kept secret by the owner
  - Used for **decryption** of messages encrypted with corresponding public key
  - Used for **digital signing** of documents/messages

### Mathematical Foundation
- Based on mathematical problems that are easy to compute in one direction but computationally infeasible to reverse
- **Examples of hard problems**:
  - Integer factorization (RSA)
  - Discrete logarithm (ElGamal, DSA)
  - Elliptic curve discrete logarithm (ECC)

### Common Asymmetric Algorithms
- **RSA**: most widely used, based on prime factorization
- **ElGamal**: based on discrete logarithm problem
- **ECC (Elliptic Curve Cryptography)**: shorter keys, same security level
- **DSA (Digital Signature Algorithm)**: primarily for digital signatures

### Advantages over Symmetric Encryption
- **No key distribution problem**: public keys can be shared openly
- **Digital signatures**: provides non-repudiation
- **Key management**: easier to manage in large networks

### Disadvantages
- **Performance**: much slower than symmetric encryption (100-1000x)
- **Key size**: requires larger keys for equivalent security
- **Resource intensive**: more CPU and memory usage

### Typical Use Cases
- **Hybrid encryption**: RSA/ECC to exchange AES keys
- **Digital certificates**: PKI infrastructure
- **Digital signatures**: document authentication
- **Key exchange**: secure establishment of symmetric keys

### 6.1 RSA (Rivest-Shamir-Adleman)

#### Mathematical Foundation
RSA security relies on the **integer factorization problem**: while it's easy to multiply two large prime numbers, factoring their product back into the original primes is computationally infeasible for sufficiently large numbers.

#### Key Generation Process
1. **Choose two large prime numbers**: p and q (typically 1024+ bits each)
   - Example: p = 61, q = 53 (small example for illustration)
2. **Compute n = p × q**: this becomes the modulus
   - Example: n = 61 × 53 = 3233
3. **Calculate Euler's totient**: φ(n) = (p-1)(q-1)
   - Example: φ(3233) = 60 × 52 = 3120
4. **Choose public exponent e**: commonly 65537 (2^16 + 1)
   - Must be coprime to φ(n): gcd(e, φ(n)) = 1
   - Example: e = 17
5. **Calculate private exponent d**: d = e^(-1) mod φ(n)
   - Find d such that: e × d ≡ 1 (mod φ(n))
   - Example: d = 2753 (since 17 × 2753 ≡ 1 mod 3120)

#### Key Components
- **Public Key**: (n, e) - can be shared openly
  - n: modulus (product of two secret primes)
  - e: public exponent
- **Private Key**: (n, d) - must be kept secret
  - n: same modulus as public key
  - d: private exponent (multiplicative inverse of e)

#### Encryption/Decryption Process
- **Encryption**: c = m^e mod n
  - Convert plaintext message m to integer < n
  - Raise to power e, take modulo n
  - Example: message = 123, ciphertext = 123^17 mod 3233 = 855
- **Decryption**: m = c^d mod n
  - Raise ciphertext c to power d, take modulo n
  - Example: 855^2753 mod 3233 = 123 (original message)

#### Security Considerations
- **Key length**: modern RSA uses 2048-4096 bit keys
- **Padding schemes**: OAEP (Optimal Asymmetric Encryption Padding) prevents certain attacks
- **Performance**: very slow compared to symmetric encryption
- **Quantum vulnerability**: Shor's algorithm can break RSA on quantum computers

### 6.2 ElGamal & ECC (Elliptic Curve Cryptography)

#### ElGamal Encryption
**Mathematical Foundation**: Based on the **discrete logarithm problem** in multiplicative groups
- Given g^x mod p, it's hard to find x even knowing g and p

**Key Generation**:
1. Choose large prime p and generator g
2. Choose private key x (random integer)
3. Compute public key y = g^x mod p
4. Public key: (p, g, y); Private key: x

**Encryption Process**:
1. Choose random k for each message
2. Compute c1 = g^k mod p
3. Compute c2 = m × y^k mod p
4. Ciphertext: (c1, c2)

**Decryption Process**:
1. Compute s = c1^x mod p
2. Compute m = c2 × s^(-1) mod p

#### ECC (Elliptic Curve Cryptography)
**Mathematical Foundation**: Based on **elliptic curve discrete logarithm problem**
- Given point P and Q = kP on elliptic curve, finding k is computationally hard

**Elliptic Curve Equation**: y² = x³ + ax + b (mod p)

**Key Advantages over RSA**:
- **Smaller key sizes**: 256-bit ECC ≈ 3072-bit RSA security
- **Better performance**: faster key generation, encryption, decryption
- **Lower bandwidth**: smaller certificates, signatures
- **Mobile-friendly**: less CPU, memory, battery usage

**Popular ECC Curves**:
- **P-256** (secp256r1): NIST standard, widely supported
- **Curve25519**: designed for high performance and security
- **Ed25519**: optimized for digital signatures

**ECC vs RSA Security Comparison**:
| ECC Key Size | RSA Key Size | Security Level |
|--------------|--------------|----------------|
| 160 bits     | 1024 bits    | 80 bits        |
| 224 bits     | 2048 bits    | 112 bits       |
| 256 bits     | 3072 bits    | 128 bits       |
| 384 bits     | 7680 bits    | 192 bits       |
| 521 bits     | 15360 bits   | 256 bits       |

#### Use Cases & Applications
- **RSA**: TLS certificates, legacy systems, key exchange
- **ElGamal**: PGP encryption, some government applications
- **ECC**: modern TLS, mobile applications, IoT devices, Bitcoin/cryptocurrency

#### Performance Comparison
- **Key Generation**: ECC > ElGamal > RSA (fastest to slowest)
- **Encryption**: ECC ≈ ElGamal > RSA
- **Decryption**: ECC ≈ ElGamal > RSA
- **Signature Generation**: ECC > RSA > ElGamal
- **Signature Verification**: ECC ≈ RSA > ElGamal

## 7. Hash Functions  

### What is hashing?
**Hashing** is the process of transforming data of any length into a **fixed-length digest (hash)** using a hash function. This is a **one-way** process - the original data cannot be recovered from the hash.

#### Basic properties of hashing:
- **Deterministic**: the same data always produces the same hash
- **Fixed length**: hash always has the same size regardless of input data size
- **One-way**: practically impossible to reconstruct data from the hash
- **Avalanche effect**: smallest change in data causes completely different hash
- **Collision resistance**: difficult to find two different datasets producing the same hash

#### Hash function applications:
- **Integrity verification**: checking if data has been modified
- **Password storage**: secure storage without knowing the original password
- **Digital signatures**: confirming document authenticity
- **Blockchain**: linking blocks in chain, proof-of-work
- **Fast comparisons**: comparing large files through their hashes

### 7.1 MD5 (Message-Digest Algorithm 5)
**Released**: 1991 by Ronald Rivest  
**Output**: 128-bit (32 hexadecimal characters)  
**Status**: **Completely insecure** - do not use for any security purposes

#### How MD5 Works
- Processes input in 512-bit blocks
- Uses four rounds of operations with different functions (F, G, H, I)
- Produces deterministic 128-bit hash regardless of input size

#### Security Problems
- **Collision attacks**: Multiple collision examples found since 2004
  - Different inputs producing identical MD5 hashes
  - Practical attacks can generate collisions in seconds
- **Rainbow tables**: Precomputed tables make password cracking trivial
- **Speed**: Too fast for password hashing (billions of hashes per second)

#### Example Usage (for legacy compatibility only)

Generate MD5 hash
```bash
echo -n "password123" | openssl dgst -md5
Output: MD5(stdin)= 482c811da5d5b4bc6d497ffa98491e38
Alternative command
echo -n "password123" | md5sum
```

#### Current Applications
- **File integrity** (when not under attack): checksums for downloads
- **Legacy systems**: some old databases still use MD5
- **Non-security purposes**: unique IDs, cache keys

### 7.2 SHA-1 (Secure Hash Algorithm 1)
**Released**: 1995 by NSA  
**Output**: 160-bit (40 hexadecimal characters)  
**Status**: **Deprecated** - collision attacks demonstrated

#### How SHA-1 Works
- Processes input in 512-bit blocks
- Uses 80 rounds of operations
- More secure than MD5 but still vulnerable

#### Security Problems
- **SHAttered attack (2017)**: Google demonstrated practical collision
  - Two different PDF files with identical SHA-1 hashes
  - Required 2^63 operations (still computationally expensive but feasible)
- **Deprecation timeline**: 
  - 2011: NIST deprecated SHA-1 for digital signatures
  - 2016: Major browsers stopped trusting SHA-1 certificates
  - 2020: Most systems phased out SHA-1

#### Example Usage

Generate SHA-1 hash
```bash
echo -n "password123" | openssl dgst -sha1
Output: SHA1(stdin)= 40bd001563085fc35165329ea1ff5c5ecbdbbeef
Alternative command
echo -n "password123" | sha1sum
```

#### Migration Strategy
- Replace with SHA-2 or SHA-3 for new applications
- Legacy systems should prioritize SHA-1 to SHA-256 migration

### 7.3 SHA-2 Family (Current Standard)
**Released**: 2001 by NSA  
**Variants**: SHA-224, SHA-256, SHA-384, SHA-512  
**Status**: **Secure** and widely recommended

#### SHA-256 (Most Common)
**Output**: 256-bit (64 hexadecimal characters)  
**Block size**: 512 bits  
**Security**: No known practical attacks

#### How SHA-2 Works
- Similar structure to SHA-1 but with enhanced security
- SHA-256: 64 rounds of operations
- SHA-512: 80 rounds with 64-bit words
- Merkle-Damgård construction with Davies-Meyer compression

#### Performance Characteristics
- **SHA-256**: Optimal for most applications
- **SHA-512**: Faster on 64-bit systems, larger output
- **Hardware acceleration**: Supported by modern CPUs (Intel SHA extensions)

#### Example Usage

SHA-256 (most common)
```bash
echo -n "password123" | sha256sum
Output: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```
SHA-512 (longer hash)
```bash
echo -n "password123" | sha512sum
File integrity checking
sha256sum file.txt > file.txt.sha256
sha256sum -c file.txt.sha256 # Verify integrity
```

#### Applications
- **TLS certificates**: SHA-256 standard for HTTPS
- **Bitcoin**: SHA-256 for proof-of-work
- **File integrity**: checksums, digital signatures
- **HMAC**: message authentication codes

### 7.4 bcrypt (Adaptive Hashing)
**Released**: 1999 by Niels Provos and David Mazières  
**Based on**: Blowfish cipher  
**Purpose**: **Password hashing** with adaptive cost

#### How bcrypt Works
1. **Salt generation**: Random 128-bit salt for each password
2. **Key expansion**: Blowfish key schedule modified by salt and password
3. **Iterative hashing**: Expensive key setup repeated 2^cost times
4. **Output format**: `$2a$cost$salt+hash` (60 characters total)

#### Key Features[1][2]
- **Adaptive cost factor**: Configurable work factor (4-31)
  - Cost 10 = 2^10 = 1,024 iterations
  - Cost 12 = 2^12 = 4,096 iterations (recommended minimum)
- **Built-in salt**: Automatic unique salt generation
- **Time-based security**: Increases cost as hardware improves

#### Security Characteristics[1][5]
- **CPU-bound**: Primarily uses CPU cycles, limited memory usage
- **Rainbow table resistance**: Salt prevents precomputed attacks
- **Brute-force resistance**: Configurable delay makes attacks expensive
- **GPU vulnerability**: Not memory-hard, vulnerable to parallel GPU attacks

#### Example Usage

Install bcrypt utility
apt-get install bcrypt # or use library
Python example
```python
import bcrypt
password = b"password123"
salt = bcrypt.gensalt(rounds=12) # Cost factor 12
hashed = bcrypt.hashpw(password, salt)
Output: $2b$12$xyz... (60 chars)
Verification
bcrypt.checkpw(password, hashed) # Returns True/False
```

#### Performance Tuning
- **Cost factor 12**: ~250ms on modern CPU (recommended minimum)
- **Cost factor 14**: ~1 second (high-security applications)
- **Rule of thumb**: Target 250ms-1s authentication time

#### When to Use bcrypt
- Legacy systems where Argon2 isn't available
- Memory-constrained environments
- Applications requiring battle-tested algorithms
- Systems with existing bcrypt infrastructure

### 7.5 Argon2 (Modern Password Hashing Winner)
**Released**: 2015 (Password Hashing Competition winner)  
**Designed by**: University of Luxembourg  
**Purpose**: **State-of-the-art password hashing**

#### Argon2 Variants
- **Argon2d**: Data-dependent memory access, GPU-resistant
- **Argon2i**: Data-independent memory access, side-channel resistant  
- **Argon2id**: Hybrid approach (**recommended** by OWASP and NIST)

#### How Argon2 Works
1. **Memory allocation**: Allocates configurable memory buffer
2. **Initialization**: Fills memory with pseudorandom data
3. **Processing**: Multiple passes through memory (time cost)
4. **Parallel execution**: Configurable thread count (parallelism)
5. **Output**: Variable-length hash (typically 32 bytes)

#### Three Key Parameters
- **Memory cost (m)**: Amount of RAM used (in kibibytes)
  - Example: m=65536 = 64 MB memory usage
- **Time cost (t)**: Number of iterations through memory
  - Example: t=3 = three passes through memory
- **Parallelism (p)**: Number of parallel threads
  - Example: p=4 = four parallel lanes

#### Security Advantages
- **Memory-hard**: Requires significant RAM, making GPU/ASIC attacks expensive
- **Parallel resistance**: Memory requirements scale with parallelization
- **Side-channel protection**: Argon2i/id variants resist timing attacks
- **Future-proof**: Designed for evolving hardware landscape

#### Example Usage

Install Argon2
```bash
apt-get install argon2
```
Command line usage
```bash
echo -n "password123" | argon2 somesalt -t 3 -m 12 -p 1
-t 3: time cost, -m 12: 2^12 KB memory, -p 1: parallelism
```
Python example
```python
from argon2 import PasswordHasher
ph = PasswordHasher(
time_cost=3, # iterations
memory_cost=65536, # 64 MB
parallelism=4 # threads
)
hashed = ph.hash("password123")
Output: $argon2id$v=19$m=65536,t=3,p=4$hash...
Verification
ph.verify(hashed, "password123") # Raises exception if invalid
```

#### Performance Comparison
| Algorithm | Time (250ms target) | Memory Usage | GPU Resistance |
|-----------|-------------------|--------------|----------------|
| bcrypt    | cost=12          | ~4 KB        | Low            |
| Argon2id  | t=3, m=65536     | 64 MB        | High           |

#### Parameter Recommendations
- **Web applications**: m=65536 (64MB), t=3, p=4
- **High security**: m=262144 (256MB), t=3, p=4  
- **Mobile/IoT**: m=16384 (16MB), t=3, p=1
- **OWASP recommendation**: Argon2id for new applications

#### When to Use Argon2
- **New applications**: OWASP recommends Argon2id as first choice
- **High-security environments**: Banking, government, healthcare
- **Systems with adequate memory**: Servers with sufficient RAM
- **Modern threat landscape**: Protection against GPU farms, cloud attacks

### Summary Recommendations

| Use Case | Algorithm | Rationale |
|----------|-----------|-----------|
| **New applications** | **Argon2id** | Best security against modern threats[8] |
| **Legacy systems** | bcrypt | Battle-tested, widely supported[8] |
| **File integrity** | SHA-256 | Fast, secure, hardware accelerated |
| **HMAC/signatures** | SHA-256 | Standard for cryptographic protocols |
| **Avoid completely** | MD5, SHA-1 | Collision attacks demonstrated |

## 8. PKI (Public Key Infrastructure)  

### What is PKI?
Public Key Infrastructure (PKI) is a comprehensive framework of hardware, software, policies, and procedures designed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption. PKI serves as the **governing body behind issuing digital certificates** to protect confidential data and provide unique digital identities to users and systems.

### Core Purpose
PKI facilitates **secure electronic transfer of information** for network activities such as e-commerce, internet banking, and confidential email where simple passwords are inadequate and more rigorous proof is required to confirm identities.

### 8.1 Certificate Authority (CA)

#### Definition & Role
The **Certificate Authority** is a trusted third-party entity that serves as the cornerstone of PKI by issuing, storing, and signing digital certificates. The CA acts as a digital notary public, vouching for the authenticity of digital identities.

#### Key Functions
- **Key pair generation**: Creates public-private key pairs (independently or with client collaboration)
- **Identity verification**: Validates the identity of certificate requestors before issuance
- **Certificate issuance**: Creates digital certificates containing user's public key and identity information
- **Digital signing**: Signs certificates with its own private key to prevent tampering
- **Certificate publishing**: Makes certificates available through directories or direct distribution
- **Certificate verification**: Provides public keys for validating certificate authenticity
- **Certificate revocation**: Maintains ability to invalidate compromised or suspicious certificates

#### CA Hierarchy Structure
Root CA (Offline, Highly Secure)
↓
Intermediate CA (Policy CA)
↓
Issuing CA (Operational CA)
↓
End-Entity Certificates (Users, Servers, Devices)

**Root CA**:
- **Offline storage**: Kept in secure, air-gapped environments (HSMs, secure facilities)
- **Infrequent use**: Only activated to sign intermediate CA certificates
- **Highest security**: Physical and logical security controls, multiple authentication
- **Long validity**: Certificates valid for 10-20 years

**Intermediate CA**:
- **Policy enforcement**: Implements specific certificate policies and practices
- **Risk distribution**: Isolates root CA from operational risks
- **Flexibility**: Can be revoked without affecting root CA trust
- **Medium validity**: Certificates typically valid for 5-10 years

**Issuing CA**:
- **Daily operations**: Issues end-entity certificates to users and systems
- **Online availability**: Accessible for certificate requests and validation
- **Automated processes**: Handles high-volume certificate issuance
- **Short validity**: Certificates typically valid for 1-3 years

### 8.2 Registration Authority (RA)

#### Definition & Purpose
The **Registration Authority** acts as an intermediary between end-entities and the Certificate Authority, focusing specifically on **identity verification** before certificate issuance.

#### Key Responsibilities
- **Identity verification**: Confirms the identity of certificate requestors through various methods:
  - Document verification (government IDs, business licenses)
  - Domain ownership validation (for SSL certificates)
  - Email verification and callback procedures
  - In-person verification for high-assurance certificates
- **Request processing**: Collects and validates certificate requests
- **Policy enforcement**: Ensures compliance with certificate policies and practices
- **Approval/rejection**: Makes decisions on certificate issuance based on verification results

#### RA vs CA Separation
- **Security benefit**: RA can be compromised without affecting CA's signing capabilities
- **Scalability**: Multiple RAs can serve different geographic regions or customer types
- **Specialization**: RAs focus on verification processes, CAs focus on cryptographic operations
- **Combined model**: Small PKIs may have CA perform RA functions

### 8.3 Certificate Revocation (CRL/OCSP)

#### Why Certificate Revocation?
Certificates need revocation when:
- **Private key compromise**: Key has been stolen, lost, or exposed
- **Identity change**: Subject's identity or organizational status changes
- **CA compromise**: Issuing CA's security has been breached
- **Supersession**: Certificate being replaced by newer version
- **Cessation**: Subject no longer needs the certificate

#### CRL (Certificate Revocation List)

**Definition**: A signed list of revoked certificates published by the CA at regular intervals.

**Structure**:
- CRL Header:
    - Issuer (CA name)
    - Issue date/time
    - Next update time
    - CRL version
- Revoked Certificates List:
    - Serial number
    - Revocation date
    - Revocation reason code
    - CA Digital Signature

**Advantages**:
- **Offline verification**: Can be cached and used without network access
- **Comprehensive**: Contains all revoked certificates
- **Standardized**: Well-established X.509 standard

**Disadvantages**:
- **Latency**: Updates only at scheduled intervals (hours/days)
- **Size growth**: CRL grows continuously as more certificates are revoked
- **Bandwidth**: Large CRLs consume significant network resources
- **Processing time**: Long lists require time to search

#### OCSP (Online Certificate Status Protocol)

**Definition**: Real-time protocol that allows applications to query certificate status from a validation authority.

**How OCSP Works**:
1. **Query**: Client sends certificate serial number to OCSP responder
2. **Response**: OCSP responder returns one of three statuses:
   - **Good**: Certificate is valid and not revoked
   - **Revoked**: Certificate has been revoked (with date and reason)
   - **Unknown**: OCSP responder doesn't know about this certificate

**OCSP Response Format**:
- Response Status: successful
- Response Type: id-pkcs9-ocspBasicResponse
- Certificate Status: good/revoked/unknown
- This Update: timestamp
- Next Update: timestamp (optional)
- Signature: OCSP responder's digital signature

**Advantages**:
- **Real-time**: Up-to-date status information
- **Efficient**: Only queries specific certificates
- **Scalable**: Distributed OCSP responders
- **Privacy**: Can use OCSP stapling to reduce queries

**Disadvantages**:
- **Availability dependency**: Requires network access
- **Privacy concerns**: Reveals browsing patterns to CA
- **Performance**: Network latency for each check

#### OCSP Stapling
**Enhancement**: Web server pre-fetches OCSP responses and "staples" them to TLS handshake, reducing client queries and improving privacy.

### 8.4 PKI Hierarchy Models

#### Single CA Model
Root CA
↓
End-Entity Certificates

- **Simple**: Easy to implement and manage
- **Risk**: Single point of failure
- **Use case**: Small organizations, closed systems

#### Hierarchical Model (Recommended)
Root CA (Offline)
↓
Intermediate CA(s)
↓
Issuing CA(s)
↓
End-Entity Certificates

- **Security**: Root CA isolation
- **Scalability**: Multiple intermediates for different purposes
- **Flexibility**: Can revoke intermediate without affecting root trust

#### Cross-Certification Model
Root CA A ←→ Root CA B
↓ ↓
Intermediate Intermediate

- **Interoperability**: Different PKI domains can trust each other
- **Federation**: Enables cross-organization certificate validation

### 8.5 Certificate Types & Use Cases

#### Server Certificates (SSL/TLS)
- **Purpose**: Authenticate web servers and enable HTTPS
- **Validation levels**:
  - **Domain Validated (DV)**: Basic domain ownership verification
  - **Organization Validated (OV)**: Domain + organization verification
  - **Extended Validation (EV)**: Highest level, legal entity verification

#### Client Certificates
- **Purpose**: Authenticate users to servers/applications
- **Use cases**: VPN access, email signing, application authentication

#### Code Signing Certificates
- **Purpose**: Verify software integrity and publisher identity
- **Applications**: Operating system drivers, mobile apps, software updates

#### Email Certificates (S/MIME)
- **Purpose**: Encrypt and digitally sign email messages
- **Standards**: S/MIME (Secure/Multipurpose Internet Mail Extensions)

### 8.6 PKI Security Considerations

#### Hardware Security Modules (HSMs)
- **Purpose**: Tamper-resistant hardware for key generation and storage
- **Benefits**: FIPS 140-2 Level 3/4 compliance, performance, key lifecycle management
- **Types**: Network-attached HSMs, PCIe cards, USB tokens

#### Certificate Pinning
- **Concept**: Applications validate against specific certificates/CAs
- **Protection**: Prevents malicious CA issuance
- **Implementation**: HTTP Public Key Pinning (HPKP), mobile app pinning

#### Certificate Transparency
- **Purpose**: Public logs of all issued certificates
- **Monitoring**: Detect unauthorized certificate issuance
- **Tools**: Google CT logs, crt.sh, Certificate Transparency Monitoring

### 8.7 PKI Implementation Example

#### Certificate Request Process
1. End-entity generates key pair
2. End-entity creates Certificate Signing Request (CSR)
3. CSR submitted to Registration Authority
4. RA verifies identity and approves request
5. CA receives approved request from RA
6. CA signs certificate with its private key
7. Certificate issued to end-entity
8. Certificate published/distributed as needed

#### Certificate Validation Process
1. Application receives certificate
2. Verify certificate signature using CA's public key
3. Check certificate validity period (not before/after dates)
4. Verify certificate hasn't been revoked (CRL/OCSP)
5. Validate certificate chain to trusted root CA
6. Check certificate purpose matches intended use
7. Validate subject name matches expected identity

### 8.8 PKI Standards & Protocols

#### X.509 Certificate Standard
- **Current version**: X.509v3
- **Fields**: Subject, Issuer, Serial Number, Validity Period, Public Key, Extensions
- **Encoding**: DER (binary), PEM (Base64)

#### Certificate Management Protocols
- **PKCS #10**: Certificate Request Syntax
- **PKCS #12**: Personal Information Exchange (PFX files)
- **CMP (Certificate Management Protocol)**: Comprehensive certificate lifecycle
- **EST (Enrollment over Secure Transport)**: RESTful certificate enrollment

#### Trust Store Management
- **Operating System**: Windows Certificate Store, macOS Keychain
- **Browsers**: Chrome, Firefox maintain separate trust stores
- **Applications**: Can maintain application-specific trust stores

## 9. JWT (JSON Web Token)

### What is JWT?
JSON Web Token (JWT) is an **open standard (RFC 7519)** for securely transmitting information between parties as a JSON object. JWTs are **self-contained** tokens that carry all necessary information within the token itself, eliminating the need for server-side session storage (stateless authentication).

### JWT Structure: header.payload.signature

JWT consists of three Base64URL-encoded parts separated by dots (`.`):

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

#### 9.1 Header
**Purpose**: Contains metadata about the token type and signing algorithm.

**Structure**:
```json
{
"alg": "HS256", // Signing algorithm
"typ": "JWT" // Token type
}
```

**Common algorithms**:
- **HS256**: HMAC with SHA-256 (symmetric key)
- **RS256**: RSA with SHA-256 (asymmetric key)
- **ES256**: ECDSA with SHA-256 (elliptic curve)
- **none**: No signature (dangerous - only for debugging)[3]

#### 9.2 Payload (Claims)
**Purpose**: Contains the actual data being transmitted, organized as claims.

**Standard claims (optional but recommended)**:

```json
{
"iss": "https://example.com", // Issuer
"sub": "1234567890", // Subject (user ID)
"aud": "https://api.example.com", // Audience
"exp": 1516239022, // Expiration time (Unix timestamp)
"nbf": 1516235422, // Not before (Unix timestamp)
"iat": 1516235422, // Issued at (Unix timestamp)
"jti": "unique-token-id" // JWT ID (unique identifier)
}
```

**Custom claims**:
```json
{
"name": "John Doe",
"role": "admin",
"permissions": ["read", "write", "delete"]
}
```

**Claim types**:
- **Registered claims**: Predefined, standardized (iss, sub, aud, exp, etc.)
- **Public claims**: Defined in IANA registry or as collision-resistant names
- **Private claims**: Custom claims for specific applications

#### 9.3 Signature
**Purpose**: Verifies the token's integrity and authenticity.

**HMAC (Symmetric) signature process**:

```bash
signature = HMACSHA256(
base64UrlEncode(header) + "." + base64UrlEncode(payload),
secret
)
```

**RSA (Asymmetric) signature process**:
```json
signature = RSA-SHA256(
base64UrlEncode(header) + "." + base64UrlEncode(payload),
private_key
)
```

### 9.4 JWS vs JWE

#### JWS (JSON Web Signature)
**Purpose**: Provides **integrity** and **authentication** but not confidentiality.

**Characteristics**:
- Payload is **readable** (only Base64 encoded)
- Signature prevents tampering
- Anyone can read the payload content
- Most common JWT implementation

**Use cases**:
- Authentication tokens where payload privacy isn't critical
- API authorization with non-sensitive user information
- Session management with public user data

**Example JWS**:
```bash
header.encrypted_key.initialization_vector.ciphertext.authentication_tag
```

**Characteristics**:
- Payload is **encrypted** and unreadable without decryption key
- Provides confidentiality + integrity
- More complex implementation
- Larger token size

**Use cases**:
- Tokens containing sensitive information (PII, financial data)
- Cross-domain authentication with private user details
- Regulatory compliance requiring data encryption

**Example JWE**:
```bash
eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.encrypted_key.iv.ciphertext.tag
```
Payload is completely encrypted and unreadable.

### 9.5 JWT Authentication Flow

Based on the diagram in the image, here's how JWT authentication works:

#### Initial Authentication
1. **User login**: Browser sends POST to `/user/login` with credentials (`username`, `password`)
2. **Server validation**: Server verifies credentials against database
3. **JWT creation**: Server creates JWT with user information and signs with secret key
4. **Token response**: Server sends JWT back to browser

#### Subsequent API Requests
1. **Token inclusion**: Browser includes JWT in `Authorization: Bearer <token>` header
2. **Token validation**: Server verifies JWT signature and extracts user information
3. **Authorization**: Server checks user permissions from JWT payload
4. **API response**: Server processes request and sends response

#### Key Benefits
- **Stateless**: No server-side session storage required
- **Scalable**: Works across multiple servers without shared state
- **Cross-domain**: Can be used across different domains/services
- **Self-contained**: All necessary information is in the token

### 9.6 Security Considerations & Best Practices

#### Token Security
- **Strong secrets**: Use cryptographically strong signing keys (256+ bits for HMAC)
- **Algorithm specification**: Always specify algorithm in code, don't trust header
- **Signature verification**: Always verify signature before trusting payload
- **Expiration**: Set reasonable expiration times (15-60 minutes for sensitive apps)
- **HTTPS only**: Never transmit JWTs over unencrypted connections

#### Common Vulnerabilities

**None Algorithm Attack**:
```json
{"alg": "none", "typ": "JWT"} // No signature required!
```
**Mitigation**: Explicitly whitelist allowed algorithms, reject "none"

**Key Confusion Attack**:
- Attacker uses public key as HMAC secret
- **Mitigation**: Separate handling of symmetric vs asymmetric algorithms

**Token Replay**:
- Stolen tokens can be reused until expiration
- **Mitigation**: Short expiration times, token refresh, JTI tracking

## 10. PGP / GPG (Pretty Good Privacy / GNU Privacy Guard)

### What is PGP/GPG?
**PGP (Pretty Good Privacy)** is a proprietary encryption program created by Phil Zimmermann in 1991, currently owned by Symantec. **GPG (GNU Privacy Guard)** is an open-source implementation of the OpenPGP standard that provides the same functionality as PGP but is freely available. Both systems provide secure encryption, decryption, and digital signing capabilities for emails, files, and digital communications.

### Core Differences: PGP vs GPG
| **PGP** | **GPG** |
|---------|---------|
| Proprietary (Symantec) | Open-source (GNU) |
| Commercial license required | Free to use |
| Limited algorithm support | Supports more algorithms |
| Primarily Windows/commercial | Cross-platform (Linux, Windows, macOS) |
| GUI-focused | Command-line focused |

### 10.1 Hybrid Encryption Model

## 10. PGP / GPG (Pretty Good Privacy / GNU Privacy Guard)

### What is PGP/GPG?
**PGP/GPG** are encryption systems for secure communication and file protection. **GPG** (GNU Privacy Guard) is the free, open-source version of **PGP** (Pretty Good Privacy).

### Main applications
- **File encryption** - document protection
- **Email encryption** - private correspondence  
- **Digital signatures** - authenticity confirmation
- **Software verification** - integrity checking

### How it works (hybrid encryption)
1. **AES** encrypts data (fast)
2. **RSA/ECC** encrypts AES key (secure)
3. Both elements sent to recipient

**Why this way?** AES is fast for large files, RSA is secure for keys.

### Basic commands

#### Key generation

Create new key pair
```bash
gpg --gen-key
```

#### File encryption
Encrypt file for specific person
```bash
gpg --encrypt --recipient user@example.com file.txt
```
Encrypt with password (without public keys)
```bash
gpg --symmetric file.txt
```

#### File decryption
Decrypt file
```bash
gpg --decrypt file.txt.gpg > original_file.txt
```

#### Digital signatures

Sign file
```bash
gpg --sign file.txt
```
Verify signature
```bash
gpg --verify file.txt.gpg
```

### Key management

#### List keys

Show all public keys
```bash
gpg --list-keys
```
Show private keys
```bash
gpg --list-secret-keys
```

#### Import/Export keys

Export your public key
```bash
gpg --export --armor user@example.com > public_key.asc
```
Import someone else's key
```bash
gpg --import their_public_key.asc
```

### Trust model
- **Web of Trust**: users sign each other's keys
- **No central authority**: no single controlling institution
- **Socially built trust**: more signatures = greater trust

### Practical example

1. Generate keys
```bash
gpg --gen-key
```
2. Export your public key
```bash
gpg --export --armor john@example.com > john_public.asc
```
3. Send public key to friends
4. Receive Alice's public key
```bash
gpg --import alice_public.asc
```
5. Encrypt file for Alice
```bash
gpg --encrypt --recipient alice@example.com secret.txt
```
6. Send encrypted file - only Alice can open it

### Most important rules
- **Private key** = keep secret, use strong password
- **Public key** = can share with everyone
- **Verify fingerprints** of keys through personal contact
- **Make backups** of private keys
- **Use expiration dates** for keys

## 11. TLS / SSL (Transport Layer Security / Secure Sockets Layer)

### What is TLS/SSL?
**TLS** (Transport Layer Security) is the modern security protocol that protects internet communications. **SSL** (Secure Sockets Layer) is the older, deprecated version. When people say "SSL", they usually mean TLS.

### Why do we need TLS?
Without TLS, all internet traffic is sent in **plaintext** - anyone can read it:
- Passwords
- Credit card numbers
- Personal messages
- Banking information

**TLS encrypts this data** so only the intended recipient can read it.

### How to recognize TLS
- **HTTPS** in browser address bar (instead of HTTP)
- **Lock icon** 🔒 in browser
- **Port 443** for HTTPS (instead of port 80 for HTTP)
- **Green address bar** for some high-security sites

### How TLS works (simplified)

#### TLS Handshake - 4 main steps:

1. Client: "Hello, I want to connect securely"
2. Server: "Hello, here's my certificate and supported encryption"
3. Client & Server: "Let's agree on encryption keys"
4. Both: "Ready! Let's start encrypted communication"


#### Detailed handshake process:
1. **ClientHello**: Browser sends supported encryption methods
2. **ServerHello + Certificate**: Server responds with its certificate (like an ID card)
3. **Key Exchange**: Both sides create shared encryption keys
4. **Finished**: Switch to encrypted communication

### What TLS provides

#### Confidentiality
- **Encryption**: Data is scrambled so only recipient can read it
- **Example**: Your password becomes unreadable gibberish to eavesdroppers

#### Integrity  
- **Tamper detection**: Knows if data was changed during transmission
- **Example**: Detects if someone modified your bank transfer amount

#### Authentication
- **Server identity**: Proves you're talking to the real website
- **Example**: Confirms you're on real Amazon.com, not a fake site

### TLS versions

| Version | Status | Security |
|---------|--------|----------|
| **SSL 2.0** | Broken | Never use |
| **SSL 3.0** | Broken | Never use |
| **TLS 1.0** | Deprecated | Avoid |
| **TLS 1.1** | Deprecated | Avoid |
| **TLS 1.2** | Good | Widely used |
| **TLS 1.3** | Best | Newest, fastest |

**Rule**: Use TLS 1.2 minimum, prefer TLS 1.3

### TLS 1.3 improvements
- **Faster**: Fewer round trips to establish connection
- **Stronger**: Removed weak/old encryption methods
- **Simpler**: Cleaner, more secure design
- **Better privacy**: Encrypts more of the handshake

### Common TLS tools

#### Check TLS version

Check what TLS version a website uses
```bash
openssl s_client -connect example.com:443 -tls1_2
```
Check certificate details
```bash
openssl s_client -connect example.com:443 -showcerts
```

#### Test TLS configuration

Connect and show connection details
```bash
curl -I https://example.com
```
Verbose connection info
```bash
curl -v https://example.com
```

### TLS certificates explained

#### What is a certificate?
A **digital ID card** for websites that contains:
- **Website name** (example.com)
- **Public key** (for encryption)
- **Certificate Authority signature** (proves it's genuine)
- **Expiration date**

#### Certificate Authority (CA)
- **Trusted organization** that issues certificates
- **Examples**: Let's Encrypt (free), DigiCert, GlobalSign
- **Browser trust**: Browsers have list of trusted CAs

#### Certificate validation
Browser checks:
1. **Signature**: Is certificate signed by trusted CA?
2. **Name**: Does certificate match website name?
3. **Date**: Is certificate still valid (not expired)?
4. **Revocation**: Has certificate been canceled?

### Common TLS problems

#### Certificate errors
- **Expired certificate**: Certificate passed expiration date
- **Wrong name**: Certificate issued for different domain
- **Self-signed**: Certificate not signed by trusted CA
- **Revoked**: Certificate was canceled

#### Connection issues
- **Mixed content**: HTTPS page loading HTTP resources
- **Weak encryption**: Using old, insecure algorithms
- **Protocol downgrade**: Forced to use older TLS version

### Best practices

#### For users
- **Look for HTTPS** - especially for sensitive sites
- **Check certificate** - click lock icon to verify
- **Don't ignore warnings** - browser certificate warnings are serious
- **Keep browsers updated** - get latest security features

#### For developers
- **Use TLS 1.2+** minimum
- **Strong ciphers** only (AES, ChaCha20)
- **Valid certificates** from trusted CA
- **HSTS headers** to force HTTPS
- **Certificate monitoring** to avoid expiration

### Real-world examples

#### Banking website

User types: https://bank.com
Browser connects to bank.com:443
TLS handshake establishes encryption
Bank's certificate proves identity
All data (login, transactions) encrypted
Attacker sees only encrypted gibberish

### Simple troubleshooting

#### "Not secure" warning
- **Problem**: Website using HTTP instead of HTTPS
- **Solution**: Try adding "https://" to URL manually

#### Certificate error
- **Problem**: Invalid/expired certificate
- **Solutions**: 
  - Check if URL is correct
  - Try again later (temporary issue)
  - Contact website owner
  - **Never** click "proceed anyway" for financial/sensitive sites

#### Connection timeout
- **Problem**: TLS handshake failing
- **Solutions**:
  - Check internet connection
  - Try different browser
  - Disable VPN temporarily
  - Clear browser cache

## 12. Steganography  

### What is Steganography?
**Steganography** is the art and science of hiding information within other non-secret data or media to avoid detection. Unlike cryptography which makes data unreadable, steganography makes the very existence of data invisible. The word comes from Greek "steganos" (covered/concealed) and "graphein" (writing).

### Steganography vs Cryptography
| **Steganography** | **Cryptography** |
|---|---|
| Hides existence of data | Makes data unreadable |
| Security through obscurity | Security through mathematical complexity |
| Data appears normal | Data obviously encrypted |
| Detection = failure | Decryption without key = security |

### Key Principle: Least Significant Bit (LSB)
The **LSB method** exploits the fact that changing the least significant bits of digital media causes minimal perceptual change. For example, in an 8-bit pixel value:

```bash
Original pixel: 11010110 (214 in decimal)
Modified pixel: 11010111 (215 in decimal) - LSB changed from 0 to 1
```

The human eye cannot detect this 1-unit difference in color intensity, making it perfect for hiding data.

### 12.1 Image Steganography

#### Common Image Formats
- **PNG**: Lossless compression, perfect for steganography
- **BMP**: Uncompressed, excellent LSB capacity
- **TIFF**: Lossless, good for large hidden payloads
- **GIF**: Limited palette, less ideal but usable
- **AVOID JPEG**: Lossy compression destroys hidden data

#### LSB Image Steganography Process

**Hiding Process**:
1. Convert secret message to binary
2. Select cover image (PNG/BMP recommended)
3. Extract pixel values (RGB channels)
4. Replace LSB of each color component with message bits
5. Save modified image (appears identical to original)

**Example**:
```bash
Secret message: "Hi" = 01001000 01101001 (16 bits)
Cover image pixels (RGB values):
Original: (255,254,253) (252,251,250) (249,248,247)...
After LSB: (255,254,252) (253,251,250) (248,248,246)...
↑ ↑ ↑ ↑ ↑ ↑
Hide: 0 1 0 0 1 0...
```
#### Capacity Calculation
For a 1920×1080 RGB image:
- Total pixels: 1920 × 1080 = 2,073,600 pixels
- RGB channels: 2,073,600 × 3 = 6,220,800 LSBs available
- Maximum payload: 6,220,800 ÷ 8 = 777,600 bytes ≈ 759 KB

### 12.2 Detection Methods & Countermeasures

#### Steganalysis Techniques
- **Visual inspection**: Look for unusual patterns, noise
- **Statistical analysis**: Chi-square test for randomness
- **Histogram analysis**: Look for LSB artifacts
- **Entropy analysis**: Measure randomness distribution
- **File size comparison**: Unexpectedly large files
- **Metadata examination**: Suspicious EXIF data
- **Tools:** `steghide`, `zsteg`, `binwalk`, `exiftool`, `stegsolve`.  

## 13. Cryptanalysis Attacks  
- Brute-force & dictionary attacks (tools: `hashcat`, `john`).  
- Known-plaintext, chosen-plaintext.  
- Birthday attack (hash collision finding, e.g., `hashclash`).  
- Meet-in-the-middle.  
- Example packet capture: `tshark -i eth0 -Y tls`.  
- Example JWT brute: `pyjwt` script to test keys.

### Usefull link

https://www.youtube.com/@cyrillgossi/playlists
