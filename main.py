print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

tip_amount = format((int(total_bill) * (int(percentage) / 100)), '.2f')

convert_percentage = 1 + (int(percentage) / 100)

num_people = input("How many people to split the bill? ")

bill_distribution = format((float(total_bill) * float(convert_percentage)) / int(num_people), '.2f')

print("\n\nYour Receipt")
print(f"Total Bill: ${total_bill}")
print(f"Selected Percentage: {percentage}")
print(f"Number of People: {num_people}\n")
print(f"Each person will contribute a total of ${bill_distribution} to give a tip of amount of ${tip_amount}")