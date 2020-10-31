# Number of Longest Increasing Subsequence
Given an integer array nums, return the number of longest increasing subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106 <br>

## Idea
yeah dynamic programming hard as f
## Code
```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp, j = [], 0
        for num in nums:
            l, r = 0, j
            while l < r:
                mid = (l+r)//2
                if min(dp[mid].keys()) < num:
                    l = mid + 1
                else: r = mid
            if l == j:
                j += 1
                dp.append({})
            if l == 0:
                dp[l][num] = dp[l].get(num, 0) + 1
            else: 
                dp[l][num] = dp[l].get(num, 0) + sum(dp[l-1][k] for k in dp[l-1] if k < num)
        return sum(dp[-1].values())
```