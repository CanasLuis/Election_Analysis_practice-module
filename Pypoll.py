# The data we need to retrieve
#1. the total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


# Import the datetime class from the datetime module.
#import datetime

#Use the now() attribute on the datetime class to get the present time. 
#now = datetime.datetime.now()

# Print the present time. 
#print("The time right now is ", now)

#import csv

#Assign a variable for the file to load and the path. 
#file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file. 
#with open(file_to_load) as election_data:

#To do: performa analysis.
#   print(election_data)
import csv
import os
from traceback import print_tb
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file. 
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data)

#Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis","election_analysis.txt")
#using the open() function with the "w" mode we will write data to the file.
open(file_to_save,"w")

#use the open statement to open the file as a text file. 
outfile = open(file_to_save,"w")
#write some data to the file. 
outfile.write("Hello World")

#Close the file
outfile.close()

# Using the with statement open the file as a text file. 
with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    txt_file.write("Hello wooooorld")

with open(file_to_save,"w") as txt_file:

    txt_file.write("Arapahoe, Denver, Jeffersson")

#para espaciar (enter)
with open(file_to_save,"w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")

#-----------------------------------------------------------

#Add our dependencies. 
import csv
import os

#Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a apath. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options = []

#Declare the empty dictionary. 
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file. 
with open(file_to_load) as election_data:
    #to do: read and analyze the data here. 
    #READ THE FILE OBJECT WITH THE READER FUNCTION. 
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    #iterate through the candidate list
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage}% of the votes. ")
        #Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

        #Determine winning vote count and candidate
        #Determine if the vote is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        

# to do: print out each candidate´s name, vote count, and percentage of
#vote to the terminal

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
        
    print(winning_candidate_summary)

        #print(row)
#3 Print the total votes
   # print(candidate_votes)
    #for row in file_reader:
    #    print(row)    
    


