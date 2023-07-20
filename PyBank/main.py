#Import modules os and csv
import os
import csv

#Set path for PyBank CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Open PyBank CSV file
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    totals = []
    changes = []
    for row_count, row in enumerate(csv_reader, start=1):
        value = int(row['Profit/Losses'])
        totals.append(value)

for i in range(1, len(totals)):
    changes.append(totals[i]-totals[i-1])

#Evaluate max and min change in profits
increase = max(changes)
decrease = min(changes)

#Print results to terminal
print("Financial Analysis")
print("-----------------------")
print("Total Months: {}".format(row_count))
print("Total: ${}".format(sum(totals)))
print("Average Change: ${}".format(str(round(sum(changes) / len(changes), 2))))
print("Greatest Increase in Profits: ${}".format(str(increase)))
print("Greatest Decrease in Profits: ${}".format(str(decrease)))

#Print results to a text file
output = os.path.join('Analysis', 'financial_analysis.txt')
with open(output, 'w') as new:
    new.write("Financial Analysis" + "\n")
    new.write("-----------------------" + "\n")
    new.write("Total Months: {}".format(row_count) + "\n")
    new.write("Total: ${}".format(sum(totals)) + "\n")
    new.write("Average Change: ${}".format(str(round(sum(changes) / len(changes), 2))) + "\n")
    new.write("Greatest Increase in Profits: ${}".format(str(increase)) + "\n")
    new.write("Greatest Decrease in Profits: ${}".format(str(decrease)))
