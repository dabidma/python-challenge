import os
import csv

pollpath = 'python-challenge\PyPoll\Resources\election_data.csv'


vote_count = 0
charles_count = 0
diana_count = 0
raymon_count = 0
charles_percent = 0
diana_percent = 0
raymon_percent = 0

with open(pollpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for rows in csvreader:
        #total count
        vote_count += 1
        #total count of each candidate
        if rows[2] == "Charles Casper Stockham":
            charles_count += 1
        elif rows[2] == "Diana DeGette":
            diana_count += 1
        elif rows[2] == "Raymon Anthony Doane":
            raymon_count += 1
        #percent of each candidate
        charles_percent = round(((charles_count/vote_count) * 100),3)
        diana_percent = round(((diana_count/vote_count) * 100),3)
        raymon_percent = round(((raymon_count/vote_count) * 100),3)
        #winner
    if charles_percent > diana_percent and charles_percent > raymon_percent:
        winner = "Charles Casper Stockham"
    elif diana_percent > charles_percent and diana_percent > raymon_percent:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
    print(f'''Election Results
-------------------------
Total Votes: {str(vote_count)}
-------------------------
Charles Casper Stockham: {str(charles_percent)}% ({str(charles_count)})
Diana DeGette: {str(diana_percent)}% ({str(diana_count)})
Raymon Anthony Doane: {str(raymon_percent)}% ({str(raymon_count)})
-------------------------
Winner: {winner}
-------------------------''')


#write results to text file       
with open('python-challenge/PyPoll/analysis/election_results.txt', 'w') as results:
    results.write(f'''Election Results
-------------------------
Total Votes: {str(vote_count)}
-------------------------
Charles Casper Stockham: {str(charles_percent)}% ({str(charles_count)})
Diana DeGette: {str(diana_percent)}% ({str(diana_count)})
Raymon Anthony Doane: {str(raymon_percent)}% ({str(raymon_count)})
-------------------------
Winner: {winner}
-------------------------''')

    #tests________
    #print(vote_count)
    # print(charles_count)
    # print(diana_count)
    # print(raymon_count)
    # print(charles_percent)
    # print(diana_percent)
    # print(raymon_percent)
    #print(winner)