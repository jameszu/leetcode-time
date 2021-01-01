class Solution:
    def longestMountain(self, A: List[int]) -> int:
        total = 0
        
        length = len(A)
        if length <= 2:
            return 0
        
        pointer = 0
        
        while pointer <= length-2:
            base = pointer
            while pointer + 1 < length and A[pointer] < A[pointer+1]:
                pointer += 1
            
            if pointer == base:
                pointer += 1
                continue
            
            peak = pointer
            while pointer + 1 < length and A[pointer] > A[pointer+1]:
                pointer += 1
            
            if peak == pointer:
                continue
                
            total = max(total, pointer - base + 1)
            
        return total