# Enterprise DevSecOps Pipeline: End-to-End Security Automation
**Tech Stack:** Python (Flask), Docker, GitHub Actions, Gitleaks, Bandit, Trivy

## Executive Summary
This project demonstrates a production-grade **DevSecOps "Fail-Fast" Pipeline**. The goal was to move security "Left" in the development lifecycle, ensuring that secrets, insecure code patterns, and vulnerable infrastructure are caught automatically before deployment.

### Key Security Achievements:
* **Layer 1 (Secret Scanning):** Prevented credential leakage using **Gitleaks**.
* **Layer 2 (SAST):** Identified Remote Code Execution (RCE) and insecure configurations using **Bandit**.
* **Layer 3 (SCA/Container Security):** Detected OS-level vulnerabilities in Docker base images using **Trivy**.

---

## The Architecture (The "Fail-Fast" Loop)
The pipeline is designed to save corporate compute costs by stopping the build immediately if a high-priority vulnerability is found.

### Pipeline Workflow:
1. **Secret Scan:** Scans the filesystem for API keys and tokens.
2. **SAST:** Analyzes the Python source code for logic flaws.
3. **Container Build:** Packages the app into a Docker image.
4. **SCA Scan:** Scans the final image for known CVEs (Common Vulnerabilities and Exposures).

---

## Layer 1: Secret Detection (Gitleaks)
**Scenario:** A developer accidentally commits a Google API Key to the source code.
**Result:** Gitleaks identified the high-entropy string and blocked the push.

> <img width="1032" height="561" alt="image" src="https://github.com/user-attachments/assets/1e05cfdf-5c0c-49b5-a592-c88acd528dda" />

---

## Layer 2: Static Analysis (Bandit)
**Scenario:** The application contained a dangerous `eval()` function, allowing for potential Remote Code Execution.
**Remediation:** Replaced `eval()` with safe integer parsing and restricted the Flask host from `0.0.0.0` to `127.0.0.1`.

> <img width="1032" height="561" alt="image" src="https://github.com/user-attachments/assets/59a4cf6a-1366-4c3d-a762-dddc6cc58a0e" />

---

### Layer 3: Container Security & Hardening (SCA)
**Scenario:** The application was initially built using an outdated `python:3.9.0` image running as the `root` user.

**Detection & Remediation:**
1.  **Vulnerability Scanning:** **Trivy** identified 3 HIGH severity vulnerabilities in the base OS. 
    * *Fix:* Migrated to `python:3.12-slim`, which cleared all critical OS vulnerabilities.
2.  **The Principle of Least Privilege:** An audit revealed the container was running with `root` privileges, creating a massive risk for container breakout.
    * *Fix:* Modified the Dockerfile to create a non-privileged system user (`appuser`). The application now runs with the minimum permissions required to function.


> <img width="1470" height="778" alt="image" src="https://github.com/user-attachments/assets/142cae42-7430-4dbb-b1b7-eb1fa8020a3e" />

> <img width="1470" height="383" alt="image" src="https://github.com/user-attachments/assets/62bfb033-e507-4360-b1a2-cc85702f1b86" />



---

## Final State: Secured & Verified
After remediation, the pipeline successfully passes all layers, ensuring the code and infrastructure are hardened.

> <img width="1032" height="561" alt="image" src="https://github.com/user-attachments/assets/41863eff-7133-4413-8a36-f06a729b6f24" />


---

## Code Reference

### The Secured `app.py`
```python
from flask import Flask, request
import html

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    user_input = request.args.get('math_expression', '0')
    try:
        # Safe integer conversion instead of eval()
        result = int(user_input) * 2
        return f"The doubled result is: {result}"
    except ValueError:
        return "Invalid input.", 400

if __name__ == '__main__':
    # Hardened local host
    app.run(host='127.0.0.1', port=5000)
```

### The Hardened `Dockerfile`
```dockerfile
# Using a slim base image to reduce attack surface
FROM python:3.12-slim

# Create a non-privileged user for security
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# Copy files and change ownership to our new user
COPY --chown=appuser:appgroup . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the non-root user
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
```

### The DevSecOps YAML (`.github/workflows/security-pipeline.yml`)
```yaml
name: Enterprise DevSecOps Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  security-scans:
    runs-on: ubuntu-latest

    steps:
      # --- PREPARATION ---
      - name: Checkout Code
        uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      # --- LAYER 1: SECRET SCANNING ---
      - name: Layer 1 - Scan for Hardcoded Secrets
        uses: gitleaks/gitleaks-action@v2
        with:
          args: detect --source . --verbose --redact
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      # --- LAYER 2: SAST (STATIC ANALYSIS) ---
      - name: Layer 2 - Install Bandit
        run: pip install bandit

      - name: Layer 2 - Run SAST Scan
        run: bandit -r . -ll -ii

      # --- LAYER 3: SCA & CONTAINER SECURITY ---
      - name: Layer 3 - Build Docker Image
        run: docker build -t enterprise-app:latest .

      - name: Layer 3 - Run Trivy Vulnerability & Misconfig Scan
        uses: aquasecurity/trivy-action@57a97c7e7821a5776cebc9bb87c984fa69cba8f1
        with:
          image-ref: "enterprise-app:latest"
          format: "table"
          exit-code: "1"
          ignore-unfixed: true
          # ADDED 'misconfig' here to catch the root user issue
          scanners: "vuln,misconfig"
          severity: "CRITICAL,HIGH"
```



