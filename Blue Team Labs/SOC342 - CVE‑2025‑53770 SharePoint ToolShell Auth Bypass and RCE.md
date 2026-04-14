# Incident Analysis: CVE-2025-53770 (ToolShell)

**Alert ID:** SOC342  
**Verdict:** **True Positive / Confirmed Compromise** **Severity:** Critical

<img width="1133" height="471" alt="image" src="https://github.com/user-attachments/assets/ac30bd09-d6b1-4c1a-9b49-f90e10e9e6d8" />

---
## 1. The two devices that are used in the communication are as follows: 

* Source IP: 107.191.58.76
* Destionation IP: 172.16.20.17 (SharePoint01 Server)
---
## 2. The extrenal IP in the question is owned by Vultr a leading privately-held global cloud computing platform offering Infrastructure-as-a-Service (IaaS) services.

Screenshot from an IP locator: 

<img width="434" height="394" alt="image" src="https://github.com/user-attachments/assets/493d74c1-cfdf-480b-91f5-981768d5ff83" />

---

## 3. The following can be derived from the alert we have received:

### 1. Traffic Content Analysis
**Requirement:** Check for suspicious conditions (Web Attack Payloads like SQLi, XSS, RCE, etc.).

* **Finding:** The traffic contains a **Remote Code Execution (RCE)** payload via **Unsafe Deserialization**.
* **Payload Indicators:**
    * The attack does not use standard text-based injections like SQLi or XSS.
    * The `Content-Length: 7699` indicates a large data blob in the POST body.
    * In this specific CVE, this blob is a Base64-encoded, serialized .NET object (often wrapping a malicious gadget chain) injected into the `MSOTlPn_DWP` parameter.

### 2. HTTP Request Field Examination
**Requirement:** Examine source data and request fields to validate the attack.

| Field | Value | Analysis |
| :--- | :--- | :--- |
| **Referer** | `/_layouts/SignOut.aspx` | **MALICIOUS.** This is the specific "exploit primitive" used to bypass authentication. Normal users never navigate to `ToolPane.aspx` from the SignOut page. |
| **URL** | `.../ToolPane.aspx...` | **TARGETED.** This legacy endpoint is the known vulnerable component for deserialization attacks in SharePoint. |
| **Method** | `POST` | **CONSISTENT.** A POST request is required to carry the large serialized payload. |
| **Source IP** | `107.191.58.76` | **EXTERNAL.** Public IP address (Geoloc: United States). Unlikely to be legitimate administrative traffic. |
| **Device Action** | **Allowed** | **CRITICAL FAILURE.** The network security controls did not block the request. |

---

## 4. Examining the device logs at time the attack happened gives us the following information:

### 1. w3wp.exe was used to execute a base64 encoded powershell code:

Screenshot:

<img width="913" height="688" alt="image" src="https://github.com/user-attachments/assets/ca37aefe-430c-433d-9bc2-9d0fd24d4651" />

Screenshot:

<img width="1174" height="688" alt="image" src="https://github.com/user-attachments/assets/c3792e53-81ba-42e0-a309-c8da0218bd23" />

### 2. csc.exe was also spawned by powershell to compile C code:

Screenshot:

<img width="1174" height="688" alt="image" src="https://github.com/user-attachments/assets/661082ed-1cd4-4996-9f4d-dc93aff9f916" />


### 3. A webshell was also added right after the C code compilation:

Screenshot:

<img width="1174" height="688" alt="image" src="https://github.com/user-attachments/assets/be7bad1f-c750-4536-a0e0-5fb7f6177aa9" />

---


## 5. Conclusion & Immediate Actions

**Assessment:**
This is a **successful exploitation** of the ToolShell Zero-Day (CVE-2025-53770). The attacker bypassed authentication and executed code on the server `172.16.20.17`.

**Finished Actions:**
1.  **Isolate:** Disconnected `172.16.20.17` from the network immediately.

**Required Actions:**

1. Escalate the case to Tier 2
2.  **Remediation:** Rotate SharePoint Machine Keys and apply the July 2025 Security Update.
