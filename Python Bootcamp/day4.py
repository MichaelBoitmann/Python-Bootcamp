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