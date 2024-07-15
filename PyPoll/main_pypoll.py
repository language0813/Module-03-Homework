# Import the operating system module for creating file path
# Import CSV module for reading CSV file
import os
import csv

# Define the path for the CSV file that we are going to use
csvpath = os.path.join("Resources", "election_data.csv")

# Open and read the CSV file
with open(csvpath) as election_data:
    
    # 'delimiter=","' is default, so we don't need to enter that parameter
    election_data_reader = csv.reader(election_data)

    # To skip the header
    next(election_data_reader,None)

    # Convert the result of csv.reader to a list of lists
    election_data_list = list(election_data_reader)

    # Sort the lists based on the "Candidate" column for calculating each candidate's votes later
    sorted_election_data = sorted(election_data_list, key=lambda row: row[2])

# Export the sorted data to a new CSV file that will be used in later processes
output_file = os.path.join("Resources", "sorted_election_data.csv")
with open(output_file,"w") as csvfile:
    writer = csv.writer(csvfile)

    # Add the same headers to the new CSV file
    writer.writerow(["Ballot ID", "County", "Candidate"])
    writer.writerows(sorted_election_data)


# Create lists for storing data
candidatelist =[]
candidatevotes = []

# Set initial value to the variables needed
total_votes = 0
previous_candidate = ""

# Define the path for the CSV file that we are going to use
csvpath = os.path.join("Resources", "sorted_election_data.csv")

# Open and read the CSV file
with open(csvpath) as sorted_election_data:
    sorted_election_data_reader = csv.reader(sorted_election_data)
    
    # To skip the header
    next(sorted_election_data_reader,None)

    # To loop through each row after header
    for row in sorted_election_data_reader:

        # To calculate the total number of votes
        total_votes = total_votes + 1

        # Since the data has been sorted by candidate, we could apply the logic to capture new candiates 
        # and their votes when the candidate in the current row is different from the previous row
        if row[2] != previous_candidate:
            current_candidate = row[2]

            # Add new candidate to the "candidatelist" list
            candidatelist.append(current_candidate)

            # To retrieve the index of current candidate in the list to add the vote count to 
            # the correct position of the "candidatevotes" list
            current_candidate_index = candidatelist.index(current_candidate)
            candidatevotes.append(0)
            candidatevotes[current_candidate_index] += 1

            # Reset the "previous_candidate"
            previous_candidate = current_candidate

        # If the previous/current candidates are the same,
        # just add the vote count to the corresponding position of the "candidatevotes" list
        else:
            candidatevotes[current_candidate_index] += 1

# To retrieve the index of maximum number in the "candidatevotes" list,
# and capture the winner in the "candidatelist" list using the index
winner_index = candidatevotes.index(max(candidatevotes))
winner = candidatelist[winner_index]

# To print out results in terminal
print("Election Results")
print("------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------")

# To loop through the "candidatelist" list to print each candidate's election result
for x in range(len(candidatelist)):
    candidate_percentage = round(candidatevotes[x] / total_votes * 100,3)
    print(f"{candidatelist[x]}: {candidate_percentage}% ({candidatevotes[x]})")
print("------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------")

# Use "csv.writer" to export the results a text file
output_file = os.path.join("analysis", "election analysis.txt")
with open(output_file,"w") as text:
    writer = csv.writer(text)
    writer.writerow(["Election Results"])
    writer.writerow(["------------------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["------------------------------------"])
    for x in range(len(candidatelist)):
        writer.writerow([f"{candidatelist[x]}: {candidate_percentage}% ({candidatevotes[x]})"])
    writer.writerow(["------------------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["------------------------------------"])
