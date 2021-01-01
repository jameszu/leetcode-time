# 4Sum II
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
 <br>

## Idea

## Code
```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        num_dict = {}
        for i in C:
            for j in D:
                s = i + j
                if s in num_dict:
                    num_dict[s] += 1
                else:
                    num_dict[s] = 1

        for i in range(len(A)):
            for j in range(len(B)):
                target = 0 - (A[i]+B[j])
                if target in num_dict:
                    count += num_dict[target]
        return count
```
 