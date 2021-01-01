class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        lenz = len(flowerbed)
        count = 0
        
        while i < lenz and count < n:
            if flowerbed[i] == 0:
                if i == lenz - 1: 
                    nex = 0 
                else: nex = flowerbed[i+1]
                if i == 0: 
                    prev = 0 
                else: 
                    prev = flowerbed[i-1]
                if nex == 0 and prev == 0:
                    flowerbed[i] = 1
                    count += 1
                    
            i += 1
        return count == n