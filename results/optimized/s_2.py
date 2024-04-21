import datetime

two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
timestamp = int(two_days_ago.timestamp())
print(timestamp)

