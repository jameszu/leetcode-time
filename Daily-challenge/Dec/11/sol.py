class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        idx = 0
        
        count = 0
        
        while idx < len(nums)-1:
            # print(idx)
            if nums[idx] == nums[idx+1]:
                count += 1
            if nums[idx] != nums[idx+1]:
                count = 0

                
            if count >= 2:
                del nums[idx]
            else:
                idx += 1
        return len(nums)
                
            