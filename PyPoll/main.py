import os 
import csv

poll_path=os.path.join(r'PyPoll\Resources\election_data.csv')

line1="Election Results"+"\n"+"----------------------------"
print(line1)

# The total number of votes cast
with open(poll_path) as csvfile:
    pollreader=csv.reader(csvfile)

    totalvotes=-1                       #To exclude the header value

    for row in pollreader:
        totalvotes+=1                   #To iterate and add to the total votes
line2=(f"Total Votes: {totalvotes}"+"\n"+"----------------------------")
print(line2)

# A complete list of candidates who received votes
unique_candidates=set()                     #To create a list for all of the unique candidates

with open(poll_path,'r') as csvfile:
    pollreader=csv.reader(csvfile)
    header=next(csv.reader(csvfile))        #To exclude the header from the list of candidates

    for row in pollreader:
        unique_candidates.add(row[2])       #To add the 3rd column to the list of unique candidates
# print(f'Candidates receiving votes: {list(unique_candidates)}')              #To print the list of unique candidates only

# The total number of votes each candidate won

temp_list = [] # make a list of the rows so that you can iterate

with open(poll_path, 'r') as csvfile:
    pollreader=csv.reader(csvfile)
    for row in pollreader:
        temp_list.append(row) #Adding all the rows

    list = temp_list[1:] #Adds all of the rows except the header
    # print(list) --> this was to test and see that the list would print
    
    candidates = [] #list for all of the values in the 3rd column
    for row in range(len(list)):
       # print(int(list[i][1])) ---> to see if it would print just the number alone
        candidates.append(str(list[row][2])) #adding the profit/losses to the list
    
    candidateCCS='Charles Casper Stockham'          #Set the names to count
    candidateRAD='Raymon Anthony Doane'
    candidateDD='Diana DeGette'

    CCScount=[]                                     #Three separate counts to tally the number of votes
    RADcount=[]
    DDcount=[]

    for row in candidates:                          #Iterate through the data to count the unique values
        if row == candidateCCS:
            CCScount.append(row)
        if row == candidateRAD:
            RADcount.append(row)
        if row == candidateDD:
            DDcount.append(row)

# The percentage of votes each candidate won
    CCSpercent= round((len(CCScount)/totalvotes)*100,3)
    RADpercent= round((len(RADcount)/totalvotes)*100,3)
    DDpercent= round((len(DDcount)/totalvotes)*100,3)

#Print the total percentages and counts
line3=(f'Charles Casper Stockham: {CCSpercent}% ({len(CCScount)})')
line4=(f'Raymon Anthony Doane: {RADpercent}% ({len(RADcount)})')
line5=(f'Diana DeGette: {DDpercent}% ({len(DDcount)})'+"\n"+"----------------------------")
print(line3)
print(line4)
print(line5)

# The winner of the election based on popular vote.
allvotes= {CCSpercent:candidateCCS, RADpercent:candidateRAD, DDpercent:candidateDD}     #Create a dictionary with all the winners and their percents

maxpercent=max(allvotes.keys())                                                         #Call for just the max percent
winner=allvotes[maxpercent]                                                             #Find the winner for all the votes 

line6=(f'Winner: {winner}'+'\n'+"----------------------------")
print(line6)

# Write the summary to a text file in the Analysis folder
text_file_path=(r'PyPoll\Analysis\PyPoll.txt')
analysis_bank= [line1,'\n',line2,'\n',line3,'\n',line4,'\n',line5,'\n',line6]

with open (text_file_path,'w') as file:
    for line in analysis_bank:
        file.write(line) 