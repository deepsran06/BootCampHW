# PyPoll Solutions using dictionaries, lists, and lambda function

# Import Dependencies

import csv
import os

# Set and Read file path

file = os.path.join("Resources/election_data.csv")
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



