# “Rigged BTLO” Investigation — Blue Team Labs

## Investigation Summary  
This analysis examines how an adversary infiltrated Rusty Shackleford’s workstation, deployed malicious scripts, elevated privileges, harvested credentials, and established outbound C2 connectivity.  
Key observations include:  
- Unauthorized access of the target user account.  
- Execution of a weaponized document to gain initial foothold.  
- Use of scheduled tasks and credential dumping to persist and move laterally.  
- Deployment of a C2 infrastructure leveraging domain-fronting and cloud-service headers to mask command traffic.

---

## Q1: Rusty’s username and host details  
- **Username:** rusty.shackleford  
- **IP address:** 192.168.116.137  
- **Hostname:** DESKTOP-6RF3M5O  

<img width="627" height="293" alt="image" src="https://github.com/user-attachments/assets/e342e764-6aa6-4972-a069-ba4905dcfa6b" />


## Q2: Artifact from explorer.exe launch  
- **PID:** 9040  
- **Parent PID:** 728  
- **Parent process name:** powershell.exe

<img width="627" height="293" alt="image" src="https://github.com/user-attachments/assets/ab8131a5-0a44-4f55-aa44-a5e0c28b3f55" />


## Q3: Initial access mechanism  
- **Executable:** winword.exe  
- **Filename:** 37486-the-shocking-truth-about-election-rigging-in-america.doc

<img width="627" height="252" alt="image" src="https://github.com/user-attachments/assets/99a5f4bd-8877-459c-898b-4cab24340924" />


## Q4: C2 framework in use  
- **Answer:** Empire

<img width="627" height="496" alt="image" src="https://github.com/user-attachments/assets/0e4827e6-9419-4477-beb0-cf1e70ff8af9" />


## Q5: Domains reached by the compromised host  
- **Primary domain:** vldlh12o060gb5[.]azureedge[.]net  
- **Secondary domain:** florencereidbank[.]com

<img width="627" height="514" alt="image" src="https://github.com/user-attachments/assets/8a775cf6-332a-40d4-acea-3b21f5407191" />


## Q6: Proxy technique and header used  
- **Technique:** Domain fronting  
- **HTTP header used:** Host

`1. Proxying Technique Used
The attacker has used domain fronting to proxy their Command and Control (C2) infrastructure.
Domain fronting allows attackers to disguise C2 traffic as legitimate requests to trusted domains (e.g., cloud services, CDNs).


In the provided PowerShell script, the attacker modifies HTTP headers to route traffic through a fronting domain while hiding the real C2 server.


2. HTTP Header Used
The attacker used the "Host" header to achieve domain fronting:
The script includes:

 $E6CC5.HeaDers.ADD("Host","florencereidbank[.]com")


The Host header is changed to "florencereidbank[.]com", which means:


The request may first go to a legitimate CDN or web service.


The backend will forward it to the real malicious C2 server.


Indicators of Attack
The presence of System.Net.WebClient for HTTP-based C2.


Custom User-Agent string spoofing (Trident/7.0 for Internet Explorer 11 evasion).


Encoded payloads (FromMBASe64StrinG(...) suggesting base64-encoded commands).


Proxy credential caching (.CrEDENtiAlCACHE) for persistence.


Final Answer
Proxying Technique: Domain Fronting


HTTP Header Used: Host header

)
`

## Q7: Likely APT group responsible  
- **Answer:** APT29

<img width="627" height="285" alt="image" src="https://github.com/user-attachments/assets/d2b17eff-66bc-4b96-b524-83c0058c2662" />


## Q8: Initial access likely vector  
- **Answer:** Phishing  

<img width="623" height="216" alt="image" src="https://github.com/user-attachments/assets/a2cae622-baac-478c-871e-2545a3ce7506" />


## Q9: Privilege escalation method & command line  
- **Technique:** Bypass UAC  
- **Command line:** `C:\Windows\system32\schtasks.exe /Run /TN \Microsoft\Windows\DiskCleanup\SilentCleanup /I`

<img width="689" height="349" alt="image" src="https://github.com/user-attachments/assets/df123c78-8318-4f84-8298-e0b0636e9c4e" />


## Q10: Additional malicious activity (Credential Access)  
- **Technique ID:** T1003.001  
- **Command line:** `"C:\Windows\System32\procdump64.exe" -accepteula -ma lsass.exe C:\lsass.dmp`

<img width="697" height="225" alt="image" src="https://github.com/user-attachments/assets/a6669b73-7c6e-40b3-a8ae-1e14e337e324" />


## Q12: Attacker access level & confidence in attribution  
- **Required access level:** NT Authority\System  
- **Attribution confidence:** Low  

## End of Report
