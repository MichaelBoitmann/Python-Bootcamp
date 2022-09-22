#####################################
# Python Dictionary: Deep Dive
####################################

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# # Retrieving items from dictionary.
# print(programming_dictionary["Function"])

# #Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# # Create an empty dictionary.
# empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "More incoming bugs are produced each time."
# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

###############################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "New Zealand": {"cities_visited": ["Auckland", "Wellington", "ChristChurch"], "total_visits": 5},
}

# Nesting Dictionary in a list
travel_log = {
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12
    },
    {"country": "New Zealand",
     "cities_visited": ["Auckland", "Wellington", "ChristChurch"], 
     "total_visits": 5},
}










#####################################
# Challenge - Grading Program
####################################
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)

#####################################
# Challenge - Secret Auction Program
####################################

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder.upper()
    print("####################################################")  
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print("####################################################")  

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        clear()
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
  

"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 

https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076

"""
