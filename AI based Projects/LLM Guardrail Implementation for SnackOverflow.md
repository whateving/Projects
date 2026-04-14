# SnackOverflow LLM Guardrails

## Securing the SnackOverflow Chatbot: A Guardrails Challenge Writeup

For this challenge, I was “hired” by the CEO of **SnackOverflow** (a competitor to PacketSnacc) to secure their brand-new AI chatbot. The bot has access to external plugins to fetch information, making it a prime target for **Prompt Injection**, **Denial of Service (DoS)**, and **Cross-Site Scripting (XSS)** attacks.

My objective was to write two robust application-layer guardrails in Python: one to sanitize user input before it reaches the LLM, and one to validate the LLM's output before it reaches the user.

Here is a breakdown of how I approached and solved the challenge.

---

## Phase 1: The Input Guardrail

The input guardrail needed to enforce three strict rules to prevent malicious prompts from manipulating the model:

1.  **Prevent competitor interaction:** Block any prompt containing the domain `packetsnacc.local`.
2.  **Character Allowlist:** Silently remove all special characters except for `.:/-_@`.
3.  **DoS Prevention:** Truncate any prompt exceeding 512 characters.

### My Strategy:
I realized that the order of operations here was critical. If a user submitted a prompt like `packet!snacc.local`, and I stripped the special characters first, the resulting string would become `packetsnacc.local` and potentially bypass a single domain check.

To prevent this, I implemented a double-check system:
* Checked for the blacklisted domain immediately.
* Used a **Regular Expression** to strip out any character that wasn't alphanumeric, whitespace, or on the approved special character list.
* Checked for the blacklisted domain again just in case the regex stripping accidentally formed the forbidden word.
* Sliced the string using standard Python indexing to enforce the hard length limit.

---

## Phase 2: The Output Guardrail

The output guardrail was designed to ensure the LLM didn't return broken data, malicious links, or XSS payloads. The requirements were:

1.  The response must be valid **JSON**.
2.  It must contain the keys `"type"` (strictly `"text"` or `"url"`) and `"response"`.
3.  If the type is `"url"`, the response must be a valid **HTTP/HTTPS** link.
4.  If the type is `"text"`, the response must be **HTML-encoded** to stop XSS.

### My Strategy:
I approached this as a strict data validation pipeline:
* **JSON Parsing:** I wrapped the JSON loading function in a `try-except` block to immediately catch and reject hallucinated or malformed formats.
* **Schema Validation:** I verified the parsed data was a dictionary and explicitly checked for the required keys and acceptable type values.
* **URL Validation:** For URLs, I first split the string to verify the scheme was strictly `http` or `https` (preventing local file inclusion tricks). Then, I passed it through a URL validator library to ensure the overall URL structure was sound.
* **XSS Sanitization:** For standard text, I used Python's native HTML escape function to neutralize dangerous characters like brackets by converting them into safe HTML entities.

---

## The Final Payload

Here is the final, working Python script that successfully satisfied all constraints and secured the application:

```python
import re
import json
import html
import validators

def input_guardrail(prompt: str) -> str:
    # 1. Initial check for competitor domain
    if "packetsnacc.local" in prompt:
        raise GuardrailException("Invalid URL")
    
    # 2. Strip unapproved special characters using Regex
    prompt = re.sub(r'[^a-zA-Z0-9\s\.\:\/\-\_\@]', '', prompt)
    
    # 3. Secondary check to prevent evasion via character stripping
    if "packetsnacc.local" in prompt:
        raise GuardrailException("Invalid URL")
    
    # 4. Enforce DoS protection limit
    return prompt[:512]

def output_guardrail(response: str) -> str:
    # 1. Validate JSON structure
    try:
        data = json.loads(response)
    except Exception:
        raise GuardrailException("Invalid JSON")
    
    # 2. Validate Schema and Keys
    if not isinstance(data, dict) or "type" not in data or "response" not in data:
        raise GuardrailException("Invalid JSON")
    
    if data["type"] not in ["text", "url"]:
        raise GuardrailException("Invalid JSON")
    
    # 3. URL Validation Pipeline
    if data["type"] == "url":
        url = str(data["response"])
        if "://" in url:
            scheme = url.split("://")[0].lower()
            if scheme not in ["http", "https"]:
                raise GuardrailException("Invalid URL scheme")
        
        if not validators.url(url):
            raise GuardrailException("Invalid URL")
    
    # 4. Text Sanitization (XSS Prevention)
    elif data["type"] == "text":
        data["response"] = html.escape(str(data["response"]))
    
    # Return safe JSON
    return json.dumps(data)
```

---

## Conclusion

By combining strict regex allowlisting on the input side with rigid schema validation and HTML escaping on the output side, the chatbot was successfully secured against the primary attack vectors.

<img width="545" height="296" alt="image" src="https://github.com/user-attachments/assets/1f7b73b5-b00c-4f1d-a371-346843279101" />
