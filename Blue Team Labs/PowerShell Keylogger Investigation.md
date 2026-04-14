# LetsDefend Challenge Write-up: PowerShell RAT Analysis
 
**Category:** Malware Analysis / Script Analysis  
**Platform:** LetsDefend  

---

## ⚠️ Spoiler Warning
This post contains solutions and detailed analysis for a specific LetsDefend challenge. I highly recommend attempting the investigation yourself before reading the answers below to maximize your learning experience.

---

## Scenario Overview
In this challenge, we are tasked with analyzing a suspicious PowerShell script found on a compromised machine. The script acts as a Remote Access Trojan (RAT), allowing an attacker to execute commands, capture screenshots, and log keystrokes. It utilizes the Tor network (via a SOCKS5 proxy) to communicate with a hidden C2 server.

---

## Investigation & Answers

### 1. What is the proxy port used by the script?

**Answer:** `9050`

**Analysis:**
At the very top of the script, the parameters define the connection details. The `$proxyPort` variable is explicitly set to `9050`, which is the default listening port for the Tor service.

**Code Reference:**
```powershell
[int]$proxyPort = 9050

```

<img width="962" height="100" alt="image" src="https://github.com/user-attachments/assets/fdf7fdde-3551-4b97-aee3-0a1f17f9cfe3" />

---

### 2. What function-method is used for starting keylogging?

**Answer:** `Start-Keylogger`

**Analysis:**
The script defines a specific function named `Start-Keylogger`. This function sets up the necessary Windows API imports (P/Invoke) and initializes a background job to poll for keystrokes.

**Code Reference:**

```powershell
function Start-Keylogger {
    $global:keylogger_active = $true
    $global:captured_keys = ""
    # ... (API definitions)
}

```

<img width="962" height="491" alt="image" src="https://github.com/user-attachments/assets/7b9890b6-e527-4a0f-b84f-e069ea4eff6e" />


---

### 3. What is the name of the file used by the script to store the keylog data?

**Answer:** `keylog.txt`

**Analysis:**
Inside the `Start-Keylogger` job logic, specifically within the loop that captures the keystrokes, the script appends the captured data to a file named `keylog.txt` located in the user's temporary directory (`$env:temp`).

**Code Reference:**

```powershell
[System.IO.File]::AppendAllText("$env:temp\keylog.txt", $mychar, [System.Text.Encoding]::Unicode)

```


---

### 4. What command is used by the script to achieve persistence?

**Answer:** `persist`

**Analysis:**
The script listens for specific commands from the C2 server. One of these commands is `persist`. However, in this version of the script, the logic is incomplete or managed externally, as it simply returns a message stating "Persistence mechanism is managed separately."

**Code Reference:**

```powershell
elseif ($command -eq "persist") {
    # Implémentez la logique de persistance ici si nécessaire
    $writer.WriteLine("Persistence mechanism is managed separately")
}

```

<img width="962" height="491" alt="image" src="https://github.com/user-attachments/assets/0c42c716-5f64-42d1-aee0-e7d4872d4264" />


---

### 5. What is the command used by the script to upload data?

**Answer:** `upload:`

**Analysis:**
The script parses incoming commands to check for the prefix `upload:`. If found, it splits the string to extract the destination file path and the Base64-encoded file content, then writes the file to the disk.

**Code Reference:**

```powershell
elseif ($command.StartsWith("upload:")) {
    $parts = $command.Split(":")
    $filePath = $parts[1]
    # ...
}

```

<img width="962" height="491" alt="image" src="https://github.com/user-attachments/assets/d05de133-1a9d-451d-aabb-cbaed69414bd" />

---

### 6. What is the regex used by the script to filter IP addresses?

**Answer:** `^(127\.|169\.254\.)`

**Analysis:**
In the `Get-SystemInfo` function, the script gathers system details to send to the attacker. It attempts to find the machine's LAN IP address by filtering out loopback (`127.x`) and APIPA (`169.254.x`) addresses using this specific regex.

**Code Reference:**

```powershell
Where-Object { $_.AddressFamily -eq "IPv4" -and $_.IPAddress -notmatch "^(127\.|169\.254\.)" }

```


---

### 7. What is the DLL imported by the script to call keylogging APIs?

**Answer:** `user32.dll`

**Analysis:**
PowerShell cannot natively capture global keystrokes. The script uses C# `DllImport` syntax to load functions from `user32.dll` (such as `GetAsyncKeyState` and `GetKeyboardState`) to interact with the hardware input layer.

**Code Reference:**

```csharp
[DllImport("user32.dll", CharSet=CharSet.Auto, ExactSpelling=true)]
public static extern short GetAsyncKeyState(int virtualKeyCode);

```

<img width="962" height="491" alt="image" src="https://github.com/user-attachments/assets/a68cad12-a1fc-4f0f-a56f-0cf12a694eeb" />

---

### 8. How many seconds does the script wait before re-establishing a connection?

**Answer:** `60`

**Analysis:**
In the `Establish-Connection` function, a `try-catch` block handles network errors. If the connection fails or drops, the script catches the error and explicitly waits 30 seconds before the loop repeats to attempt a reconnection.

**Code Reference:**

```powershell
catch {
    Write-Error "Connection error: $_"
    # ...
    Start-Sleep -Seconds 60  # Attendre avant de tenter une reconnexion
}

```

---

## Conclusion

This script demonstrates a typical "Stage 2" payload. It relies on standard protocols (SOCKS5) to hide its traffic and utilizes "Living off the Land" techniques (PowerShell, .NET) to perform surveillance without needing to drop extra binaries for the keylogger.

**Defensive Recommendations:**

1. **Network Monitoring:** Alert on traffic to port `9050` or known Tor exit node traffic.
2. **File Integrity:** Monitor the `%TEMP%` directory for suspicious file creation (`.txt` logs or rapid `.png` creation/deletion).
3. **PowerShell Logging:** Enable Script Block Logging (Event ID 4104) to capture the execution of decoded Base64 commands and P/Invoke calls.





