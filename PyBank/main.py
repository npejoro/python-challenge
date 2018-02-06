import os
import csv

#create file extension numbers, add to list as needed
fileext = ['1', '2']

#for loop to create file path and extract source data
for filenumber in fileext:
    
    file = os.path.join('raw_data', 'budget_data_' + str(filenumber) + '.csv')

#create lists for month and revenue data
    months = []
    revenue = []

#read csv and calculation to count total months
    with open(file, 'r') as csvfile:
        csvread = csv.reader(csvfile)
    
        next(csvread, None)

        for row in csvread:
            months.append(row[0])
            revenue.append(int(row[1]))

    totalmonths = len(months)

#create greatest increase, greatest decrease and total revenue
    greatinc = revenue[0]
    greatdec = revenue[0]
    totalrev = 0

#for loop to calculate revenue and calculate greatest increase and greatest decrease
    for r in range(len(revenue)):
        if revenue[r] >= greatinc:
            greatinc = revenue[r]
            greatincmonth = months[r]
        elif revenue[r] <= greatdec:
            greatdec = revenue[r]
            greatdecmonth = months[r]
        totalrev = totalrev + revenue[r]

#calculate average change
    avgchange = round(totalrev/totalmonths, 2)

#create output file
    output_dest = os.path.join('Output','pybank_output_' + str(filenumber) + '.txt')

#print summary to output file
    with open(output_dest, 'w') as writefile:
        writefile.writelines('Financial Analysis' + '\n')
        writefile.writelines('----------------------------------------------------------------' + '\n')
        writefile.writelines('Total Months: ' + str(totalmonths) + '\n')
        writefile.writelines('Total Revenue: $' + str(totalrev) + '\n')
        writefile.writelines('Average Revenue Change: $' + str(avgchange) + '\n')
        writefile.writelines('Greatest Increase in Revenue: ' + greatincmonth + ' $' + str(greatinc) + '\n')
        writefile.writelines('Greatest Decrease in Revenue: ' + greatdecmonth + ' $' + str(greatdec) + '\n')

#print summary to terminal 
    print('Financial Analysis')
    print('----------------------------------------------------------------')
    print('Total Months: ' + str(totalmonths))
    print('Total Revenue: $' + str(totalrev))
    print('Average Revenue Change: $' + str(avgchange))
    print('Greatest Increase in Revenue: ' + greatincmonth + ' $' + str(greatinc))
    print('Greatest Decrease in Revenue: ' + greatdecmonth + ' $' + str(greatdec))
