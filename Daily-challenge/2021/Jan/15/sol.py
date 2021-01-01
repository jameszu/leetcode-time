class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        
        for i in nums:
            lst += [i**2]
            
        return sorted(lst)