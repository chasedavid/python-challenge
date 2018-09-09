#Created By:    Chase Farnsworth
#Created On:    2 Sep 2018

#Purpose:       run through provided file to pull, how many Months
#               total, average changes

import os
import csv

#sum function
def total_profit(numbers):
    total = 0
    for number in numbers:
        total += number
    return (total)

def mean(numbers):
    return (total_profit(numbers) / len(numbers))

#set file csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")
outpath = os.path.join("result.csv")

#open file and itterate
with open(csvpath, 'r+', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
#set variables
    months = 0
    prolos = []
    prolos_month = []
    mx_pro = 0
    mp_month = ""
    mx_los = 0
    ml_month = ""
    delta_prolos = []
    result = []

#iterate through the file
    for row in csvreader:
        months += 1
        prolos.append(int(row[1]))
        length = len(prolos)
        if length > 1:
            delta_prolos.append(int(prolos[length - 1] - prolos[length - 2]))
            prolos_month.append(row[0])
    for i in range(len(delta_prolos)):
        if int(delta_prolos[i]) > mx_pro:
            mx_pro =  int(delta_prolos[i])
            mp_month = prolos_month[i]
        if int(delta_prolos[i]) < mx_los:
            mx_los = int(delta_prolos[i])
            ml_month = prolos_month[i]

#store outcome
    result.append("Financial Analysis")
    result.append("--------------------------------")
    result.append("Total Months: %i" %(months))
    result.append("Total: $%i" %(total_profit(prolos)))
    result.append("Average Change: $%.02f" %(mean(delta_prolos)))
    result.append("Greatest Increase in Profits: %s ($%i)" %(mp_month, mx_pro))
    result.append("Greatest Increase in Profits: %s ($%i)" %(ml_month, mx_los))

#close filen for reading
    csvfile.close()

#open for writing
with open(outpath, 'w+', newline='') as outpt:

#output to file and print
    csvwriter = csv.writer(outpt, delimiter='\n', quoting=csv.QUOTE_NONE)
    print()
    csvwriter.writerows([result])
    for row in result:
        print(row)
    print()

#close for writing
    csvfile.close()
