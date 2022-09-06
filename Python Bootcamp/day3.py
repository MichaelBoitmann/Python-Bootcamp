###############################################################
# Lecture for if/elif/else statement
###############################################################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age < 12:
        bill = 5
		print("Please pay $5.")
	elif age <= 18:
        bill = 7
		print("Please pay $7.")
	else:
        bill = 12
		print("Please pay $12.")

    includes_photo = input("Do you want a photo taken? Y or N.")
    if includes_photo == "Y":
        bill += 3

print(f"Your final bill is {bill}")
else:
	print("Sorry, you have to grow taller before you can ride.")

###############################################################
# Challenge 1 = Odd or Even
###############################################################
# 🚨 Don't change the code below 👇
print("Let me guess your number if odd or even")
number = int(input("Please key-in any number: "))
# 🚨 Don't change the code above 👆

if number % 2 == 0:
	print(f"{number} is Even")
else:
	print(f"{number} is Odd")

###############################################################
# Challenge 2 = BMI 2.0
###############################################################

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight / height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")


###############################################################
# Challenge 3 = Leap Year
###############################################################

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

###############################################################
# Challenge 4 = Python Pizza
###############################################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")

###############################################################
# Challenge 5 = Love Calculator
###############################################################
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):    
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


###############################################################
# Challenge 6 = Treasure Island
###############################################################
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")