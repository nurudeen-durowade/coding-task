# Top 5 accounts by Log Frequency

from collections import Counter

log_file = "./application.log"

account = []

with open(log_file) as f:
    for line in f:
        account_id = line.strip().split(",")
        account.append(account_id)

top5 = Counter(account).most_common(5)

print(top5)