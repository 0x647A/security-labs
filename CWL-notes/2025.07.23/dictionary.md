# A
**AAA (Authentication, Authorization, Accounting)**  
A security framework:  
- **Authentication** – Verifying identity (password, token, biometrics).  
- **Authorization** – Granting access rights.  
- **Accounting** – Logging activities for audit.

**ABAC (Attribute-Based Access Control)**  
Real-time access decisions based on user, resource, and environment attributes.

**ACL (Access Control List)**  
Resource-specific list defining user/group permissions (read, write, execute).

# C
**CTAP (Client to Authenticator Protocol)**  
Protocol for communicating with external authenticators (USB/NFC/Bluetooth).

# D
**DAC (Discretionary Access Control)**  
Resource owner–managed permissions, typically via ACLs.

# F
**FIDO2**  
Passwordless standard combining WebAuthn (browser API) and CTAP for secure public-key authentication.

**IAM (Identity and Access Management)**  
Framework of policies, processes, and technologies for managing digital identities and access.

# J
**JIT (Just-In-Time Access)**  
Temporary privilege elevation granted only as needed and revoked automatically.

# L
**LDAP (Lightweight Directory Access Protocol)**  
Protocol for querying and modifying directory services (e.g., Active Directory).

# M
**MAC (Mandatory Access Control)**  
System-enforced access based on security labels; users cannot override.

**MFA (Multi-Factor Authentication)**  
Authentication requiring two or more independent factors (knowledge, possession, inherence, etc.).

# O
**OAuth 2.0**  
Authorization framework allowing third-party apps limited access via tokens.

**OIDC (OpenID Connect)**  
Authentication layer on OAuth 2.0 issuing ID tokens (JWT) for identity assertions.

# P
**PAM (Privileged Access Management)**  
Securing privileged accounts via vaulting, session isolation, and least-privilege/JIT.

**PoLP (Principle of Least Privilege)**  
Granting users only the permissions essential for their tasks.

# R
**RBAC (Role-Based Access Control)**  
Assigning permissions to roles, then assigning roles to users.

**RADIUS (Remote Authentication Dial-In User Service)**  
Network authentication/accounting protocol encrypting only the password.

# S
**SAML (Security Assertion Markup Language 2.0)**  
XML-based standard for exchanging authentication and authorization data between IdP and SP.

**Session Isolation**  
PAM feature routing privileged sessions through a bastion host and recording them.

**SSO (Single Sign-On)**  
One authentication grants access to multiple service providers.

# T
**TACACS+**  
Cisco proprietary AAA protocol encrypting the entire packet and separating AAA functions.

**Token**  
Digital artifact (JWT, SAML assertion, OAuth token) conveying identity or authorization information.

# U
**ULM (User Lifecycle Management)**  
Managing identity creation, provisioning, maintenance, deprovisioning, and retirement.

# V
**Vaulting**  
Secure storage of privileged credentials with automated rotation.

**WebAuthn**  
W3C browser API for passwordless authentication using public-key credentials.

# Z
**Zero Trust Architecture (ZTA)**  
Security model “never trust, always verify,” enforcing continuous authentication, authorization, and encryption for every request.
