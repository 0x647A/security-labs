# Linux commands list

## User and Group Management
`useradd john`  
Create user “john”.

`usermod -aG sudo john`  
Add “john” to the “sudo” group.

`groupadd devops`  
Create group “devops”.

`gpasswd -a john devops`  
Add “john” to group “devops”.

`userdel -r john`  
Delete user “john” and remove their home directory.

## Passwords and Authentication
`passwd john`  
Set or change “john”’s password.

`chage -l john`  
Display password aging information for “john”.

`ssh-keygen -t ed25519 -C "john@host"`  
Generate an Ed25519 SSH key pair for “john”.

`ssh-copy-id john@server`  
Install “john”’s SSH public key on a remote host.

## File Permissions and ACLs
`chmod 750 /srv/app`  
Set owner=rwx, group=rx, others=— on `/srv/app`.

`chown john:devops /srv/app`  
Change owner to “john” and group to “devops”.

`getfacl /srv/app`  
Show POSIX ACL entries on `/srv/app`.

`setfacl -m u:qa:rwx /srv/app`  
Grant user “qa” read, write, execute on `/srv/app`.

`setfacl -R -m g:infra:rx /etc/infra`  
Recursively add read and execute for group “infra” under `/etc/infra`.

## Sudo and Privileged Access
`visudo`  
Safely edit the `/etc/sudoers` file.

Add line in sudoers:  
`john ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart httpd`

`sudo -l -U john`  
List commands “john” may run via sudo.

`sudo journalctl -u sshd`  
View SSH daemon logs (requires sudo).

## PAM and Authentication Policies
`authselect list`  
List available PAM profiles on RHEL/CentOS 8+.

`authselect select sssd`  
Enable SSSD PAM profile.

Edit `/etc/pam.d/system-auth` (or `/etc/pam.d/sshd`) to require MFA, enforce password complexity, etc.

## LDAP and Directory Services
`getent passwd john`  
Query user “john” via NSS (files, LDAP, SSSD).

`ldapsearch -x -LLL -b dc=example,dc=com "(uid=john)"`  
Search LDAP for “john”.

`realm join example.com`  
Join an Active Directory domain via Realmd/SSSD.

`realm list`  
Display joined realm configuration.

## Monitoring and Auditing
`ausearch -m USER_LOGIN -ts today`  
Search auditd logs for user login events today.

`grep john /var/log/auth.log`  
Filter authentication log entries for “john”.

`journalctl -u sshd --since "2 hours ago"`  
Show SSH daemon logs from the last two hours.

## Passwordless and FIDO2/WebAuthn
`pamu2fcfg > ~/.config/Yubico/u2f_keys`  
Register your U2F security key.

Add to `/etc/pam.d/sshd`:  
`auth required pam_u2f.so`