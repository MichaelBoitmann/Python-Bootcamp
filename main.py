# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇

# name_list = len(names)
# random_choice = random.randint(0, name_list-1)
# next_person_play = names[random_choice]

next_person_play = random.choice(names)
print(next_person_play + " is going to buy a meal today!")

# Angela, Ben, Jenny, Michael, Chloe