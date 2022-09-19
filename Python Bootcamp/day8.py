###########################################################################
# Positional and Keyword Argument
###########################################################################
# Review: 
# Create a function called greet(). 
# desc1, desc2, and line1 are called parameters
def greet(desc1, desc2, line1):
    
# Write 3 print statements inside the function.
    print(f"Hello {line1}!")
    print("I am looking forward to be good in Pyhton!")
    print(f"I just need a great {desc1} and {desc2}!")
    
# Call the greet() function and run your code.
# Inside the call greet() are arguments
greet("encouragement", "passion", "Pythonians")


###########################################################################
# Paint Area Calculator
###########################################################################

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("Number of Coverage: "))

# Calling out the function
paint_calc(height=test_h, width=test_w, cover=coverage)

###########################################################################
# Prime Number Checker
###########################################################################

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number.")
    else: 
        print("It is not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)