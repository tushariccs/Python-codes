from numpy import *
# # Multi-Demsional Array
# arr = array([[1, 2, 3],
#              [1, 2, 3],
#              [1, 2, 3]])
# print(arr.dtype)
# print((arr.ndim)+1)
# print(arr.shape)
# print(arr.size)
# # Converts two d array in single dimensional array

# arr2 = arr.flatten()
# arr3 = array([[]])
# print(arr2)


# # Converts single d array in three dimensional array

# arr = array([[1, 2, 3, 4, 5, 6, 7, 8],
#              [1, 2, 3, 4, 5, 6, 7, 8]])
# # we can convert any array in other shape as per the no of elements
# # please calculate the no of elements to type parameter in reshape method
# arr3 = arr.reshape(2, 4, 2)
# print(arr3)

# # list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# # print(list)

# operations in matrix
# to convert an array into matrix we have matrix function which does that.

# arr1 = array([[1, 2, 3, 4],
#               [4, 5, 6, 7]])
# m = matrix(arr1)
# print(m)
# arr2 = array([[1, 2, 3, 4], [4, 5, 6, 7]])
# m1 = matrix(arr2)
# m3 = m - m1
# print(m3)

# we don't need to define array to create a matrix we have another way i.e as follows
m = matrix('1 2; 3 4; 5 6 ; 4 5 ;6 7 ;8 9')
print(m)
# here ; divides the values in the row
'''[[1 2]
    [3 4]
    [5 6]
    [4 5]]'''
# in this pattern

# if we need only diagonal elements only then
m1 = matrix('1 2 3;6 4 5; 1 6 7')
print(m1)
# diagonal elements
print(diagonal(m1))
# min element from the matrix
print(m1.min())
# max element from the matrix
print(m1.max())

# multiplication of matrices
m1 = matrix('1 2 3;6 4 5; 1 6 7')
m2 = matrix('1 2 3;6 4 5; 1 6 7')

m3 = m1 * m2
print(m3)
