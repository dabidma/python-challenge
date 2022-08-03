import os
import csv

bankpath = os.path.join("PyBank", "Resources", "budget_data.csv")
#a la was with me and we tried multiple different pathway functions which wouldn't work except for this

c = 0
total_months = 0
total_net = 0
net_change = 0
current_month = 0
previous_month = 0
profit_loss_ot = []
date = []

with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for rows in csvreader:
        if c ==1:
            previous_month = current_month
        else:
            #total months
            total_months += 1
            #total net profit/loss
            total_net += int(rows[1])
            #changes in profit/loss and average of change
            net_change = current_month - previous_month
            profit_loss_ot.append(net_change)
            previous_month = current_month


            
    print(total_months)
    print(total_net)
    print(net_change)