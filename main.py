print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

tip_amount = format((int(total_bill) * (int(percentage) / 100)), '.2f')

convert_percentage = float(1 + (int(percentage) / 100))

num_people = int(input("How many people to split the bill? "))

bill_distribution = format((total_bill * convert_percentage) / num_people, '.2f')

print("\n\nYour Receipt")
print(f"Total Bill: ${format(total_bill, '.2f')}")
print(f"Selected Percentage: {percentage}%")
print(f"Number of People: {num_people}\n")
print(f"Each person should pay ${bill_distribution}\nTip Amount: ${tip_amount}")