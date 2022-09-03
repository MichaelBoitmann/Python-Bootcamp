# Day 2
# Data Types, Numbers, Operations, Type Conversion, f-Strings

# # Input Number then convert to string
# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

###############################################################
# Challenge 1 = adding 2 digits
###############################################################
# two_digit_number = input("Type a two digit number: ")
# # Input digits are in string type
# print(type(two_digit_number))
# # Subcripting each digit to separate
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# # Convert each digit from string to int
# result = int(first_digit) + int(second_digit)
# print(result)

###############################################################
# Challenge 2 -  BMI calculation
###############################################################
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# # Convert the string to a float
# height_num = float(height)
# weight_num = float(weight)

# # Use the BMI calculation
# BMI = weight_num / (height_num ** 2)

# # Use format to round of the float output to 2 decimal number
# print("Your BMI is " + format(BMI, '.2f'))
# # Convert int to str to concatenate to str
# print("Your BMI is " + str(round(BMI)))

###############################################################
# Challenge 3 - Life remaining
###############################################################
# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# new_age = int(age)

# total_days = 90 * 365
# total_weeks = 90 * 52
# total_months = 90 * 12

# consumed_days = new_age * 365
# consumed_weeks = new_age * 52
# consumed_months = new_age *12

# days_left = total_days - consumed_days
# weeks_left = total_weeks - consumed_weeks
# months_left = total_months - consumed_months

# print(f"You have\n {days_left} days,\n {weeks_left} weeks, and\n {months_left} months left.")

###############################################################
# Challenge 4 - Tip Calculator
###############################################################
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")

tip_amount = format((int(total_bill) * (int(percentage) / 100)), '.2f')

convert_percentage = float(1 + (int(percentage) / 100))

num_people = int(input("How many people to split the bill? "))

bill_distribution = format((total_bill * convert_percentage) / num_people,
                           '.2f')

print("\n\nYour Receipt")
print(f"Total Bill: ${format(total_bill, '.2f')}")
print(f"Selected Percentage: {percentage}%")
print(f"Number of People: {num_people}\n")
print(f"Each person should pay ${bill_distribution}\nTip Amount: ${tip_amount}")
