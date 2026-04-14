**Objective:**
For this project, I developed an Anomaly Detection system designed to identify malicious network traffic. My goal was to build a robust model capable of distinguishing between normal user activity and security breaches (such as intrusions or denial-of-service attacks) by analyzing network log data.

---

## 1. Model Architecture: Why I Chose Random Forests 

To handle the complexity of high-dimensional network data, I selected the **Random Forest** algorithm.

### Design Rationale
I chose Random Forest over a single Decision Tree or simpler linear models for three specific reasons:
1.  **Ensemble Power:** Instead of relying on a single "expert," I wanted to aggregate the decisions of multiple trees to reduce the risk of errors.
2.  **Handling High Dimensions:** Network logs have many features (protocols, byte counts, flags). Random Forests handle this volume efficiently without overfitting.
3.  **Robustness:** By using majority voting, the model remains stable even if individual trees are sensitive to noise in the data.

### Implementation Logic
In my implementation, I relied on the three core pillars of the Random Forest architecture:
* **Bootstrapping:** I ensured diversity in the model by training each tree on different random subsets of the data (sampling with replacement).
* **Feature Randomness:** At each split in the tree, I restricted the model to consider only a random subset of features. This forced the trees to learn independent patterns rather than relying on one dominant feature.
* **Voting Mechanism:** For the final classification, I utilized a majority vote system if 80 out of 100 trees classify a packet as "Attack," the system flags it as an attack.



---

## 2. The Dataset: NSL-KDD 

I utilized the **NSL-KDD** dataset as my primary data source.

**Why this dataset?**
While the original KDD Cup 1999 dataset is famous, it suffers from severe issues like duplicate records and class imbalance. I chose NSL-KDD because it resolves these redundancy issues, providing a cleaner, more realistic benchmark for evaluating my Intrusion Detection System (IDS).

**Scope:**
The dataset provided me with labeled instances of:
* **Normal Traffic:** Standard user behavior.
* **Attacks:** Various malicious activities (DoS, Probe, U2R, R2L).

---

## 3. Technical Implementation 


### Step 1: Environment Setup

I set up my Data Science stack, importing `pandas` for data manipulation, `sklearn` for the Random Forest implementation and metrics, and `seaborn` for visualization.

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
```

### Step 2: Schema Definition & Loading

Since the raw data file (`KDD+.txt`) did not include headers, I manually defined the schema based on the dataset documentation. I mapped all 42 columns to ensure I could accurately analyze features like `src_bytes` (data sent) and `protocol_type`.

```python
# 1. Defining the file path
file_path = r'KDD+.txt'

# 2. Defining the feature map (Schema)
columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 
    'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 
    'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'attack', 'level'
]

# 3. Ingesting the data into a DataFrame
df = pd.read_csv(file_path, names=columns)

# 4. Verifying the structure
print(df.head())
```

<img width="1469" height="577" alt="image" src="https://github.com/user-attachments/assets/cdb80860-ca83-4f9e-a848-2883ea8f9152" />

# Project Phase 2: Preprocessing and Splitting the Dataset ⚙️

**Objective:**
After loading the NSL-KDD dataset, my next goal was to transform the raw network logs into a structured, numerical format that the Random Forest algorithm could interpret. This involved defining clear target variables, encoding categorical data, and rigorously splitting the data to prevent overfitting.

---

## 1. Creating the Binary Classification Target 

First, I needed a simple baseline: is the traffic safe or not? I created a binary target to distinguish purely between normal user activity and attacks.

**Implementation:**
I created a new column `attack_flag`. If the dataset labeled the traffic as `'normal'`, I assigned it a `0`. Any other label (indicating an attack) was assigned a `1`.

```python
# Binary classification target
# Maps normal traffic to 0 and any type of attack to 1
df['attack_flag'] = df['attack'].apply(lambda a: 0 if a == 'normal' else 1)
````

-----

## 2\. Creating the Multi-Class Classification Target 

While a simple alert is useful, I wanted my model to provide granular forensics. I decided to categorize the specific attack names into four major families: **DoS, Probe, Privilege Escalation,** and **Access** attacks.

