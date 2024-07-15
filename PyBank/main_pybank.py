# Import the operating system module for creating file path
# Import CSV module for reading CSV file
import os
import csv

# Define the path for the CSV file that we are going to use
csvpath = os.path.join("Resources", "budget_data.csv")

# Create lists for storing needed data
date = []
changes_profit_losses = []

# Set initial value to the variables needed
total_months = 0
total_amount = 0

# Open and read the CSV file
with open(csvpath) as budget_data:
    
    # 'delimiter=","' is default, so we don't need to enter that parameter
    budget_data_reader = csv.reader(budget_data)

    # To skip the header
    next(budget_data_reader,None)
    
    # To loop through each row after header
    for row in budget_data_reader:

        # To count rows for calculating the total number of months
        total_months = total_months + 1

        # To sum up the column "Profit/Losses" for calculating the net total amount.
        # Use "float" in case there are decimal numbers 
        total_amount = total_amount + float(row[1])      
        
        # Set a condition in order to set the first row's profit/loasses as the startpoint 
        # For calculating the changes over the entire period
        if total_months == 1:
            previous_profit_losses = float(row[1])

        else:
            # Add current date to the "date" list to track the corresponding changes
            date.append(row[0])

            current_profit_losses = float(row[1])
            changes = current_profit_losses - previous_profit_losses

            # Add the changes to the "changes_profit_losses" list for calculating the average, greatest increase/decrease later
            changes_profit_losses.append(changes)

            # Reset the previous_profit_losses for calculating next period's change
            previous_profit_losses = current_profit_losses

# To calculate the average of changes and round the result to 2 decimals
changes_sum = sum(changes_profit_losses)
changes_average = round(changes_sum/len(changes_profit_losses),2)

# Use function "max" and "min" to find the greates increase/decrease in the "changes_profit_losses" list
greatest_increase = max(changes_profit_losses)
greatest_decrease = min(changes_profit_losses)

# To retrieve the index of the greates increase/decrease for reference while getting the corresponding date in the "date" list
greatest_increase_index = changes_profit_losses.index(max(changes_profit_losses))
greatest_decrease_index = changes_profit_losses.index(min(changes_profit_losses))
greatest_increase_date = date[greatest_increase_index]
greatest_decrease_date = date[greatest_decrease_index]


# To print out results in terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Amount: ${total_amount}")
print(f"Average of changes: ${changes_average}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


# Use "csv.writer" to export the results a text file
output_file = os.path.join("analysis", "financial analysis.txt")
with open(output_file,"w") as text:
    writer = csv.writer(text)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Net Total Amount: ${total_amount}"])
    writer.writerow([f"Average of changes: ${changes_average}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"])
