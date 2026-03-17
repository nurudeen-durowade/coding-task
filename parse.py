#parse logs for unique session

log_file = 'logs.txt'

unique_session = set()

with open(log_file) as f:
    for line in f:
        parts = line.strip().split(',')
        sessionId = parts[1]
        unique_session.add(sessionId)
print("Unique sessions", unique_session)