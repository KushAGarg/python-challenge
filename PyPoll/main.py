#Import modules os and csv
import os
import csv

#Set path for PyPoll CSV file
election_path = os.path.join('Resources', 'election_data.csv')

#Open PyPoll CSV file
with open(election_path) as csv_election_file:
    csv_reader = csv.reader(csv_election_file, delimiter=',')
    csv_header = next(csv_election_file)
    num_rows = 0
    total_votes = {}
    results = []
    for row in csv_reader:
        num_rows += 1
        if row[2] not in total_votes.keys():
            total_votes[row[2]] = 1
        else:
            total_votes[row[2]] += 1

#Print results to terminal
print("Election Results")
print("-----------------------")
print(f"Total Votes: {(num_rows)}")
print("-----------------------")
for candidates in total_votes.keys():
    print("{candidate} {percent_votes:.2%} ({total_votes})".format(candidate=candidates, percent_votes=total_votes[candidates] / num_rows, total_votes=total_votes[candidates]))
winner = max(total_votes, key=total_votes.get)
print("-----------------------")
print(f"Winner: {(winner)}")
print("-----------------------")

#Print results in a text file
output = os.path.join('Analysis', 'election_results.txt')
with open(output, 'w') as new:
    new.write("Election Results\n")
    new.write("-----------------------\n")
    new.write(f"Total Votes: {(num_rows)}\n")
    new.write("-----------------------\n")
    new.write("{candidate} {percent_votes:.2%} ({total_votes})\n".format(candidate=candidates, percent_votes=total_votes[candidates] / num_rows, total_votes=total_votes[candidates]))
    new.write("-----------------------\n")
    new.write(f"Winner: {(winner)}\n")
    new.write("-----------------------")
