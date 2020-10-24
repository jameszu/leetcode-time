# 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109 <br>

## Idea
Fairly interssting and hard question, multiple ways to solve it. <br>
Either brute force with n^2 or even binary search. <br>
I used a stack which makes it linear and it also makes life ezier.<br>

## Code
```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, s3 = [], -float("inf")
        for n in nums[::-1]:
            if n < s3: return True
            while stack and stack[-1] < n: s3 = stack.pop()
            stack.append(n)
        return False
```
