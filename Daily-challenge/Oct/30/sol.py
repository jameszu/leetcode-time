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