## Finding the Square Root of an Integer

### Reasoning

when we are findng the floor of the sqrt of a number `X`, then we are searching for a number `N` in the range `(0, X)` that meets a the condition `N^2 = X` or `(N^2 < X) and ((N+1)^2 > X)`, since the range `(0, X)` is sorted, we can use a version of binary search:
if the number is negative sqrt is `None`.
we start with the number itself as `N`.
### Efficiency

- Time Complexity: The Time complexity of binary search (and therefore this solution) is `O(log(n))`. This matches the expected time complexity stated in the problem description.

- Space Complexity: O(1) Constant extra space is needed.
