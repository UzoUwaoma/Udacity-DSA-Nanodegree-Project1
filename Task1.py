""""
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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Initialize a set to store unique phone numbers from provided call & text records
unique_numbers = set()

# Loop through text records and extract unique phone numbers
for record in texts:
    sending_number = record[0]
    receiving_number = record[1]

    unique_numbers.add(sending_number)
    unique_numbers.add(receiving_number)

# Loop through call records and extract unique phone numbers
for record in calls:
    sending_number = record[0]
    receiving_number = record[1]

    unique_numbers.add(sending_number)
    unique_numbers.add(receiving_number)

# Print to the console, the number of unique phone numbers
print("There are {} different telephone numbers in the records.".format(len(unique_numbers)))
