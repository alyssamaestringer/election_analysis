# the data we need to retrieve:

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total votes variable to 0
total_votes = 0

# declare a new list to find candidates
candidate_options = []
#declare empty dict for candidate votes
candidate_votes = {}
# declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""
#declare a variable for the winning count
winning_count = 0
#declare a variable for the winning percentage
winning_percentage = 0

#Open election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#print the header row
    headers = next(file_reader)

#print each row in the CSV file
    for row in file_reader:        

        # Add to the total vote count
        total_votes += 1

        #print thhe candidate name from each row
        candidate_name = row[2]

        # If statement inside loop: If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

        # if candidate does not match any exisiting candidate
            candidate_options.append(candidate_name)
        
        # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # add vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
    # use a for loop to iterate through candidate list
    for candidate_name in candidate_votes:
        # get vote count of candidate
        votes = candidate_votes[candidate_name]
        #calc percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

# print candidate name and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    #print out winning candidate summar
    winning_candidate_summary = (
        f"---------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------\n")
    print(winning_candidate_summary)








# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote