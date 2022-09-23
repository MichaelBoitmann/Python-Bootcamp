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