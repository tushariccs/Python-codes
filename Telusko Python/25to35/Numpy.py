# we can't work with multidemsional array in python.
'''If we try to do that in this faction
from array import *
arr  = array('i',[1,2,3,4],[5,6,7,8])
print(arr)
These above code throws an error

To do these we use third party package numpy
'''

from numpy import *
arr = list([[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6]])
print(arr)
print(arr.__getitem__(1))
# [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]
# [2, 3, 4, 5, 6]
