#PyPoll

import os
import csv

print("Election Results")

print ("---------------------------------------")

read_dir = 'PyPoll/Resources'
filename = 'election_data.csv'
election_data_csv = os.path.join(read_dir, filename)

total_votes = 0
candidate_votes={}

with open(election_data_csv, 'r') as file:
    csv_reader = csv.reader(file)
    
    next (csv_reader)
    
    for row in csv_reader:
         total_votes += 1
         candidate_name = row[2]
         
         if candidate_name in candidate_votes:
             candidate_votes[candidate_name] += 1
         else:
            candidate_votes[candidate_name] = 1
        
print(f"Total Votes: {total_votes}")
print ("---------------------------------------")
for candidate, votes in candidate_votes.items():
    percentage=(votes/total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print ("---------------------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner:{winner}")
print ("---------------------------------------")