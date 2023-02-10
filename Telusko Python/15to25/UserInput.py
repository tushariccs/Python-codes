# By default it is String
# x = int(input("Enter the number1: "))
# y = int(input("Enter the number2: "))
# z = x+y
# print("The sum of two numbers: ", z)

# input function returns always string,so we need typecast the value
# result = input("To check datatype of the variable: ")
# print(type(result))

# We need a char
# char = input('enter a char: ')
# print(char[0])

# # We need to take a single char then
# char1 = input('Enter a char: ')[0]
# print(char1)

# Use Eval it needs the expression to execute
# result = eval(input('Enter a Expression: '))
# print(result)

# Taking input from the command line
# we use argv
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print(z)
