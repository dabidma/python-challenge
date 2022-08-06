from calendar import month
import os
import csv

bankpath = 'python-challenge/PyBank/Resources/budget_data.csv'
#a la was with me and we tried multiple different pathway functions which wouldn't work except for this

c = 0
total_months = 0
total_net = 0
net_change = 0
net_month_change = 0
net_change_ot = []
month_change = []

with open(bankpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    first_row = next(csvreader)
    prev_row = int(first_row[1])
    for rows in csvreader:
         #total months

        total_months += 1
        #total net profit/loss

        total_net += int(rows[1])
        #changes in profit/loss and average of change

        net_change = int(rows[1]) - prev_row
        prev_row = int(rows[1])
        net_change_ot.append(net_change)
        month_change.append(rows[0])

    
    net_month_change = round((sum(net_change_ot) / total_months),2)
    month_net = dict(zip(net_change_ot, month_change))
    
    greatest_increase_value = max(month_net)
    greatest_decrease_value = min(month_net)
    greatest_increase = []
    greatest_decrease = []

    for key, value in month_net.items():
        if key == greatest_increase_value:
            greatest_increase.append([value, key])
        if key == greatest_decrease_value:
            greatest_decrease.append([value, key])
    
    #print financial analysis
    print(f'''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${net_month_change}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}''')

#write onto txt file
with open('python-challenge/PyBank/analysis/financial_analysis.txt', 'w') as analysis:
    analysis.write(f'''Financial Analysis
----------------------------
Total Months: {str(total_months)}
Total: ${str(total_net)}
Average Change: ${str(net_month_change)}
Greatest Increase in Profits: {str(greatest_increase)}
Greatest Decrease in Profits: {str(greatest_decrease)}''')


    #tests______        
    # print(total_months)
    # print(total_net)
    # print(net_change_list[1])
    # print(first_row)
    # print(net_month_change
    #print(net_change_ot)
    # print(type(month_change))
    # print(month_net)
    # print(greatest_increase)
    # print(greatest_decrease)