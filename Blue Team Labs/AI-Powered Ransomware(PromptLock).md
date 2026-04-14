# PromptLock Ransomware:




1. I first pushed the .exe file through the strings function on CyberChef, after analyzing the readable text, I saw that the Lua language was used
as a code generator.

<img width="937" height="590" alt="image" src="https://github.com/user-attachments/assets/0caa59f2-12e2-45f5-95ec-6d0cc381ae12" />

2. I then looked for the version of go programming language used in this ransomware:

<img width="937" height="590" alt="image" src="https://github.com/user-attachments/assets/a44e4c5c-63b2-458a-a082-955ceaa6b455" />

3. I also found that the LLM was assigned the role of a "cybersecurity expert" to summarize the information which was found for each file and
determine if there is sensitive information or PII in these files.

<img width="937" height="590" alt="image" src="https://github.com/user-attachments/assets/f07c8306-dce2-4eaf-a053-3c00d1ac2086" />

4. Investigating this further, I also found that the PromptLock ransomware connect to the following IP address:

<img width="937" height="590" alt="image" src="https://github.com/user-attachments/assets/4ee74fb0-a0bd-457b-aa9b-a1e69e8def99" />

5. I found that the the PromptLock uses is gpt_oss:20b:

<img width="660" height="471" alt="image" src="https://github.com/user-attachments/assets/c4854fd8-256e-41ec-a1ae-a2c3b563bb46" />

6. The encryption algorithm promptlock uses is SPECK 128-bit:

<img width="974" height="471" alt="image" src="https://github.com/user-attachments/assets/4c92b3f9-1364-43b1-ab89-54be0f2e63e0" />


7. The following was the bitcoin address found embedded into the binary:

<img width="974" height="471" alt="image" src="https://github.com/user-attachments/assets/d34bdfd4-9ee0-46e0-bfa3-188b230b77d4" />


8. The following is the list of files to encrypt:

<img width="745" height="455" alt="image" src="https://github.com/user-attachments/assets/37702d30-128b-4015-b2bb-f2a023eadbde" />
