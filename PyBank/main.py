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

# with open(csvpath, 'r') as fh:
#     m = csv.reader(fh)
#     for i in m:
#         print(i)

temp_list = [] # make a list of the rows so that you can iterate

with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        temp_list.append(row) #Adding all the rows

    list = temp_list[1:] #Adds all of the rows except the header
    # print(list) --> this was to test and see that the list would print
    
    value = [] #list for all of the values in the 2nd column
    for row in range(len(list)):
       # print(int(list[i][1])) ---> to see if it would print just the number alone
        value.append(int(list[row][1])) #adding the profit/losses to the list
    # print(value) ---> to see if the list would print only profit/losses
    
    mvalue = [] #list for all of the values in the 1st column
    for row in range(len(list)):
       # print(int(list[i][1])) ---> to see if it would print just the month alone
        mvalue.append(list[row][0])
        # print(mvalue) #---> to see if the list would print only the month

#Find the differences between the values
    difference = []

    for row in range (len(value)):
        if row > 0:
            temp_difference = value[row]-value[row-1] #calculate the difference between the rows
            difference.append(temp_difference)  #add the difference to the list
    # print(difference) ---> to see if the differences would print
    
    difference_sum = 0 #Placeholder variable to create the sum
    for row in difference:
        difference_sum += row


    print(f"Average: ${round(difference_sum/len(difference),2)}")

# The greatest increase in profits (date and amount) over the entire period
maxprofit=(difference.index(max(difference)))+1 #to find the position of the max profit
# print(mvalue[maxprofit]) to print only the date

print(f"Greatest Increase in Profits: {(mvalue[maxprofit])} (${max(difference)})")


#The greatest decrease in profits (date and amount) over the entire period
minprofit=(difference.index(min(difference)))+1 #to find the position of the min profit
# print(mvalue[minprofit]) to print only the date

print(f"Greatest Decrease in Profits: {(mvalue[minprofit])} (${min(difference)})")
