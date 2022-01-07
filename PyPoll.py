# the data we need to retrieve:

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#print the header row
    headers = next(file_reader)
    print(headers)

#print each row in the CSV file
    # for row in file_reader:
    #     print(row[0])





# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote