# Threat Intelligence & Enterprise Risk Assessment: APT34 (OilRig)

## 📌 Project Overview
This project simulates an end-to-end security consulting engagement, divided into two primary phases: 
1. **Threat Intelligence:** Conducting in-depth research on the Advanced Persistent Threat (APT) group **APT34** to understand their operational history, motives, and technical attack paths.
2. **Enterprise Risk Assessment:** Applying that threat intelligence to evaluate a client's security posture, identify vulnerabilities, and calculate risk using a structured matrix.

---

## 🕵️‍♂️ Phase 1: Threat Profile - APT34 (OilRig / Helix Kitten)

### Threat Actor Background
* **Origin & Association:** State-sponsored cyber-espionage group linked to the Iranian government. Active since at least 2014.
* **Primary Motive:** Espionage and the covert collection of sensitive strategic information to support national geopolitical objectives.
* **Target Industries:** Energy, Finance, Telecommunications, and Government sectors.
* **Target Regions:** Primarily focused on organizations operating within the Middle East.

### Tactics, Techniques, and Procedures (TTPs)
APT34 utilizes a robust set of techniques across the attack lifecycle. Their methodologies map to the following MITRE ATT&CK categories:

* **Initial Access:** Spear-phishing campaigns with malicious attachments/links; exploitation of compromised valid accounts.
* **Execution:** Heavy reliance on scripting interpreters including PowerShell (for decoding/execution), Windows Command Shell (macro-driven malware like QUADAGENT and OopsIE), and VBScript. Often requires user interaction (enabling macros).
* **Persistence:** Exploitation of remote services (VPN, Citrix, OWA), lateral movement via compromised credentials, web shell deployments, and scheduled tasks executing VBScript payloads.
* **Privilege Escalation:** Scheduled task manipulation and lateral movement utilizing stolen higher-level credentials.
* **Defense Evasion:** Payload deobfuscation (PowerShell/Base64), masquerading executables as legitimate documents (`.doc`), indicator removal (deleting payloads post-execution), and sandbox/virtualization evasion (e.g., checking for connected peripherals).
* **Credential Access:** Brute-force attacks, keylogging (KEYPUNCH, LONGWATCH), and credential dumping (Mimikatz, LaZagne).
* **Discovery:** Network scanning (SoftPerfect, GOLDIRONY), process enumeration (`tasklist`), and local system discovery (`hostname`, `ipconfig`).
* **Lateral Movement:** Execution via Remote Desktop Protocol (RDP) and Secure Shell (SSH) utilizing tools like PuTTY.
* **Collection:** Automated keylogging and screen capture software (CANDYKING).
* **Command and Control (C2):** Primary communication via HTTP, utilizing Plink for protocol tunneling. Employs DNS tunneling as a fallback channel (ISMAgent).
* **Exfiltration:** Data exfiltration conducted over FTP, intentionally separated from primary C2 channels.

### Recommended Mitigation Strategy
To defend against APT34's specific TTPs, the following defensive architecture is recommended:
1. **Perimeter & Email Security:** Deploy advanced email filtering to quarantine phishing attempts. Enforce strict application whitelisting and disable MS Office macros globally.
2. **Identity & Access Management (IAM):** Mandate Multi-Factor Authentication (MFA) across all remote access points and enforce aggressive password cycling policies.
3. **Execution Controls:** Restrict PowerShell execution policies; implement aggressive script monitoring for obfuscated commands.
4. **Network Architecture:** Segment critical network enclaves to choke lateral movement. Audit and restrict RDP/SSH access. 
5. **Vulnerability Management:** Prioritize patching for public-facing infrastructure (Web Apps, VPN gateways) to close initial access vectors.
6. **Detection & Response:** Deploy comprehensive EDR solutions mapped to behavioral anomalies (e.g., unexpected DNS tunneling, registry modifications). 

---

## 📊 Phase 2: Enterprise Risk Assessment

Following the threat intelligence phase, a comprehensive risk assessment was conducted for the client. While the client maintained basic physical security controls (fencing, padlocks), their cyber infrastructure required systematic evaluation to ensure the Confidentiality, Integrity, and Availability (CIA) of their critical assets.

### Assessment Methodology
* **Asset Identification:** Mapped critical data and infrastructure assets requiring protection.
* **Scenario Development:** Outlined realistic cyber risk scenarios based on current threat intelligence (including APT34 TTPs).
* **Risk Matrix Application:** Calculated Inherent Risk (without controls) versus Residual Risk (with proposed controls).
* **Remediation Prioritization:** Delivered prioritized security recommendations to help the client mitigate high-impact vulnerabilities and achieve regulatory compliance.

## 📁 Repository Contents
* `Risk_Assessment.xlsx` - Contains the full quantitative risk matrix, asset inventory, scenario mappings, and prioritized security controls.
