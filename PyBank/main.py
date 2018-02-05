import os
import csv

file_num = ['1', '2']

#create file path and save as file
for filenumber in file_num:
    
    file = os.path.join('raw_data', 'budget_data_' + str(filenumber) + '.csv')

#create lists for month and revenue data
    months = []
    revenue = []

#read csv 
    with open(file, 'r') as csvfile:
        csvread = csv.reader(csvfile)
    
        next(csvread, None)

        for row in csvread:
            months.append(row[0])
            revenue.append(int(row[1]))

    total_months = len(months)

#create greatest increase, greatest decrease and total revenue
    greatest_inc = revenue[0]
    greatest_dec = revenue[0]
    total_revenue = 0

#loop through revenue and calculate greatest increase and greatest decrease
    for r in range(len(revenue)):
        if revenue[r] >= greatest_inc:
            greatest_inc = revenue[r]
            great_inc_month = months[r]
        elif revenue[r] <= greatest_dec:
            greatest_dec = revenue[r]
            great_dec_month = months[r]
        total_revenue += revenue[r]

#calculate average_change
    average_change = round(total_revenue/total_months, 2)

#create output file
    output_dest = os.path.join('Output','pybank_output_' + str(filenumber) + '.txt')

#print summary to output file
    with open(output_dest, 'w') as writefile:
        writefile.writelines('Financial Analysis\n')
        writefile.writelines('----------------------------' + '\n')
        writefile.writelines('Total Months: ' + str(total_months) + '\n')
        writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
        writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
        writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' $' + str(greatest_inc) + '\n')
        writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')