**Implementation:**
I defined lists for each attack category based on the dataset documentation. Then, I wrote a mapping function to assign an integer ID to each row:

  * `0`: Normal
  * `1`: DoS
  * `2`: Probe
  * `3`: Privilege
  * `4`: Access

<!-- end list -->

```python
# Multi-class classification target categories
dos_attacks = ['apache2', 'back', 'land', 'neptune', 'mailbomb', 'pod', 
               'processtable', 'smurf', 'teardrop', 'udpstorm', 'worm']
probe_attacks = ['ipsweep', 'mscan', 'nmap', 'portsweep', 'saint', 'satan']
privilege_attacks = ['buffer_overflow', 'loadmdoule', 'perl', 'ps', 
                     'rootkit', 'sqlattack', 'xterm']
access_attacks = ['ftp_write', 'guess_passwd', 'http_tunnel', 'imap', 
                  'multihop', 'named', 'phf', 'sendmail', 'snmpgetattack', 
                  'snmpguess', 'spy', 'warezclient', 'warezmaster', 
                  'xclock', 'xsnoop']

def map_attack(attack):
    if attack in dos_attacks:
        return 1
    elif attack in probe_attacks:
        return 2
    elif attack in privilege_attacks:
        return 3
    elif attack in access_attacks:
        return 4
    else:
        return 0

# Assign multi-class category to each row
df['attack_map'] = df['attack'].apply(map_attack)
```

-----

## 3\. Encoding Categorical Variables 

The dataset contained text-based features like `protocol_type` (e.g., TCP, UDP) and `service` (e.g., HTTP). Since the Random Forest algorithm requires numeric input, I had to transform these.

**Implementation:**
I used One-Hot Encoding via `pd.get_dummies`. This created binary columns for every category, ensuring the model didn't infer any false ordinal relationships between the protocols.

```python
# Encoding categorical variables
features_to_encode = ['protocol_type', 'service']
encoded = pd.get_dummies(df[features_to_encode])
```

-----

## 4\. Selecting Numeric Features 

To capture the statistical properties of the traffic, I selected specific numeric columns. These included basic metrics like byte volume as well as derived rates (e.g., error rates) which are critical for detecting anomalies.

```python
# Numeric features that capture various statistical properties of the traffic
numeric_features = [
    'duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'urgent', 'hot', 
    'num_failed_logins', 'num_compromised', 'root_shell', 'su_attempted', 
    'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 
    'num_outbound_cmds', 'count', 'srv_count', 'serror_rate', 
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 
    'dst_host_srv_rerror_rate']
```

-----

## 5\. Preparing the Final Training Set 

I combined the newly encoded categorical features with the selected numeric features to create the final feature set (`train_set`). I also isolated the multi-class target variable (`multi_y`).

```python
# Combine encoded categorical variables and numeric features
train_set = encoded.join(df[numeric_features])

# Multi-class target variable
multi_y = df['attack_map']
```

-----

## 6\. Splitting the Dataset 

To ensure a robust evaluation, I implemented a two-stage split. This gave me three distinct datasets: **Training** (to teach the model), **Validation** (to tune it), and **Test** (to evaluate it).

**Step 1: Creating the Test Set**
I withheld 20% of the data for the final test.

```python
# Split data into training and test sets for multi-class classification
train_X, test_X, train_y, test_y = train_test_split(train_set, multi_y, test_size=0.2, random_state=1337)
```

**Step 2: Creating the Validation Set**
I took the remaining training data and split it again, reserving 30% of it for validation purposes.

```python
# Further split the training set into separate training and validation sets
multi_train_X, multi_val_X, multi_train_y, multi_val_y = train_test_split(train_X, train_y, test_size=0.3, random_state=1337)
```

<img width="1469" height="577" alt="image" src="https://github.com/user-attachments/assets/39e553de-1545-4755-8932-96c2fc123a12" />

# Project Phase 3: Training and Evaluation 

**Objective:**
With the data prepared and split, I moved to the core of the project: training the Random Forest algorithm. My goal was to teach the model to distinguish between normal traffic and the four specific attack categories (DoS, Probe, Privilege, Access) and then rigorously evaluate its performance using the Validation and Test sets.

---

## 1. Training the Model 

