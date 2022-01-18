"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create list of numbers that sent texts, received texts, called a number, and received a call.
numbers_sent_text = []
numbers_received_text = []
numbers_with_outgoing_calls = []
numbers_with_incoming_calls = []

[numbers_sent_text.append(record[0]) for record in texts]
[numbers_received_text.append(record[1]) for record in texts]
[numbers_with_outgoing_calls.append(record[0]) for record in calls]
[numbers_with_incoming_calls.append(record[1]) for record in calls]

# Remove duplicates
numbers_sent_text = set(numbers_sent_text)
numbers_received_text = set(numbers_received_text)
numbers_with_outgoing_calls = set(numbers_with_outgoing_calls)
numbers_with_incoming_calls = set(numbers_with_incoming_calls)

# Find numbers who only make outgoing calls, and do not receive calls, send texts, nor receive texts.
telemarketers = numbers_with_outgoing_calls.difference(numbers_with_incoming_calls, numbers_sent_text, numbers_received_text)

# Convert to sorted list
telemarketers = list(telemarketers)
telemarketers.sort()

print("These numbers could be telemarketers: ")
for num in telemarketers:
    print(num)
