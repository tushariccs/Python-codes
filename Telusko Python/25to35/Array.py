import array as arr
# if u want some specified method then we use
from array import *

# array conatins element of same datatype
# to specify datatype we don't use keywords such as int,float
# we use Typecode for specifying it
# unsigned integers -> 0 to +ve number doesn't include -ve numbers
# An unsigned integer is a 32-bit non-negative integer(0 or positive numbers) in the range of 0 to 2^32-1
# A signed integer is a 32-bit integer in the range of -(2^31) = -2147483648 to (2^31) – 1=2147483647 which contains positive or negative numbers.
# It is represented in two's complement notation. An unsigned integer is a 32-bit non-negative integer(0 or positive numbers) in the range of 0 to 2^32-1.

vals = array('i', [5, 9, 8, 4, 2])
print(type(vals))
print(vals)


# vals = array('i', [5, 9, -8, 4, 2])
# print(type(vals))
# print(vals)
# if we add a float value in the array it will throw an error
# i defines all negative and positive value


# vals = array('I', [5, 9, -8, 4, 2])
# print(type(vals))
# print(vals)
# if we have I as a specifier of dataype is doesn't have negative value i.e unsigned int
# if we type a negative value then it will throw an error

print(vals.buffer_info())
# it will give size of an array
# O/P: it is tuple (2529597570480, 5)
#                      ^           ^
#                      |           |
#                   address      size

print(vals.typecode)
# o/p : i
# that defines the typecode of the array that is the datatype
vals.reverse()
print(vals)
print(vals[1])


# to print whole array
for i in vals:
    print(i)

# unicode
uni = array('u', ['a', 'b', 'c', 'd'])
print(uni)

# to make a new Array

newArr = array(vals.typecode, (a for a in vals))
for i in newArr:
    print(i)


# methods of array
# insertion of an element at the end of an array
vals.append(32)
print(vals)

# remove an element from an array
vals.pop()
print(vals)

vals.remove(8)
print(vals)

vals.append(2)
print(vals)
print(vals.count(2))

# insert(5, 1) where 5 is the position and 1 is the element added
vals.insert(5, 1)
print(vals)
