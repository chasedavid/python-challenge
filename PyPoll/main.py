#Created by:    Chase Farnsworth
#Created on:    8 Sep 2018

#Purpose:       iterate through file to find winner of local election

#import dependencies
import os, csv

def comp(k, c, l, o):
    if k > c:
        comp1 = k
    else:
        comp1 = c
    if l > o:
        comp2 = l
    else:
        comp2 = o
    if comp1 > comp2:
        final = comp1
    else:
        final = comp2
    if final == k:
        return ('Khan')
    elif final == c:
        return ('Correy')
    elif final == l:
        return ('Li')
    elif final == o:
        return ("O'Tooley")
    else:
        return ("Error in comparison")

#set file csv
csvpath = os.path.join(".", "Resources", "election_data.csv")
outpath = os.path.join("result.csv")

#open file and itterate
with open(csvpath, 'r+', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)

#set variables
    k = 0
    c = 0
    l = 0
    o = 0
    total_vote = 0
    other = 0
    result = []

    for row in csvreader:
        total_vote += 1
        if row[2].lower() == "Khan".lower():
            k += 1
        elif row[2].lower() == "Correy".lower():
            c += 1
        elif row[2].lower() == "Li".lower():
            l += 1
        elif row[2].lower() == "O'Tooley".lower():
            o += 1
        else:
            other += 1

    result.append('Election Results')
    result.append('-------------------------')
    result.append('Total Votes: %i' %(total_vote))
    result.append('-------------------------')
    result.append('Khan: %.03f (%i)' %((100*k/total_vote), k))
    result.append('Correy: %.03f (%i)' %((100*c/total_vote), c))
    result.append('Li: %.03f (%i)' %((100*l/total_vote), l))
    result.append('O\'Tooley: %.03f (%i)' %((100*o/total_vote), o))
    result.append('-------------------------')
    result.append('Winner: %s' %(comp(k, c, l, o)))
    result.append('-------------------------')

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
