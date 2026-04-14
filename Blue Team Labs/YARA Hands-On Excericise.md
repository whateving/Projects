# YARA: Hands-on Exercises

**Tags:** #YARA #ThreatHunting #CTF #DefensiveEngineering

---

## Exercise 1: Basic Pattern Matching

**Objective:** Write a YARA rule to find the file that contains the exact pattern `THM{}`. 
**Target Directory:** `C:\TMP\Exercise1\`
**Goal:** Enter the flag found inside the file.

**My YARA Rule:**
```yara
rule Exercise1_Find_THM {
    meta:
        author = "MyVault"
        description = "Searches for the standard TryHackMe flag prefix."
    strings:
        $flag_prefix = "THM{"
    condition:
        $flag_prefix
}
```

<img width="723" height="87" alt="image" src="https://github.com/user-attachments/assets/53114cf9-8429-4572-b428-e2436310028c" />

<img width="723" height="206" alt="image" src="https://github.com/user-attachments/assets/c928fdbe-d6b3-457c-9cd5-e855891f66ab" />


## Exercise 2: Multiple Strings

**Objective:** Write a YARA rule that finds the file containing both of the following strings: `Yet another` AND `Ridiculous acronym`.
**Target Directory:** `C:\TMP\Exercise2\`
**Goal:** Identify the name of the file.

**My YARA Rule:**

```yara
rule Exercise2_Multiple_Strings {
    meta:
        author = "Me"
        description = "Searches for two specific text strings within the same file."
    strings:
        // Adding 'wide' and 'ascii' searches for both 1-byte and 2-byte encodings.
        $string1 = "Yet another" nocase wide ascii
        $string2 = "Ridiculous acronym" nocase wide ascii
    condition:
        all of them 
}

```

<img width="723" height="206" alt="image" src="https://github.com/user-attachments/assets/b3c91f6b-deb0-43f5-b1f5-c89c2959509a" />



## Exercise 3: Base64 Encoding

**Objective:** Write a YARA rule that searches for the file containing the base64 encoded string `THM{This was a really fun exercise}`.
*Hint: Remember the specific modifier needed in the strings section.*
**Target Directory:** `C:\TMP\Exercise3\`
**Goal:** Identify the name of the file.

**My YARA Rule:**

```yara
rule Exercise3_Base64 {
    meta:
        author = "Me"
        description = "Searches for a specific base64 encoded string."
    strings:
        // The base64 modifier automatically encodes the string at runtime to find the match.
        $b64_string = "THM{This was a really fun exercise}" base64
    condition:
        $b64_string
}
```

<img width="723" height="206" alt="image" src="https://github.com/user-attachments/assets/1debaf16-5248-4b90-b07d-001e03303ba1" />




## Exercise 4: XOR Encryption & Recursive Searching

**Objective:** Write a YARA rule that searches for the XOR encrypted string `THM{FoundSomethingHidden}`.
*Hint: You will need to search recursively and use a specific command-line flag to print the XOR key and plaintext.*
**Target Directory:** `C:\TMP` directory AND subdirectories.
**Goal:** Identify the encrypted text and the XOR key used.

**My YARA Rule:**

```yara
rule Exercise4_XOR {
    meta:
        author = "Me"
        description = "Searches for an XOR encrypted string with a 1-byte key."
    strings:
        // The xor modifier checks all 255 possible 1-byte XOR keys.
        $xor_string = "THM{FoundSomethingHidden}" xor
    condition:
        $xor_string
}
```

<img width="723" height="206" alt="image" src="https://github.com/user-attachments/assets/470936a6-3766-4544-a91e-163db1c480db" />


