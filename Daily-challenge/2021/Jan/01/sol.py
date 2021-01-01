class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dict1 = { p[0]: p for p in pieces }
        
        res = []
        
        for i in arr:
            res += dict1.get( i, [] ) 
            
        return res == arr