# Beautiful Arrangement

Solution
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15<br>

## Idea
Just a while loop or for loop is fine

## Code

```python
class Solution:
    def countArrangement(self, N: int) -> int:
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                       for x in X
                       if x % i == 0 or i % x == 0)
        return count(N, set(range(1, N + 1)))
```