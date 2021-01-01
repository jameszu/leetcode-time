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