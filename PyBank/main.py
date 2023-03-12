import os 
import csv
from datetime import date

csvpath=os.path.join(r"PyBank\Resources\budget_data.csv")

print("Financial Analysis")

#  The total number of months included in the dataset
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    totalmonths=-1

    for row in csvreader:
        totalmonths+=1
print(f"Total Months: {totalmonths}")

# The net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csv.reader(csvfile))

    positivebudget=0
    negativebudget=0

    for row in csvreader:
        value=int(row[1])
        if value >0:
            positivebudget += (value)
        elif value <0:
            negativebudget+= (value)
        
print(f"Total: ${positivebudget + negativebudget}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes



with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csv.reader(csvfile))

    monthlyrevenue=0
    totalchange=0
    
    for row in csvreader:
        value=float(row[1])
        monthlychange= float(value + row[1]) -(value)

print(f"Average Changes: ${monthlychange}")

