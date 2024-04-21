import datetime

# Get the current datetime
current_datetime = datetime.datetime.now()

# Calculate the datetime for two days before the current datetime
two_days_before = current_datetime - datetime.timedelta(days=2)

# Convert to timestamp
timestamp_two_days_before = two_days_before.timestamp()

# Print the timestamp
print(timestamp_two_days_before)

# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)