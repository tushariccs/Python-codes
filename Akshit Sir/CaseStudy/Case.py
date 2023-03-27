# a = int(input("Please Enter 1 for Sign Up: "))
# a = int(input("Please Enter 2 for Sign in: "))
# a = int(input("Please Enter 3 for Quit: "))
import re


def case():
    print("Please Enter 1 for Sign Up: ")
    print("Please Enter 2 for Sign in: ")
    print("Please Enter 3 for Quit: ")
    a = int(input("Please Enter the value"))
    if (a == 1):
        Sign_Up()
    # if (a == 2):
    #     Password_Validation()


def Sign_Up():
    fixed_number = 0
    mobile_number = (
        input("The 10 digit mobile number must start with 0: "))
    # mobile_number = str(mobile_number)
    # print(type(mobile_number))
    # first_number = int(str(mobile_number)[0])

    # print(first_number)
    if (mobile_number[0] == '0'):
        fixed_number = mobile_number
        # print(fixed_number)
    else:
        print("Enter the valid number")
    # print(fixed_number)


# Email

    s = input("Enter your password")
    count = 0
    for i in s:
        if (s == '@' or s == '&'):
            count += 1
    if (count > 0):
        print("Password is valid")
    else:
        print("Password is invalid")


case()
