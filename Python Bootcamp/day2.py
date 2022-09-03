# Day 2
# Data Types, Numbers, Operations, Type Conversion, f-Strings

# # Input Number then convert to string
# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

###############################################################
# Challenge 1
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
# Challenge 2
###############################################################
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert the string to a float
height_num = float(height)
weight_num = float(weight)

# Use the BMI calculation
BMI = weight_num / (height_num * height_num)

# Use format to round of the float output to 2 decimal number
print("Your BMI is " + format(BMI, '.2f'))