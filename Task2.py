"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""


# Create helper function to record time spent on phone by a given number
def record_time_on_phone(time_record, sender, receiver, duration):
    """
    Args:
        time_record (Dictionary): Contains Key - value pair (Number - Time spent (seconds)
        sender (String): Phone number starting call.
        receiver (String): Phone number receiving a call.
        duration(String): Time spent on a call between sender & receiver

    Returns:
        None.
    """

    if sender not in time_record:
        time_record[sender] = 0

    time_record[sender] += int(duration)

    if receiver not in time_record:
        time_record[receiver] = 0

    time_record[receiver] += int(duration)


# Initialize dictionary to store time spent on the phone by each number in the calls records
time_spent = {}

for record in calls:
    sender = record[0]
    receiver = record[1]
    duration = record[3]

    record_time_on_phone(time_spent, sender, receiver, duration)

# Get the phone number with the maximum time spent on the phone
number_with_max_time = max(time_spent, key=time_spent.get)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016."
      .format(number_with_max_time, time_spent[number_with_max_time]))
