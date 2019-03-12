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

    # Use Vote Count and lambda to Find the Winner
    winner = max(vote_count.keys(), key=(lambda x: vote_count[x]))

    # Create break line variable and format print
    break_line = "-------------------------"
    print("Election Results")
    print(break_line)
    print(f"Total Votes: " + str(votes))
    print(break_line)
    # Print each items in dictionary vote_percentage
    for name, num in vote_percent.items():
        print(name, ":", num)
    print(break_line)
    print(f"Winner: " + str(winner))
    print(break_line)





