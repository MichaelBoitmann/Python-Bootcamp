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
# Lecture for list
###############################################################

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

num_of_states = len(states_of_america)

print(states_of_america[num_of_states -1])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

## Output
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]


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

###############################################################
# Challenge 3 - treasure map
###############################################################
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


###############################################################
# Challenge 4 - rock paper scissors
###############################################################
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_choice >= 3 or user_choice < 0:
	print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
    	print("You win!")
    elif computer_choice == 0 and user_choice == 2:
    	print("You lose")
    elif computer_choice > user_choice:
    	print("You lose")
    elif user_choice > computer_choice:
    	print("You win!")
    elif computer_choice == user_choice:
    	print("It's a draw")