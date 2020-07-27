# Max and Min in a Unsorted Array

# Reasoning:

since we proving that the input list has at one element or more we can start by thinking that the first element is the min and max.
then loop through the entire list and for each element test if it's smaller then min, then assign it's value to min, otherwise if it's larger than max assign it's value to max.
at the end of iteration through the array we have both min and  max.

# Efficiency:

Time Complexity: we're iterating once through the entire array, making O(1) operations at each iteration, and then returning min and max,
  so the time complexity is 'O(n)'.

Space Complexity: since, we only using 2 variables regardless of the input, so the space complexity is 'O(1)'.
