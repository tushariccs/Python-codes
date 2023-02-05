# declare
student_name = "John Doe"
student_roll_no = 27
student_height = 6.2
#type
print(student_name,type(student_name))
print(student_roll_no,type(student_roll_no))
print(student_height,type(student_height))
#address
age = 25
new_age = 23
print("current address: ",id(age))

age = 23
print("new address: ",id(age))
print("new address: ",id(new_age))
#point to same location in memory i.e age and new_age

#how variable is stored in a memory location

#global / local variable
#global variable counter
counter = 0

def increment_counter():
    #def increment_counter()->str:
    global counter
    #local variable in counter
    
    #counter = 10
    counter=+1
    print("local variable: ",counter)
    
increment_counter()
print("global variable: ",counter)
