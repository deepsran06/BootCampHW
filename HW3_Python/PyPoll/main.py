# PyPoll Solution using dictionaries, lists, and lambda function

# Import Dependencies

import csv
import os

# Define varibles using dictionaries and lists

candidates = []
vote_count = {}
vote_percent = {}
votes = -1

# Set and Read file path
file = os.path.join("Resources/election_data.csv")
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Use for and if to count the number of votes using append
    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

# Calculations for Percentage of Vote
    for name, num in vote_count.items():
        vote_percent[name] = str(round(((num/votes)*100),3)) + "% ("+str(num) + ")"





