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
# Challenge  - highest score
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
