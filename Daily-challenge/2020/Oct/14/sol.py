class Solution:
    def rob(self, nums: List[int]) -> int:
        def idk(nums, lo, hi):
            yes, no = 0, 0
            for i in range(lo, hi):
                num = nums[i]
                yes, no = no + num, max(yes, no)
            return max(yes, no)

        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(idk(nums, 1, n), idk(nums, 0, n-1))