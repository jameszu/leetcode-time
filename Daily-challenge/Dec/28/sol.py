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