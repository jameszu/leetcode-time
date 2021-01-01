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