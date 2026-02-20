# MuleShield: Rule-Based Financial Mule Account Detection System

## 🚀 Overview
*MuleShield* is a lightweight, rule-based system designed to detect suspicious mule accounts in digital financial transactions.  
The system analyzes transaction frequency, total amount received, and outgoing behavior to compute a *fraud score* for each account. Accounts exceeding a defined threshold are flagged as potential mule accounts, helping prevent money laundering and fraudulent activity.

---

## 👥 Team Members
- Ashylin  Denny
- Adlin Jeno 
- Benitah Joshi

---

## 🛠 Tech Stack
- *Python* – Programming language  
- *Pandas* – Data manipulation  
- *Matplotlib* – Visualization  
- *VS Code* – Development environment  

---

## 📄 Project Files
| File | Description |
|------|-------------|
| generate_data.py | Generates synthetic transaction dataset for testing |
| detect_mule.py | Core fraud detection logic with fraud scoring |
| transactions.csv | Sample transaction dataset |
| suspicious_accounts.csv | Output of flagged suspicious accounts |
| fraud_chart.png | Bar chart visualization of fraud scores |

---

## 🧩 Methodology
1. *Load Dataset* – Synthetic transactions with sender, receiver, and amount.  
2. *Aggregate Metrics* – Count incoming and outgoing transactions per account, sum total received amount.  
3. *Compute Fraud Score* –
Fraud Score = (Received Count × 2) + (Total Received ÷ 10000) − Sent Count
4. *Flag Suspicious Accounts* – Accounts with fraud score above threshold are automatically flagged.  
5. *Visualize Results* – Generate bar chart ranking accounts by fraud score.  
6. *Export Output* – CSV of suspicious accounts for reporting.

---

## 🏃 How to Run

1. *Install dependencies*  
```bash
pip install pandas matplotlib
2. Generate dataset
python generate_data.py
3. Detect suspicious accounts
python detect_mule.py
4. Outputs generated
- Terminal table of flagged accounts
- suspicious_accounts.csv
- Fraud score bar chart (fraud_chart.png)

## Key Results
- System successfully identifies accounts with abnormal receiving patterns.
- Generates fraud score ranking to prioritize investigation.
- Visualization clearly shows high-risk accounts for quick analysis.
## Impact & Future Scope
- Can integrate into banking systems for real-time mule account detection.
- Expand to ML-based detection using Isolation Forest or anomaly detection.
- Add network graph analysis to detect clusters of mule accounts.
- Develop live dashboard for financial monitoring.

Note: This project uses rule-based logic for explainability. All detection logic, dataset, and analysis were developed and understood by the team.
