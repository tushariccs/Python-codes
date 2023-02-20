import array
from array import *
arr = array('i', [])

a = int(input("Enter the size of an array "))

for i in range(0, a, 1):
    x = int(input("Enter the values in the array"))
    arr.append(x)


def search():
    search_element = int(input("Enter the element to be searched"))
    for i in range(0, len(arr)):
        if (arr[i] == search_element):
            print("Element found")


print(arr)
