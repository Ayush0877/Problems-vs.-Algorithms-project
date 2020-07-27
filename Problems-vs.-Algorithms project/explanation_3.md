# Rearrange Array Elements

# Reasoning
By using the largest numbers from the input list as the most significant digits in the generated numbers, we are guaranteed to find the largest possible numbers.

For example:
```python
input_list = [1, 2, 3, 4, 5]
sorted_list = [5, 4, 3, 2, 1]

since we know elements in input can only be [0-9] then we can create an array of size 10 with each index representing an element and loop through the input to count the maximum_sum of each number, 
then we loop through the maximum_sum array from last index to the first, and at each index we loop adding digits to the numbers until the maximum_sum is 0.
then, we return the output of the two numbers.

# Efficiency of solution:

- Time Complexity: we create the size 10 maximum_sum array O(1), then iterate through the input list once to count the maximum_sums of each digit 'O(n)', 
  then we loop through the maximum_sum array O(1), performing at most O(n) operations through each iteration.
  therefore our time complexity is 'O(n)'.

- Space Complexity: we make a size 10 array, regardless of the input. therefore our space complexity is 'O(1)'.
