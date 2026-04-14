# BlueSky Ransomware Incident — Network Forensics Report

## Summary
This report analyzes a ransomware intrusion affecting a major corporation responsible for critical data across multiple industries. 
The attack led to encryption of key files, system disruption, and signs of sophisticated threat actor activity. 
Through log analysis, packet captures, registry inspection, and event log parsing, investigators uncovered the attacker’s methods: credential compromise, privilege escalation, lateral movement using SQL Server abuse, process injection, PowerShell abuse, persistence creation, and eventual ransomware deployment. 
The findings below reconstruct the attacker’s actions step-by-step to support containment and remediation.


## Category  
Network Forensics

## Tactics Observed  
Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Command & Control, Impact

## Tools Used  
Wireshark, Network Miner, Windows Event Viewer, Event Log Explorer, VirusTotal, CyberChef

---

# Incident Questions & Answers

## Q1 — Source IP of port scanning activity  
**Answer:** `87.96.21.84`

<img width="626" height="433" alt="image" src="https://github.com/user-attachments/assets/a9c93428-7db9-4b4b-9a08-acfd535d99a4" />


## Q2 — Username targeted by the attacker  
**Answer:** `Sa`

<img width="626" height="433" alt="image" src="https://github.com/user-attachments/assets/687955a7-c6e1-4243-9abc-412e4d8275e4" />


## Q3 — Password successfully discovered by the attacker  
**Answer:** `cyb3rd3f3nd3r$`

<img width="626" height="433" alt="image" src="https://github.com/user-attachments/assets/a1fdd4b0-bd2a-4649-8e58-d5692f4fcf87" />


## Q4 — Setting enabled by the attacker for further control  
**Answer:** `xp_cmdshell`  

The attacker enabled and executed commands through the SQL Server extended stored procedure `xp_cmdshell` to run OS-level commands remotely.

<img width="626" height="346" alt="image" src="https://github.com/user-attachments/assets/b138f6cd-78f3-49f8-bd34-3987c205113f" />
<img width="626" height="338" alt="image" src="https://github.com/user-attachments/assets/dfcc11c9-913f-43c3-922a-3058246b2818" />
<img width="626" height="338" alt="image" src="https://github.com/user-attachments/assets/303168e2-defb-400c-a61d-90098ef35be8" />

`To enable xp_cmdshell you would run the following command

EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
`


## Q5 — Process used for C2 process injection  
**Answer:** `winlogon.exe`  

The attacker injected the Metasploit C2 payload into this privileged system process to obtain administrative-level control.

<img width="626" height="671" alt="image" src="https://github.com/user-attachments/assets/a92fae5b-5024-4024-aae2-d9ead82f8501" />

`🚨 PowerShell Event ID 400: Attack Significance
PowerShell Event ID 400 logs the successful initialization of the PowerShell engine, transitioning its state to 'Available.' This event is a critical indicator in security monitoring because PowerShell is often abused for post-exploitation activities (e.g., executing commands, downloading payloads, or establishing Command and Control (C2) communication).

🔍 Context and Attack Technique
The specific log entry highlighted is highly suspicious because it shows the PowerShell engine starting with the hostname MSFConsole and the application path winlogon.exe.
MSFConsole: This refers to the Metasploit Framework's command-line interface, a powerful penetration testing tool frequently used by attackers to launch and manage exploits.
Process Injection: The key threat is the reference to winlogon.exe, a critical system process running with high privileges that handles user logins. By injecting the Metasploit C2 framework into winlogon.exe, the attacker gains administrative privileges and can execute commands stealthily, granting them full control over the system.

🛡️ Defensive Action
Defenders should actively monitor process creation and PowerShell events, especially looking for abnormal activity involving sensitive processes like winlogon.exe. Implementing detailed logging, command-line auditing, and Endpoint Detection and Response (EDR) solutions is essential to detect and mitigate such advanced attacks.
`

## Q6 — URL of attempted file download  
**Answer:** `http://87.96.21.84/checking.ps1`

<img width="626" height="342" alt="image" src="https://github.com/user-attachments/assets/09abc335-4022-4361-ab4c-3bcd75adc8c5" />


## Q7 — Group SID checked by the malicious script  
**Answer:** `S-1-5-32-544`  
This SID corresponds to the Local Administrators group.

<img width="626" height="342" alt="image" src="https://github.com/user-attachments/assets/bb3bfe2c-3d4a-4492-9889-2e918018aa46" />


## Q8 — Registry keys used to disable Windows Defender  
**In order:**  
1. `DisableAntiSpyware`  
2. `DisableRoutinelyTakingAction`  
3. `DisableRealtimeMonitoring`  
4. `SubmitSamplesConsent`  
5. `SpynetReporting`

<img width="626" height="342" alt="image" src="https://github.com/user-attachments/assets/d0d529e5-533e-4d1b-a305-0e9a0df1cd23" />


## Q9 — Second malicious file downloaded  
**Answer:** `http://87.96.21.84/del.ps1`

<img width="626" height="500" alt="image" src="https://github.com/user-attachments/assets/b86d1f0d-01d0-4883-8ec6-e3d7f05b70b1" />


## Q10 — Full name of malicious scheduled task (persistence)  
**Answer:** `\Microsoft\Windows\MUI\LPupdate`

<img width="626" height="494" alt="image" src="https://github.com/user-attachments/assets/a5fc233f-0101-49e0-a417-bb59d9f2566b" />


## Q11 — MITRE ID for the main tactic of the second file  
**Answer:** `TA0005` — *Defense Evasion*

The `del.ps1` script deletes forensic artifacts and terminates monitoring tools to hinder detection.

`Justification (TA0005: Defense Evasion)
The entire purpose of the del.ps1 script is to take steps after the primary compromise to avoid detection and hinder forensics. This directly aligns with the Defense Evasion tactic.
The script accomplishes this through two main techniques:
Deletion of Persistence Mechanisms: It runs Get-WmiObject _FilterToConsumerBinding... | Remove-WmiObject to clean up WMI event consumers, which are often used by attackers to establish stealthy, persistent access. Removing this evidence makes detection and tracing the initial compromise difficult.
Process Termination: It forcefully kills critical security and monitoring tools (taskmgr, Procmon, ProcessHacker, etc.). By terminating these defensive processes, the script prevents the victim or security tools from observing the malicious activity, services, or files created by the main payload.`

<img width="626" height="494" alt="image" src="https://github.com/user-attachments/assets/e20d0450-6660-40c4-b0b8-e53b62a75e11" />


## Q12 — PowerShell script invoked for credential dumping  
**Answer:** `Invoke-PowerDump.ps1`

<img width="626" height="494" alt="image" src="https://github.com/user-attachments/assets/adf65e21-28de-4982-990d-92b63490ffaf" />


## Q13 — Saved text file containing dumped credentials  
**Answer:** `Hashes.txt`

<img width="626" height="370" alt="image" src="https://github.com/user-attachments/assets/e8dd6e09-7dcf-45fc-a13e-2f8a8f13e912" />


## Q14 — File containing discovered hosts  
**Answer:** `Extracted_hosts.txt`

<img width="626" height="496" alt="image" src="https://github.com/user-attachments/assets/bf19c150-f52e-447a-a4a0-253651b9e332" />


## Q15 — Ransom note filename  
**Answer:** `#DECRYPT FILES BLUESKY#`


## Q16 — Ransomware family  
**Answer:** `Bluesky`

<img width="626" height="310" alt="image" src="https://github.com/user-attachments/assets/7377e76f-1d53-48d9-a420-645acaa676fa" />


# End of Report
