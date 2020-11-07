class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        eve = 0
        odd = 0
        for i in position:
            if i % 2 == 0:
                eve += 1
            else:
                odd += 1
                
        return min(eve, odd)