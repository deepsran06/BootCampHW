# PyBank Solution

# Import Dependencies
import csv
import os

# Create empty lists
revenue = []
months = []

# Set and Read file path
file = os.path.join("Resources/budget_data.csv")
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

# Create some more variables and lists
total_months = len(months)
total_revenue = 0
increase = revenue[0]
decrease = revenue[0]

# For Loop, go through the revenue to find the largest increase and decrease
for x in range(len(revenue)):
    if revenue[x] >= increase:
        increase = revenue[x]
        increase_month = months[x]
    elif revenue[x] <= decrease:
        decrease = revenue[x]
        decrease_month = months[x]
    total_revenue += revenue[x]

# Calculate average change
average_change = round(total_revenue/total_months, 2)

# Create break line variable and format print
break_line = "-------------------------"
print("Financial Analysis")
print(break_line)
print("Total Months: " + str(total_months))
print("Total: $" + str(total_revenue))
print("Average  Change: $" + str(average_change))
print("Greatest Increase in Profits: $" + str(increase) + " (" + str(increase_month) + ")")
print("Greatest Decrease in Profits: $" + str(decrease) + " (" + str(decrease_month) + ")")

# Set Variable for Output File
output_file = os.path.join("financial_analysis.txt")

# Open Output File
writer = open(output_file, mode = "w")

# Write into file using 'write'
writer.write("Financial Analysis" + "\n" +
             break_line + "\n" +
             "Total Months: " + str(total_months) + "\n" +
             "Total: $" + str(total_revenue) + "\n" +
             "Average  Change: $" + str(average_change) + "\n" +
             "Greatest Increase in Profits: $" + str(increase) + " (" + str(increase_month) + ")" + "\n" +
             "Greatest Decrease in Profits: $" + str(decrease) + " (" + str(decrease_month) + ")")
