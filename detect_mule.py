import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")

send_counts = df['sender'].value_counts()
receive_counts = df['receiver'].value_counts()
total_received = df.groupby('receiver')['amount'].sum()

results = []

for account in receive_counts.index:
    received_times = receive_counts.get(account, 0)
    sent_times = send_counts.get(account, 0)
    received_amount = total_received.get(account, 0)

    # Fraud Score Calculation
    fraud_score = (received_times * 2) + (received_amount / 10000) - sent_times

    if fraud_score > 10:
        results.append({
            "Account": account,
            "Received Times": received_times,
            "Sent Times": sent_times,
            "Total Received": received_amount,
            "Fraud Score": fraud_score
        })

suspicious_df = pd.DataFrame(results)

print("Suspicious Mule Accounts Detected:")
print(suspicious_df)

# Save results
suspicious_df.to_csv("suspicious_accounts.csv", index=False)

# Visualization
if not suspicious_df.empty:
    suspicious_df.plot(
        x="Account",
        y="Fraud Score",
        kind="bar",
        legend=False
    )
    plt.title("Fraud Score of Suspicious Accounts")
    plt.ylabel("Fraud Score")
    plt.savefig("fraud_chart.png")
print("Fraud chart saved as fraud_chart.png")
plt.show()