import timeit
import sys
#tuple:ordered,immutable,allows duplicate elemenets
#can not be changed after the creation
tuple1 = ("Max",23,"Canada")
print(tuple1)
print(type(tuple1))

#another way of declareation
tuple2 = tuple(["Hii","how","are","u"])
print(type(tuple2))
print(tuple2)

#list vs tuples
#immutable->list


#size
first_list = ["Max",23,"Canada"]
print(sys.getsizeof(first_list))
print(sys.getsizeof(tuple1))

#size diffenence is between tuple and list 
 
#initialize the tuple

#optional


#single value tuple
single_value = (100)
print(type(single_value))
#it is such that  single_value = 100
single_value = (100,)
print(type(single_value))
#after putting , it behaves like a tuple



#indexing
index = tuple1[0]
print(index)
#check using in keyword 


#length

# check using in
if 23 in tuple1:
    print("23 is in tuple")
else:
    print("23 is not in tuple")
    
    
    
# how many elements are there
second_tuple = (10, 20, 30, 10, 40, 50, 20, 30, 70)
# second_list = [10, 20, 30, 10, 40, 50, 20, 30, 70]
print(second_tuple.count(20))
# print(second_list.count(20))


mark01, mark02, mark03 = input("Enter three subjects marks:").split(",")
print(mark01)
print(mark02)
print(mark03)

name, age, country = ("Max", 23, "Canada")

print(name)
print(age)
print(country)