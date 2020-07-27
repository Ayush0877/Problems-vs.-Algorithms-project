def get_min_max(array):
   """
   Return a tuple(min, max) out of list of unsorted integers.
   Args:
      ints(list): list of integers containing one or more integers
   """
   min_int = array[0]
   max_int = array[0]


   for i in array:
      if i <min_int:
         min_int = i
      elif i >max_int:
         max_int = i
         
   return (min_int, max_int)




## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(get_min_max([9,8,3,4,5]))
# expected output:(3, 9)
print ("Pass" if ((3, 9) == get_min_max(l)) else "Fail")
print('-----------------------------')

print(get_min_max([1]))
# expected output:(1, 1)
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print('-----------------------------')

print(get_min_max([1,1,1,2,5]))
# expected output:(1, 5)
print ("Pass" if ((1, 5) == get_min_max([1,1,1,2,5])) else "Fail")
print('-----------------------------')

print(get_min_max([2,3,4,7,9]))
# expected output:(2, 9)
print ("Pass" if ((2, 9) == get_min_max(l)) else "Fail")
print('-----------------------------')
