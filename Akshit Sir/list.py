#what is list
#list: ordered, mutable, allows duplicate elements
#Everthing in python is an object
student_name = [10,20,30,40,50]
print(student_name)

for number in student_name:
    print(number)
    
#indexing
print(student_name[0])
print(student_name[1])
print(student_name[2])
print(student_name[3])

#reverse indexing
last_element_index = len(student_name) - 1
print("Last element index",last_element_index)
print("Last element ",student_name[last_element_index])

print(student_name[-1])

#length
print(len(student_name))

#delete element
print("Before list",student_name)
del student_name[2]
print("After delete the element in the list",student_name)

#list remove
student_name.remove(40)
print("After deleting the value 40",student_name)

#pop
print("\n")
numbers = [10,20,30,40,50]
print("Before poping the element: ",numbers)
deleted_value = numbers.pop()
print("Deleted value is: ",deleted_value)
print("After poping the element",numbers)


#clear
#clear or deleted all the list
# numbers.clear()
# print(numbers)

#append
print("Before the append element",numbers)
numbers.append(100)
numbers.append(200)
numbers.append(400)
print("AFter the element append is: ",numbers)

#extend
numbers.extend(student_name)
print("After the extend is: ",numbers)

#insert
numbers.insert(2,800)
print(numbers)

#multiply elements
zeros = [0]*10
print(zeros)

#reverse
numbers.reverse()
print(numbers)

#copy list
#print(numbers)
copied_list  = numbers
#In this to understand the copied_list and number are pointing to each other.
print("Copied numbers: ",copied_list)
print("Original numbers",numbers)

numbers.append(10000)

print("Original numbers",numbers)
print("Copied numbers: ",copied_list)

#append two list
numbers.extend(copied_list)
print("New numbers list",numbers)
# for value in enumerate(numbers):
#     print(value)

#one liner
multipy_by_2 = [number*number for number in range(1,10)]
print(multipy_by_2)

square_list = []

for numbers in range(1,10):
    result = number * number
    square_list.append(result)
print(square_list)

#slicing
