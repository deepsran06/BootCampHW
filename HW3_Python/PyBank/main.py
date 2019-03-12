# PyBank Solution

# Import Dependencies

import csv
import os

# Set and Read file path
file = os.path.join("Resources/budget_data.csv")
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")