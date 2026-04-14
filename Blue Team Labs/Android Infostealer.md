A user downloads what appears to be a legitimate mobile app from an app store. The app seems to work fine and doesn't raise any suspicion, but in the background, it silently installs an Android info stealer malware on the user's device.

The malware is designed to collect a wide range of sensitive information from the device, including call logs, SMS messages, contacts, browsing history, and location data. It may also be able to take screenshots, record audio or video, and access the device's camera.

Try to reverse it and help this user with information.


# What is the package name for the app?

I put the file through jadx-gui, and read the AndroidManifest.xml

Answer: com.example.appcode.appcode

<img width="982" height="676" alt="image" src="https://github.com/user-attachments/assets/61e42a32-3ecb-4e6b-8fd8-13deced5532c" />


# What is the name of the background service declared in the manifest?

Answer: com.example.appcode.appcode.CMDService

This service is a critical point of interest for your investigation. Here is why:

It's the Engine: In Android malware, Activities (like MainActivity) are often just decoys to look normal. The Service is what runs in the background to perform the actual malicious work (stealing data, recording audio, etc.) without a UI.

Naming Convention: The name CMDService strongly suggests "Command Service," implying this is likely where the malware interprets commands received from the attacker (C2 server).

<img width="982" height="676" alt="image" src="https://github.com/user-attachments/assets/ed4e6bc7-a884-4d68-934f-017fbea3fd81" />

# Which permission allows an app to access information about Wi-Fi networks?

The permission that specifically allows the app to access information about Wi-Fi networks is: android.permission.ACCESS_WIFI_STATE

<img width="982" height="676" alt="image" src="https://github.com/user-attachments/assets/c8896b7e-fc87-4429-8675-3ca0b2fda7b4" />


# What permission is needed for an app to determine its approximate location using network-based methods?

The permission that allows the app to determine its approximate (network-based) location is:

android.permission.ACCESS_COARSE_LOCATION

<img width="982" height="676" alt="image" src="https://github.com/user-attachments/assets/ac03fbbd-74ca-479d-aec3-f9d0a9f98f79" />

# What is the name of the method that retrieves the call log information?

<img width="982" height="676" alt="image" src="https://github.com/user-attachments/assets/36d39990-404c-4e8d-9aeb-b693d6501499" />


# During the analysis of the “CallLogLister” class. What the number of fields are included in the call log information? 

7, as can be seen in the screenshot above.

# What command should be used to get SMS data?

<img width="1027" height="739" alt="image" src="https://github.com/user-attachments/assets/5b2505f3-b7e4-45c4-8e63-a4302a7347cc" />


# Which command is used to update the malware app?

<img width="543" height="181" alt="image" src="https://github.com/user-attachments/assets/90fe2e9a-91cc-4e95-b24e-1f67a2b7c898" />


# What command is used to take screenshots?

<img width="1027" height="739" alt="image" src="https://github.com/user-attachments/assets/a27e7528-44be-4556-8fca-de9df90cfed6" />


# Which command is used to record from the microphone?

<img width="1027" height="739" alt="image" src="https://github.com/user-attachments/assets/d11174b7-b8b4-4d11-9ae6-e15f2926da55" />

# What is the C2 server which is used by malware to send stolen device system?

<img width="1027" height="739" alt="image" src="https://github.com/user-attachments/assets/e3fa1103-ab63-4c78-a940-d39a26082fc7" />
