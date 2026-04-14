# FakeGPT Browser Extension — Malware Analysis Report

## Summary
This report examines a malicious browser extension disguised as “ChatGPT,” which was installed by several employees believing it to be legitimate. After installation, the extension began stealing credentials, monitoring user activity, and transmitting sensitive data to an attacker-controlled domain. The analysis reveals a combination of obfuscation, keylogging, form interception, encrypted exfiltration, and anti-analysis triggers. The following findings outline each malicious behavior observed during the investigation.

---

## Category  
Malware Analysis

## Tactics Observed  
Credential Access, Collection, Command & Control, Exfiltration

---

# Investigation Questions & Answers

## Q1 — Encoding method used to hide target URLs  
**Answer:** Base64

<img width="626" height="435" alt="image" src="https://github.com/user-attachments/assets/b927d51f-a976-44c7-8885-fdc588ece021" />


## Q2 — Website targeted for credential theft  
**Answer:** `www.facebook.com`

<img width="626" height="371" alt="image" src="https://github.com/user-attachments/assets/9b3988ec-72a5-4d95-8b69-bf4fbabcc62e" />


## Q3 — HTML element used for exfiltration  
**Answer:** `<img>`

<img width="626" height="54" alt="image" src="https://github.com/user-attachments/assets/b75fc1a3-9610-4ce1-837f-865c8728871c" />


## Q4 — First condition that triggers extension self-deactivation  
**Answer:** `navigator.plugins.length === 0`

This check helps detect headless browsers or sandboxed analysis environments.

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/88d4d2f7-9a48-44ff-b127-4c96eb5e5dd6" />


## Q5 — Event used to track form submissions  
**Answer:** `submit`

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/052e29a2-ac72-43d8-b696-c48c8d23b5b8" />

## Q6 — API/method used to capture keystrokes  
**Answer:** `keydown`

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/9e98dd39-664f-4fb9-8c10-019bbd67922f" />


## Q7 — Domain receiving stolen data  
**Answer:** `mo[.]elshaheedy[.]com`

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/ab084a20-6e90-4b57-95bb-3ea739a2cf82" />


## Q8 — Function responsible for credential exfiltration  
**Answer:** `exfiltrateCredentials(username, password);`

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/02ec5b6b-e95f-4e0c-a30a-fae3549e0e99" />


## Q9 — Encryption algorithm applied before sending data  
**Answer:** `AES`

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/ac037e3a-6c28-44a5-9a48-4abf5fc67205" />


## Q10 — What the extension accesses to manage session/auth data  
**Answer:** Cookies

<img width="626" height="319" alt="image" src="https://github.com/user-attachments/assets/b979496c-8581-4c7b-8ea0-05085fc11a8f" />


# End of Report
