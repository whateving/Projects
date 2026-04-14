# A new SIA secret agent transforms into a fearless hacktivist by spilling his country's most heinous secrets to the world.

## AWS CloudTrail is a service that provides a detailed, immutable log of actions (API calls) taken by users, roles, or AWS services within your account, crucial for governance, compliance, security monitoring, and troubleshooting by answering "who did what, where, and when". It records events from the AWS Management Console, SDKs, and Command Line Tools, offering insights into resource changes and access patterns for operational auditing and risk management. 

## An Amazon Resource Name (ARN) in AWS is a unique identifier for an individual resource, like an EC2 instance, S3 bucket, or IAM user, used for unambiguous identification across the AWS cloud, especially in IAM policies and API calls to grant fine-grained permissions

## 1. I first identified the name of the IAM username used by the SIA agent (agentdarius):

<img width="723" height="92" alt="image" src="https://github.com/user-attachments/assets/6f0598fb-cf65-4f18-b931-f7b3320885ec" />


## 2. Then I identified the source IP from where the SIA agent was authenticating:

<img width="723" height="114" alt="image" src="https://github.com/user-attachments/assets/d3839da6-a8ac-4afb-9777-33cb418ec0d6" />

## 3. Activities related to enumerating identities and permissions (GetCallerIdentity,ListUserPolicies,ListAttachedUserPolicies,GetPolicy):

<img width="723" height="433" alt="image" src="https://github.com/user-attachments/assets/f479dbb6-2e7d-4b16-93af-1a958a37465a" />

## 4. They tried to establish persistence by creating a user, as you can see from the screenshot in point 3.


## 5. The SIA agent had the following managed policy:

<img width="723" height="132" alt="image" src="https://github.com/user-attachments/assets/817f237e-d112-4a57-adc7-6e89389b856f" />

## 6. The attacker also enumerated S3 buckets as can be seen from the screenshot in point 3 and they performed this by running ListBuckets and ListObjects. ListBuckets (Enumerates all buckets in the account). ListObjects (Enumerates the files inside specific buckets)

## 7. A bucket was tempered with and its ARN is as follows arn:aws:s3:::siasecrets

<img width="723" height="132" alt="image" src="https://github.com/user-attachments/assets/b092164e-4892-4694-9478-af6ed671cabb" />


## 8. He removed the "Block Public Access" setting (DeleteBucketPublicAccessBlock). He manually changed the permissions of the object (PutObjectAcl) to make it readable by everyone.

<img width="723" height="230" alt="image" src="https://github.com/user-attachments/assets/39bab55c-4726-497b-b523-1d59a82ad9e1" />
