# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

'''
Datatypes
None
Numeric
List
Tuples
Set
String
Range 
Dictionary
'''

#NUMERIC
#If a variable is defined but not assigned a value then is it a none datatype/null datatype

#int
num = 2.5
print(type(num))

#float
num = 5
print(type(num))

#complex
#format = a+bj
# j->imaginary number
num = 9+6j
print(type(num))

#typecasting the element a into int by using b variable
a = 5.6
b = int(a)
print(type(b))
print(b)

k = float(b)
print(k)

k = 6
c = complex(b,k)
print(c)
#o/p->5+6j where j is an imaginary number
bool  = k>b
print(bool)
print(type(bool))

print(int(True))
print(int(False))


#SEQUENCE
list = [1,2,3,4,5,6,7]
print(type(list))

tuple = (1,2,3,4,5)
print(type(tuple))

#set is mutable
set = {1,2,3,4,5,6}
print(type(set))

x = range(10)
print(x)

#Mapping 
dict = {"Name":"Tushar","Class":"A","Course":"FYMCA","Subject":"Python"}
print(type(dict))

#String
a = "Tushar"
b = a.upper()
print(b)

a = frozenset({2,3,4,5,6,7,8,9})
print(type(a))

