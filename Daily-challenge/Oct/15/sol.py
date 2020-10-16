# Mine
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenz = len(nums)
        k = k % lenz
        if k == 0:
            return nums
        nums += nums[:-k]
        del nums[:lenz-k]
# Bad, its n^2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            n = nums.pop()
            nums.insert(0, n)
        
# Wow wtf
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a = nums[len(nums)-k:]
        a += nums[0: len(nums) - k]
        nums[:] = a