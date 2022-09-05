###############################################################
# Lecture for if/else/elif statement
###############################################################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age < 12:
		print("Please pay $5.")
	elif age <= 18:
		print("Please pay $7.")
	else:
		print("Please pay $12.")
else:
	print("Sorry, you have to grow taller before you can ride.")

###############################################################
# Challenge 1 = Odd or Even
###############################################################
print("Let me guess your number if odd or even")
number = int(input("Please key-in any number: "))

if number % 2 == 0:
	print(f"{number} is Even")
else:
	print(f"{number} is Odd")

###############################################################
# Challenge 2 = BMI 2.0
###############################################################

BMI = round(weight / height ** 2)

if BMI < 18.5:
    print(f"You BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"You BMI is {BMI}, you are normal weight.")
elif BMI < 30:
    print(f"You BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"You BMI is {BMI}, you are obese.")
else:
    print(f"You BMI is {BMI}, you are clinically obese.")