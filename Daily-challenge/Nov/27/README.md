# Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumn = sum(nums) 
        if sumn % 2 or len(nums) < 2 :
            return False
        
        subSum = sumn // 2
        nums.sort(reverse = True)
        
        for i in range(1 ,len(nums)) :
            tmp = nums[0]
            for j in range(i ,len(nums)) :
                tmp += nums[j]
                if tmp > subSum :
                    tmp -= nums[j]
                elif tmp == subSum :
                    return True
        
        return nums[0] == subSum
        
```