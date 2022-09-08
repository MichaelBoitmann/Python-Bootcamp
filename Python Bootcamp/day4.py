###############################################################
# Lecture for random / randint() / random()
###############################################################
import random

random_integer = random.randint(1, 1000)
print(random_integer)

random_float = random.random()
print(format((random_float * 100), '.2f'))

randomFloat = random.random() * 5
print("randomFloat")

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

###############################################################
# Challenge 1 - Heads or Tails
###############################################################
import random

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")

###############################################################
# Challenge 2 - random names
###############################################################

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇
name_list = len(names)
random_choice = random.randint(0, name_list-1)
next_person_play = names[random_choice]

# next_person_play = random.choice(names)
print(next_person_play + " is going to buy a meal today!")

# Angela, Ben, Jenny, Michael, Chloe