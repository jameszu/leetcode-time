# Rotate Array

Solution
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105 <br>
---

## Idea
Mine one is just appedn the array and del the first part.<br>
A naive way would be a for loop and a O(n) function like insert inside. <br>
A god way is to create a array and optimise it to super fast.<br>
btw this should be just a eazy question.
## Code
```python
# Mine
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenz = len(nums)
        k = k % lenz
        if k == 0:
            return nums
        nums += nums[:-k]
        del nums[:lenz-k]
# Bad, its n^2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            n = nums.pop()
            nums.insert(0, n)
        
# Wow wtf
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a = nums[len(nums)-k:]
        a += nums[0: len(nums) - k]
        nums[:] = a
```