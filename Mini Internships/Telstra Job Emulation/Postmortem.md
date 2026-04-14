# Incident Postmortem: Spring Framework RCE (CVE-2022-22965)

## Summary
On **2022-03-20 at 03:16:34 UTC**, firewall alerts identified multiple malicious HTTP POST requests originating from various IP addresses. All traffic targeted `nbn.external.network`, exploiting a critical **Remote Code Execution (RCE)** vulnerability (**Spring4Shell**) within the Spring Framework. The incident was mitigated within two hours through the deployment of targeted firewall filtering rules.

---

## Impact
The vulnerability allowed unauthorized actors to execute arbitrary code on the affected server. Initial assessments indicate potential compromise of the application environment prior to containment.


---

## Detection
The incident was detected by automated firewall alerting. Security logs revealed a high volume of coordinated HTTP POST requests sharing identical paths and header signatures, signaling an active exploitation attempt.

---

## Root Cause
The root cause was identified as an outdated version of the **Spring Framework (v5.3.0)** susceptible to **CVE-2022-22965**. Publicly available Proof-of-Concept (PoC) exploits facilitated the attack.


---

## Resolution
Immediate remediation involved implementing a **Web Application Firewall (WAF)** rule to drop requests targeting the malicious path (`/tomcatwar.jsp`) and blocking the specific header patterns used in the exploit payload.

---

## Action Items
* **Perform an immediate upgrade** of the Spring Framework from version 5.3.0 to 5.3.18 or higher.
* **Conduct a comprehensive audit** of all internal dependencies to identify other vulnerable instances.
* **Review and enhance** automated patch management workflows for critical security libraries.

---

## Conclusion
By rapidly identifying the exploit pattern and deploying WAF rules, the immediate threat was neutralized. However, a full library upgrade is required to ensure long-term stability and security.
