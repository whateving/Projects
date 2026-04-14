# SOC Alpha 3 — BTLO Walkthrough

## Investigation Summary
In this lab scenario, you act as a SOC analyst reviewing Windows and firewall logs stored in an ELK stack. By examining process events, registry changes, firewall rules, evidence of compression and data staging, malicious downloads, and ransomware activity, you uncover a full attacker lifecycle: data collection, persistence via Run keys, log tampering, firewall manipulation, payload retrieval, ransomware deployment, and crypto-mining activity.

---

## Q1: What program is used for compression?  
**Answer:** `C:\Program Files\WinRAR\WinRAR.exe`

<img width="626" height="230" alt="image" src="https://github.com/user-attachments/assets/b7afea09-5e29-4fd9-bbac-926a4409a270" />


## Q2: What is the name of the compressed file?  
**Answer:** `gatherings.rar`

## Q3: What is the name of the file that has been added to the registry?  
**Answer:**  
`reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /v WindowsProcess /t REG_S`

## Q4: What is the RegValue?  
**Answer:** `WindowsProcess`

<img width="626" height="230" alt="image" src="https://github.com/user-attachments/assets/22e74988-f957-4108-9e91-1f19112309ee" />


## Q5: What is the timestamp when the logs are cleared?  
**Answer:** `2021-05-28T00:26:29`

## Q6: Log source and field confirming log clearing?  
**Answer:**  
- Log source: `winevent-security`  
- Field: `Event_System_EventID = 1102`

<img width="626" height="230" alt="image" src="https://github.com/user-attachments/assets/747ab54b-e48b-4a8e-ad55-37a8642f2c7c" />


## Q7: What program was used to add the firewall rule?  
**Answer:** `netsh.exe`

## Q8: What is the rule name?  
**Answer:** `Zoop TCP Port 80`

<img width="626" height="230" alt="image" src="https://github.com/user-attachments/assets/89c958f1-c4c2-4301-8e07-a5b239049637" />


## Q9: What program downloaded the suspicious file?  
**Answer:** `bitsadmin.exe`

## Q10: What is the download URL?  
**Answer:** `https://pastebin.com/raw/AGdtReXJO`

<img width="626" height="230" alt="image" src="https://github.com/user-attachments/assets/69423c2f-a640-484e-839e-f57a2de16cea" />


## Q11: MD5 hash of the DarkSide ransomware sample?  
**Answer:** `9d418ecc0f3bf45029263b0944236884`

<img width="626" height="583" alt="image" src="https://github.com/user-attachments/assets/419d95bd-660b-470f-851d-80c2469c89bc" />


## Q12: Full command associated with DllHost.exe alert?  
**Answer:**  
`C:\Windows\SysWOW64\DllHost.exe /Processid:{3E5FC7F9-9A51-4367-9063-A120244FBEC7}`

<img width="626" height="343" alt="image" src="https://github.com/user-attachments/assets/73a2aca1-cac8-4b8f-be49-6d56f9da636a" />


## Q13: Full command used to delete the malware?  
**Answer:**  
`C:\Windows\system32\cmd.exe /C DEL /F /Q C:\Users\nexus\DOWNLO~1\151FBD~1.EXE >> NUL`

<img width="626" height="343" alt="image" src="https://github.com/user-attachments/assets/c76d4926-0a73-444e-a179-4d50716d261f" />


## Q14: Username of the mining server?  
**Answer:**  
`42PkwcWLCjheUAaXy2h6CndY9DoKvv4pQ6QogCxgnFFF268ueYNb2FXiLCgQeds64jAytuaXzFTctbsujZYzUuaRVhn8Cjd`

## Q15: Version of the miner?  
**Answer:** `6.12.1`

<img width="626" height="220" alt="image" src="https://github.com/user-attachments/assets/815b87d5-9a04-4512-a1ec-c27f739f4cd9" />


## Q16: Full command attempting to stop Windows Defender?  
**Answer:**  
`C:\Windows\system32\net.exe STOP WinDefend`

<img width="626" height="220" alt="image" src="https://github.com/user-attachments/assets/c88d2612-1816-4446-9a2e-03e126274523" />


## Q17: Services the attacker attempted to stop (alphabetical order)?  
**Answer:** `spooler`, `WbioSrvc`, `wlidsvc`

<img width="626" height="220" alt="image" src="https://github.com/user-attachments/assets/5b19697c-d8ac-44fc-a160-60e435c663b5" />

## End of Walkthrough
