###############################################################
# Lecture - for loop with range
###############################################################
for number in range(1, 101):
    total += number
print(total)

###############################################################
# Challenge 1 - average height
###############################################################

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Number of Students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average Height = {average_height}")

###############################################################
# Challenge 2 - highest score
###############################################################

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

###############################################################
# Challenge 3 - sum of even numbers in range of 100
###############################################################
#Write your code below this row 👇
total = 0
for number in range(0, 101, 2):
    total += number
    # print(number) # will print each number
print(total)

# another sulution

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)

###############################################################
# Challenge 4 - fizz, buzz or fizzbuzz (divisible by 3 or 5 or 3 and 5)
###############################################################
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)