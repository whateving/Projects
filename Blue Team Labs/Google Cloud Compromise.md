A Project ID is the globally unique identifier for a Google Cloud project. While you might give your project a friendly name (like "My Startup App"), the Project ID is what the system uses behind the scenes to distinguish your resources from every other project in existence.
Key Characteristics of a Project ID
Globally Unique: No two projects in the entire Google Cloud ecosystem can share the same Project ID.

Immutable: Once a project is created, its Project ID cannot be changed.

Human-Readable: Unlike the "Project Number" (which is just a long string of digits), the Project ID is alphanumeric and usually contains words related to your project (e.g., secret-code-startup-4421).

Visibility: It appears in resource names, URLs (like Cloud Storage bucket names), and, most importantly for your investigation, in Cloud Logging entries.


## 1. The project that was compromised can be seen in the screenshot down below after the command have been run:

<img width="1172" height="496" alt="image" src="https://github.com/user-attachments/assets/b7d86153-7d27-49ff-a7fb-d836db73ea62" />

## 2. The following identity was compromised

<img width="1172" height="381" alt="image" src="https://github.com/user-attachments/assets/46c31793-bcc5-4cd0-ae90-a19fd4ce5a2d" />

as you can see this email is associated with the following activities coming from the following IP which belong to Romania and user agent.

<img width="889" height="381" alt="image" src="https://github.com/user-attachments/assets/5a2a0a29-d6fb-4504-8785-959bd18494a8" />

## 3. Looks like the attack initiated from a MacBook 

<img width="1156" height="442" alt="image" src="https://github.com/user-attachments/assets/e84a7875-2cb3-4926-a51a-38b7f1e28dde" />

## 4. There was a failed API call that was made as you can see from the screenshot below:

<img width="1023" height="555" alt="image" src="https://github.com/user-attachments/assets/63a7de81-a4c3-4b71-bd3e-a41e43d60f62" />

What This API Call Means
The attacker was attempting to enable the Google Compute Engine API (compute.googleapis.com) to start creating Virtual Machines (VMs).

Why they did this: Given the scenario of a "greedy developer" and the project name "cryptostartup," the attacker likely intended to spawn illicit virtual machines to mine cryptocurrency on the company's dime.

Why it failed: The log shows a message: "Permission denied to enable service [compute.googleapis.com]" (Line 207). The compromised identity (cloud-storage-helper) likely only had permissions for Storage, not for managing Compute resources.


## 5. A bucket named "importantbucket' was enumerated by using the storage.buckets.list API call:

<img width="738" height="798" alt="image" src="https://github.com/user-attachments/assets/4e84bcd2-6a3c-4abc-9c42-6a9b585dffac" />


## 6. An item was exfiltrated from the bucket by using the API called storage.objects.get:

<img width="738" height="798" alt="image" src="https://github.com/user-attachments/assets/2fff0e45-f043-46ce-b6ef-3f7576df5c5b" />

## 7. Google command line tool, gsutil, was used during the exfiltration attempt as can be seen from the screenshot above

## 8. secretcode.java file was exfiltrated as can also be seen from the screenshot above. 
