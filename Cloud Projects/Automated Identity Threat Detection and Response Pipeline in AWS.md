# Automated Identity Threat Detection and Response Pipeline in AWS

## Project Overview
In modern cloud environments, identity is the ultimate perimeter. Relying on manual human intervention after a credential leak is mathematically too slow. To solve this, I built a fully automated, serverless Identity Threat Detection and Response pipeline in AWS. The system detects unauthorized actions from compromised credentials in real time and automatically isolates the threat by attaching a custom "Deny All" policy to the user within milliseconds. 

I engineered this entire solution to be highly scalable and entirely serverless. By utilizing event-driven architecture, the pipeline incurs absolutely zero baseline cost and runs highly efficiently, proving that enterprise-grade security automation does not require a massive infrastructure budget.

## Architecture and Tools
* **AWS CloudTrail:** The security camera, auditing all API calls across the account.
* **Amazon EventBridge:** The tripwire, filtering logs for specific unauthorized actions.
* **AWS Lambda (Python/Boto3):** The automated security response, executing the containment logic.
* **AWS IAM:** The access control mechanism, utilizing strict least privilege execution roles and custom managed policies.

<img width="1408" height="768" alt="image" src="https://github.com/user-attachments/assets/a07bec58-a848-4d30-af68-4fc2946457d1" />


## The Execution

### 1. Establishing the Perimeter and the Target
I started by creating an administrative audit trail in CloudTrail to monitor all API activity within the Stockholm region. Next, I provisioned a dummy IAM user named "compromised-hacker" with limited Read Only access. This simulated an employee whose credentials had been leaked. 

<img width="1455" height="600" alt="Screenshot 2026-04-27 at 11 07 25 AM" src="https://github.com/user-attachments/assets/f3eb1c6e-42c0-4bab-a6b9-39d8cbc11d84" />

### 2. Forging the Containment Policy
To isolate a threat, the system needs an absolute kill switch. I authored a custom IAM policy named "AwsDenyA". This policy utilizes a strict wildcard statement to explicitly deny all actions across all resources. In AWS IAM evaluation logic, an explicit Deny always overrides any Allow, making this the perfect containment mechanism.

<img width="1149" height="618" alt="image" src="https://github.com/user-attachments/assets/8c924db7-3770-4312-8af1-7121323a93eb" />


### 3. Engineering the Serverless Response
I deployed a Python-based Lambda function to act as the automated responder. To adhere to the Principle of Least Privilege, I did not give Lambda full administrative rights. Instead, I crafted a highly restricted inline IAM policy for the Lambda execution role. Using the "ArnLike" condition key, I mathematically restricted the function so it was only legally allowed to attach my specific "AwsDenyA" policy, completely preventing privilege escalation.

The Python script uses the Boto3 library to parse the incoming threat data, extract the exact username of the attacker dynamically, and execute the IAM policy attachment.

<img width="759" height="762" alt="image" src="https://github.com/user-attachments/assets/02e1fea6-6136-49ae-97fe-81af76374ea2" />

```
import boto3
import logging

# Initialize logging for CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    iam = boto3.client('iam')
    
    try:
        # Define the exact ARN of the custom containment policy
        deny_policy_arn = "arn:aws:iam::123456789012:policy/AwsDenyA"
        
        # Parse the EventBridge JSON payload to extract the attacker's username dynamically
        user_name = event['detail']['userIdentity']['userName']
        logger.info(f"CRITICAL: Attack detected from user: {user_name}. Initiating lockdown.")
        
        # Execute the automated response by attaching the handcuffs
        iam.attach_user_policy(
            UserName=user_name,
            PolicyArn=deny_policy_arn
        )
        
        logger.info(f"SUCCESS: {user_name} has been isolated.")
        return {"statusCode": 200, "body": "Lockdown successful."}
        
    except Exception as e:
        logger.error(f"FAILED: {str(e)}")
        raise e
```
### 4. Setting the Event-Driven Tripwire
The most critical part of an ITDR pipeline is the detection logic. I configured an EventBridge rule to monitor CloudTrail for specific destructive API calls, such as "StopLogging" or "DeleteTrail". 

<img width="759" height="396" alt="image" src="https://github.com/user-attachments/assets/4d85fdd5-0438-494c-b247-cbf3f4d9e4fe" />


## The Attack Simulation

Before the environment priming:

<img width="720" height="31" alt="image" src="https://github.com/user-attachments/assets/02037acf-b4ab-421e-83af-dea6e3b02a72" />

As you can see I am able to read the available trails, this is, of course, by design. 

With the environment primed, I executed a simulated attack from my local terminal using the compromised credentials, attempting to blind the security cameras.

Command Executed:
`aws cloudtrail stop-logging --name ITDR-Audit-Trail --region eu-north-1`

The terminal returned an Access Denied exception. However, within milliseconds, the following automated sequence occurred:
1. CloudTrail logged the unauthorized "StopLogging" attempt.
2. EventBridge detected the "AccessDenied" error pattern and instantly invoked Lambda.
3. Lambda extracted the "compromised-hacker" username and applied the explicit deny policy.

Upon refreshing the AWS IAM Console, the threat was fully contained. 

<img width="720" height="157" alt="Screenshot 2026-04-27 at 11 16 38 AM" src="https://github.com/user-attachments/assets/4f1dbd45-5f91-462b-98c1-47f839d639d2" />
<img width="1149" height="283" alt="image" src="https://github.com/user-attachments/assets/f8a586c5-8d34-421b-8cef-65d71eccea49" />


## Key Engineering Takeaways
Building this pipeline from scratch reinforced several critical cloud security concepts:
* **Strict IAM Condition Keys:** I navigated the precise difference between "ArnEquals" and "ArnLike" when dynamically passing account IDs into resource constraints, ensuring the execution role was bulletproof.
* **Cost-Effective Security:** By keeping compute entirely serverless and relying on native AWS API integrations, I built a zero-cost, enterprise-grade response system.
