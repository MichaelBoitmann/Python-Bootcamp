# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert the string to a float
height_num = float(height)
weight_num = float(weight)

# Use the BMI calculation
BMI = weight_num / height_num ** 2

# Use format to round of the float output to 2 decimal number
print("Your BMI is " + format(BMI, '.2f'))