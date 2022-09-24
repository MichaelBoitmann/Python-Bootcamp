from replit import clear
from art import logo


# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# Recursion
def calculator():

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True
    
    while should_continue:         
        math_operation = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation = operations[math_operation]
        answer = round(calculation(num1, num2), 4)
       
        print(f"\n{num1} {math_operation} {num2} = {answer}\n")
       

        continue_calculation = input(f"Type \n 'y' to continue calculating with {answer} \n 'n' to start a new calculation \n 'q' to quit. ")
    
        if  continue_calculation == 'y':
            num1 = answer
        elif continue_calculation == 'n':
            # Below will cause the recursion of the function until not being called
            should_continue = False
            calculator()
        else:
            break
calculator()
