import pandas as pd
import random
from datetime import datetime, timedelta

accounts = [f"A{i}" for i in range(1, 21)]
channels = ["App", "Web", "UPI", "ATM"]

data = []
start_time = datetime.now()

for _ in range(200):
    sender = random.choice(accounts)
    receiver = random.choice(accounts)
    
    if sender != receiver:
        amount = random.randint(1000, 20000)
        channel = random.choice(channels)
        time = start_time + timedelta(minutes=random.randint(0, 120))
        
        data.append([sender, receiver, amount, channel, time])

# Inject artificial mule behaviour
for i in range(10):
    data.append([
        f"A{i}",      # different senders
        "A99",        # mule account receiving
        15000,        # high amount
        "UPI",
        pd.Timestamp.now()
    ])

df = pd.DataFrame(data, columns=["sender", "receiver", "amount", "channel", "time"])

df.to_csv("transactions.csv", index=False)

print("Dataset created successfully!")