I initialized the `RandomForestClassifier`. I specifically set a `random_state` to ensure that my results are reproducible—meaning anyone running this code will get the exact same decision trees I did.

**Implementation:**
I fit the model using the `multi_train_X` (features) and `multi_train_y` (targets) subsets.

```python
# Train RandomForest model for multi-class classification
rf_model_multi = RandomForestClassifier(random_state=1337)
rf_model_multi.fit(multi_train_X, multi_train_y)
````

-----

## 2\. Evaluating on the Validation Set 

Before testing the model on the final "unseen" data, I evaluated it on the **Validation Set**. This intermediate step allows me to check if the model is learning correctly or if it is overfitting (memorizing the training data).

**Metrics Used:**

  * **Accuracy:** Overall correctness.
  * **Precision (Weighted):** How trustworthy the alerts are.
  * **Recall (Weighted):** How many attacks the model actually caught.
  * **F1-Score:** The balance between precision and recall.

**Visualization:**
I generated a **Confusion Matrix**. This is a heatmap that shows exactly where the model gets confused (e.g., "Did it mistake a DoS attack for Normal traffic?").

```python
# Predict and evaluate the model on the validation set
multi_predictions = rf_model_multi.predict(multi_val_X)
accuracy = accuracy_score(multi_val_y, multi_predictions)
precision = precision_score(multi_val_y, multi_predictions, average='weighted')
recall = recall_score(multi_val_y, multi_predictions, average='weighted')
f1 = f1_score(multi_val_y, multi_predictions, average='weighted')

print(f"Validation Set Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# Confusion Matrix for Validation Set
conf_matrix = confusion_matrix(multi_val_y, multi_predictions)
class_labels = ['Normal', 'DoS', 'Probe', 'Privilege', 'Access']
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_labels,
            yticklabels=class_labels)
plt.title('Network Anomaly Detection - Validation Set')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Classification Report for Validation Set
print("Classification Report for Validation Set:")
print(classification_report(multi_val_y, multi_predictions, target_names=class_labels))
```
<img width="1469" height="577" alt="image" src="https://github.com/user-attachments/assets/b6b58daa-0e20-4170-bbed-2dd434249fd6" />

-----

## 3\. Final Testing on Unseen Data 

Once I was satisfied with the validation results, I performed the **Final Exam** using the **Test Set** (`test_X`). This data was completely hidden from the model during training, providing an unbiased estimate of how the system would perform in a real-world deployment.

**Implementation:**
I repeated the evaluation process—calculating metrics and plotting the confusion matrix—to confirm the model's generalization capabilities.

```python
# Final evaluation on the test set
test_multi_predictions = rf_model_multi.predict(test_X)
test_accuracy = accuracy_score(test_y, test_multi_predictions)
test_precision = precision_score(test_y, test_multi_predictions, average='weighted')
test_recall = recall_score(test_y, test_multi_predictions, average='weighted')
test_f1 = f1_score(test_y, test_multi_predictions, average='weighted')

print("\nTest Set Evaluation:")
print(f"Accuracy: {test_accuracy:.4f}")
print(f"Precision: {test_precision:.4f}")
print(f"Recall: {test_recall:.4f}")
print(f"F1-Score: {test_f1:.4f}")

# Confusion Matrix for Test Set
test_conf_matrix = confusion_matrix(test_y, test_multi_predictions)
sns.heatmap(test_conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_labels,
            yticklabels=class_labels)
plt.title('Network Anomaly Detection')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Classification Report for Test Set
print("Classification Report for Test Set:")
print(classification_report(test_y, test_multi_predictions, target_names=class_labels))
```
<img width="1469" height="577" alt="image" src="https://github.com/user-attachments/assets/00ef996e-6367-4876-a5ac-08749020db0d" />

-----

## 4\. Saving the Model 

Finally, to make this project reusable, I serialized (saved) the trained model using `joblib`. This allows the model to be loaded later for real-time predictions without needing to be retrained from scratch.

```python
import joblib

# Save the trained model to a file
model_filename = 'network_anomaly_detection_model.joblib'
joblib.dump(rf_model_multi, model_filename)

print(f"Model saved to {model_filename}")
```
