import datetime

two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
timestamp = int(two_days_ago.timestamp())
print(timestamp)

# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)