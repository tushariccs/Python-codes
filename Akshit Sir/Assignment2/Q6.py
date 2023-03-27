# def adjust(input_number):

#     round_of_value = input_number % 10
#     if (round_of_value == 1 or round_of_value == 2):
#         value = input_number - round_of_value
#         print("The round off value of the number is: ", value)

#     if (round_of_value == 3):
#         value = input_number+2
#         print("The round off value of the number is: ", value)
#     if (round_of_value == 4):
#         value = input_number+1
#         print("The round off value of the number is: ", value)
#     if (round_of_value == 6):
#         value = input_number-1
#         print("The round off value of the number is: ", value)
#     if (round_of_value == 7):
#         value = input_number-2
#         print("The round off value of the number is: ", value)
#     if (round_of_value == 8):
#         value = input_number+2
#         print("The round off value of the number is: ", value)
#     if (round_of_value == 9):
#         value = input_number+1
#         print("The round off value of the number is: ", value)


# number = int(input("Enter a value: "))
# adjust(number)
def roundOff(Take_number):
    String_value = Take_number
    String_value = String_value.split('.')
    print(String_value)
    rounded_value = 0
    rounded_value = int(String_value[1])
    print(rounded_value)
    rounded_valued = rounded_value % 10
    print(rounded_valued)
    if (rounded_valued == 1 or rounded_valued == 2):
        value = rounded_value - rounded_valued
        print("The round off value of the number is: ", value)
    if (rounded_valued == 0):
        value = rounded_value+0
        print("The round off value of the number is:",
              str(String_value[0]), '.', value)
    if (rounded_valued == 3):
        value = rounded_value+2
        print("The round off value of the number is:",
              str(String_value[0]), '.', value)
    if (rounded_valued == 4):
        value = rounded_value + 1
        print("The round off value of the number is: ",
              str(String_value[0]), '.', value)
    if (rounded_valued == 6):
        value = rounded_value-1
        print("The round off value of the number is: ",
              str(String_value[0]), '.', value)
    if (rounded_valued == 7):
        value = rounded_value-2
        print("The round off value of the number is: ",
              str(String_value[0]), '.', value)
    if (rounded_valued == 8):
        value = rounded_value+2
        print("The round off value of the number is: ",
              str(String_value[0]), '.', value)
    if (rounded_valued == 9):
        value = rounded_value+1
        print("The round off value of the number is: ",
              str(String_value[0]), '.', value)


# pass value as a String
number = input("Enter a number: ")
roundOff(number)
