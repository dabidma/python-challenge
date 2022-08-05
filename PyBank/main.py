from calendar import month
import os
import csv

bankpath = 'python-challenge/PyBank/Resources/budget_data.csv'
#a la was with me and we tried multiple different pathway functions which wouldn't work except for this

c = 0
total_months = 0
total_net = 0
net_change = 0
net_change_list = []
month_change = []

with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    first_row = next(csvreader)
    for rows in csvreader:
         #total months
        total_months += 1
        #total net profit/loss
        total_net += int(rows[1])
        #changes in profit/loss and average of change
        #first_row = int(rows[1])
        if first_row[1] == rows[1]:
            net_change_list.append(rows[1])
            month_change.append(rows[0])
        else:
            current_row = int(rows[1])
            net_change = current_row - (current_row-1)
            net_change_list.append(rows[1])
            month_change.append(rows[0])
    



            
    print(total_months)
    print(total_net)
    print(net_change_list)