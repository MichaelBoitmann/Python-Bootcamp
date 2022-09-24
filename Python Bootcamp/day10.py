#####################################
# Functions with Outputs
#####################################

def format_name(f_name, l_name):
    f_name.title()
    l_name.title()

###################################################
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("michael", "BOITMANN")

###################################################
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("michael", "BOITMANN")


################################################################
# Return is the key word that will make the function with output

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("michael", "BOITMANN"))

#########################################################
# Added if statement
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide a valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

######################################################
# Leap year challenge
#####################################################

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
    
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


########################################################
# Challenge - simple calculations using dictionary
########################################################

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
    print(symbol)
math_operation = input("Pick an operation from the line above: ")

calculation_function = operations[math_operation]
answer = calculation_function(num1, num2)


print(f"{num1} {math_operation} {num2} = {answer}")