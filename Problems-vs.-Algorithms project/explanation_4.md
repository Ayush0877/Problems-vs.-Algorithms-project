# Dutch National Flag Problem

# Reasoning

since we only have 3 values, all we need to do is put the 2's at the end and 0 at the start and the array will be sorted, we can do that by having an index for the zeros at the start of the array `low_index`, index for the twos at the end `high_index`, and an index to iterate through the array with `index`.
while `index` is less than `high_index` then we haven't walked the whole input list once yet:

- so we keep checking if `high_index` is over a 2 we reduce it by 1
- otherwise if `index` is over a 0 we swap it with `low_index` and move them both 1 forward
- otherwise if `index` is over a 2 we swap it with `high_index` and reduce `high_index` by 1

by the end the 2's will be at the end, the zeros at the start, the 1's in the middle.

# Efficiency

- Time Complexity: we only loop through the input list once, and do O(1) operations in each loop, so the time complexity of the solution is 'O(n)'.

- Space Complexity: all the operations on the input list are in place, we only use 3 variables for the indecies, so the space complexity is 'O(1)'.
