#1 occurance of each number
# x = int(input("Enter the number"))

number = [10,20,30,20,40]
occurence_number = dict()
for numbers in number:
    if numbers in occurence_number:
        occurence_number[numbers] +=1
    else:
        occurence_number[numbers] = 1

print(occurence_number)     
