import os
import csv
import statistics

# declaration of variables

months = []
profit_losses = []
change = []
greatest_increase = 0
greatest_decrease = 0
date = []
change_range = []

# TODO read file
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for rows in reader:
        # print(rows)
        months.append(rows[0])
        profit_losses.append(int(rows[1]))

# TODO 1 :The total number of months included in the dataset:

total_months = len(months)

print(f"\nTotal Months: {total_months}")


# todo 2: The net total amount of "Profit/Losses" over the entire period:

total_amount = sum(profit_losses)

# TODO 3:The changes in "Profit/Losses" over the entire period, and then the average  those changes

for i in range(len(profit_losses) - 1):
    x = profit_losses[i + 1] - profit_losses[i]
    change.append(x)
    change_range.append(months[i + 1])

print(f"Average Change : ${round(statistics.mean(change), 2)}")

# TODO 4: The greatest decrease in profits (date and amount) over the entire period

for i in change:
    if i > greatest_increase:
        greatest_increase = i
        index_GI = change.index(i)
    elif i < greatest_decrease:
        greatest_decrease = i
        index_GD = change.index(i)

print(f"The Greatest increase is {greatest_increase} happened in {change_range[index_GI]}")
print(f"The Greatest decrease is {greatest_decrease} happened in {change_range[index_GD]}")

# TODO 5: WRITE TO FILE

with open('Analysis/Analysis.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_amount}\n")
    f.write(f"Average Change : ${round(statistics.mean(change), 2)}\n")
    f.write(f"Greatest increase is (${greatest_increase}) happened in {change_range[index_GI]}\n")
    f.write(f"Greatest decrease is (${greatest_decrease}) happened in {change_range[index_GD]}\n")
