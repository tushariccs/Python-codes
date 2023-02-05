num = 5

'''
Memory allocation
 _______
|       |
|   5   |
|_______|
<address>
  num
  object
'''


# to get a address of the variable we use id function

print(id(num))

tuple = (5,6,7,8,8,9)
print(id(tuple[1]))

#if we use id(tuple[0]) it is same as value of num that is 5 so the address is same as they are pointing each 
#other

name = "Tushar"
print(id(name))

a = 10 
b = a 
print(id(a))
print(id(b))
# b is pointing to a 
# that is the reason python is memory efficient
#Everthing in python is an object if we consider a,b,name,tuple also
k = 10
print(id(k))

'''
Memory allocation
 _______
|       |
|  10   |
|_______|
<address>
address can chnage
  a,b,k
  object
'''
a = 9
print(id(a))
print(b)

'''
Memory allocation
 _______
|       |
|   9   |
|_______|
<address>
  a
  object
'''
b = 8 
print(id(b))

#here it comes a concept of garbage collection
#if some variable is not used and create different object of same name has assigned a different value then it
#undergoes garbage collection is deleted

pi = 3.14
print(type(pi))


