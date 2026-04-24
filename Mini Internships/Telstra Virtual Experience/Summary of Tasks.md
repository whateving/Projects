# Security Operations Center (SOC) Incident Response Summary

## Task 1: Malware Incident Triage and Initial Response
**Objective:** Respond to an active malware attack by identifying affected critical infrastructure and initiating incident response via appropriate team notification.

### Steps Completed:
* **Triage:** Reviewed firewall logs to identify infrastructure under attack, prioritizing critical services utilizing the Spring Framework to assess the immediate impact on company operations.
* **Coordination:** Determined the appropriate incident response team based on the severity and affected infrastructure priority.
* **Communication:** Drafted a concise and contextual email to the relevant team, conveying the urgency of the situation and including key details such as the incident timestamp and affected infrastructure to prepare them for mitigation efforts.


---

## Task 2: Attack Vector Analysis and Mitigation Strategy
**Objective:** Analyze firewall logs to identify non-IP-based patterns in attacker network requests to deduce the characteristics of the Spring4Shell vulnerability being exploited, as IP blocking was ineffective due to the distributed attack nature.

### Analysis and Findings:
* **Log Review:** Examined firewall logs for recurring patterns, focusing on anomalies in HTTP methods, payload structures, headers, and user agents associated with exploitation attempts.
* **Vulnerability Identification:** Confirmed the adversary was exploiting the Spring4Shell vulnerability (**CVE-2022-22965**), which allows Remote Code Execution (RCE) via untrusted data binding in the Spring Framework (v5.3.0). The immediate mitigation requirement was identified as updating to at least v5.3.18.
* **Communication Improvement:** The initial email drafted to the Networks Team, which requested the development of a non-IP-based firewall rule, should have explicitly specified the identified attack characteristics for effective blocking: `ClientRequestPath` (`/tomcatwar.jsp`) and exploit-specific Headers (`suffix=%>// c1=Runtime c2=<% DNT=1 Content-Type=application/x-www-form-urlencoded`).


---

## Task 3: Implementation and Documentation
**Objective:** Implement an immediate, non-IP-based mitigation firewall rule and formally document the incident.

### Actions:
* **Rule Implementation:** Implemented a firewall rule using Python (via a POST function) to block requests that match the identified attack vector (specifically checking for the request path `/tomcatwar.jsp` and the outlined headers). The complete implementation file is available in the project directory.
* **Postmortem:** Completed and submitted a postmortem report detailing the entire incident response process, analysis, and mitigation steps (file location noted).
