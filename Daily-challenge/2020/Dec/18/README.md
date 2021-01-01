# Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        idx = 0
        lenz = len(nums)
        temp = temp2 = float('inf')
        count = 0
        for idx in range(lenz):
            if nums[idx] <= temp:
                temp = nums[idx]
            elif nums[idx] <= temp2:
                temp2 = nums[idx]
                
            
            else:
                return True
            
        return False
```