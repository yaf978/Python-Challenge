import os
import csv
import statistics

candidates_list = []
temp_list = []
counter = 0
count_list = []
key = []
value = []
percentage = []
winner_vote_count = 0
winner = ""

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for row in reader:
        temp_list.append(row[2])
# TODO 1: The total number of votes cast
total_vote_number = len(temp_list)
print(total_vote_number)

# TODO 2: A complete list of candidates who received votes

temp_list.sort()
# print(temp_list)
candidates_list.append(temp_list[0])
for i in range(1, len(temp_list)):
    if temp_list[i] != temp_list[i - 1]:
        candidates_list.append(temp_list[i])

print(candidates_list)

# TODO 4: A complete list of candidates who received votes
Charles_vote_count = temp_list.count(candidates_list[0])
Diana_vote_count = temp_list.count(candidates_list[1])
Raymon_vote_count = temp_list.count(candidates_list[2])

candidates_info = {}

print(Charles_vote_count)
print(Diana_vote_count)
print(Raymon_vote_count)

# TODO 3: The percentage of votes each candidate won

Charles_percentage = round((Charles_vote_count / total_vote_number) * 100, 3)
Diana_percentage = round((Diana_vote_count / total_vote_number) * 100, 3)
Raymon_percentage = round((Raymon_vote_count / total_vote_number) * 100, 3)
print(Charles_percentage)
print(Diana_percentage)
print(Raymon_percentage)

# TODO 5: The winner of the election based on popular vote

for i in range(len(candidates_list)):
    key.append(candidates_list[i])
    value.append(temp_list.count(candidates_list[i]))
    percentage.append(round((temp_list.count(candidates_list[i]) / total_vote_number) * 100, 3))
    if value[i] > winner_vote_count:
        winner_vote_count = value[i]
        winner = candidates_list[i]

x = zip(candidates_list, value, percentage)
print(tuple(x))
print(winner, winner_vote_count)
