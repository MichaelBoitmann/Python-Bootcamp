# Day 2
# Data Types, Numbers, Operations, Type Conversion, f-Strings

# # Input Number then convert to string
# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# Challenge 1

two_digit_number = input("Type a two digit number: ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)