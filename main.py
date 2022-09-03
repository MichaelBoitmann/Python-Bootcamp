# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age = int(age)

total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12

consumed_days = new_age * 365
consumed_weeks = new_age * 52
consumed_months = new_age *12

days_left = total_days - consumed_days
weeks_left = total_weeks - consumed_weeks
months_left = total_months - consumed_months

print(f"You have\n {days_left} days,\n {weeks_left} weeks, and\n {months_left} months left.")
