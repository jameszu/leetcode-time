# Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length<br>

## Idea
Just do while loop and convert to decimal

## Code
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], w: int) -> List[int]:
        max_left = [0 for n in range(len(nums))]
        max_right = [0 for n in range(len(nums))]
        max_left[0] = nums[0]
        max_right[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            if i % w == 0:
                
                max_left[i] = nums[i]
            else:
                max_left[i] = max(nums[i], max_left[i-1])
                
            
            j = len(nums) - i - 1
            
            if j % w == 0:
                max_right[j] = nums[j]
            else:
                max_right[j] = max(nums[j], max_right[j+1])
        # print(max_right, max_left)
        lst = []
        x = 0
        # j = 0
        while x + w <= len(nums):
            # j += 1
            # print(j)
            lst += [max(max_right[x], max_left[x+w-1])]
            x += 1
            
        return lst
        
```