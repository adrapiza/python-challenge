#PyBank

import os
import csv

print("Financial Analysis")
print ("---------------------------------------")

read_dir = 'PyBank/Resources/'
filename = 'budget_data.csv'
budget_data_csv = os.path.join(read_dir, filename)


with open(budget_data_csv, 'r') as file:
    csv_reader = csv.reader(file)


    next(csv_reader)

    total_months = 0
    total_amount = 0
    changes = []
    previous_amount = 0
    greatest_increase= 0
    Greatest_increase_date= "" 
    greatest_decrease = 0
    Greatest_decrease_date = ""
    

    for row in csv_reader:
        
        total_months += 1
        current_amount = int(row[1])
        total_amount += current_amount 
        
        if total_months >1:
            change = current_amount - previous_amount
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                Greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                Greatest_decrease_date = row [0]
                
        previous_amount = current_amount
         
    average_change = sum(changes) / len(changes)

print (f"Total Months: {total_months}")
print (f"Total: ${total_amount}")
print(f"Average Change: ${average_change:.2f}")
print (f"Greatest Increase in Profits: {Greatest_increase_date}(${greatest_increase})")
print (f"Greatest Decrease in Profits: {Greatest_decrease_date}(${greatest_decrease})")