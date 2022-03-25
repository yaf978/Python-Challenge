import os
import csv

# declaration of variables
candidates_list = []
temp_list = []
counter = 0
count_list = []
vote_count = []
percentage = []
winner_vote_count = 0
winner = ""

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # to skip the header
    next(reader, None)
    for row in reader:
        temp_list.append(row[2])

# TODO 1: The total number of votes cast

total_vote_number = len(temp_list)

# TODO 2: A complete list of candidates who received votes

temp_list.sort()

# initial value for candidate name
candidates_list.append(temp_list[0])

for i in range(1, len(temp_list)):
    if temp_list[i] != temp_list[i - 1]:
        candidates_list.append(temp_list[i])

# TODO 4: A complete list of candidates who received votes
# TODO 5: The winner of the election based on popular vote
for i in range(len(candidates_list)):
    vote_count.append(temp_list.count(candidates_list[i]))
    percentage.append(round((temp_list.count(candidates_list[i]) / total_vote_number) * 100, 3))
    if vote_count[i] > winner_vote_count:
        winner_vote_count = vote_count[i]
        winner = candidates_list[i]

x = zip(candidates_list, percentage, vote_count)
info = tuple(x)

# TODO 6: WRITE TO FILE and print the result to the termial

with open('Analysis/Analysis.txt', 'w') as file:
    file.write('Election Results\n')
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_vote_number}\n")
    file.write("----------------------------\n")
    for i in info:
        file.write(f"{i[0]} : {i[1]}% ({i[2]})\n")
    file.write("----------------------------\n")
    file.write(f"Winner:{winner}\n")
    file.write("----------------------------\n")

with open('Analysis/Analysis.txt', 'r') as txt_f:
    print(txt_f.read())
